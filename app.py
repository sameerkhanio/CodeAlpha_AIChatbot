from flask import Flask, request, render_template_string, jsonify
import re

app = Flask(__name__)

FAQ = [
    (["hello", "hi", "hey", "good morning", "good evening"],
     "Hello! Welcome to CloudAssist. How can I help you today?"),
    (["price", "pricing", "cost", "plans"],
     "Our demo plans are Basic (free), Pro ($9/month), and Business ($29/month). Contact sales for a custom quote."),
    (["hours", "opening", "open", "timing", "working hours"],
     "Our support team is available Monday to Friday, 9:00 AM to 6:00 PM."),
    (["contact", "email", "phone", "reach"],
     "You can contact our support team at support@example.com. We usually reply within one business day."),
    (["refund", "return", "cancel"],
     "For refunds or cancellations, email support@example.com with your order reference. Our team will review your request."),
    (["features", "service", "product", "offer"],
     "CloudAssist provides website support, cloud setup guidance, account assistance, and basic troubleshooting."),
    (["thank", "thanks"],
     "You're welcome! Is there anything else I can help you with?"),
    (["bye", "goodbye", "see you"],
     "Thanks for visiting CloudAssist. Have a great day!")
]

def get_reply(message):
    text = re.sub(r"[^a-z0-9\s]", " ", (message or "").lower())
    words = set(text.split())
    if not words:
        return "Please type a question so I can help."
    best = None
    best_score = 0
    for patterns, reply in FAQ:
        score = sum(1 for p in patterns if p in text or p in words)
        if score > best_score:
            best, best_score = reply, score
    return best if best_score else "I'm not sure I understood that. Try asking about pricing, features, support hours, contact details, or refunds."

PAGE = """
<!doctype html><html><head><meta name="viewport" content="width=device-width,initial-scale=1">
<title>CloudAssist Chatbot</title><style>
body{font:16px Arial;background:#eef2f8;margin:0;color:#172238}.wrap{max-width:760px;margin:35px auto;padding:16px}
.panel{background:white;border-radius:16px;box-shadow:0 8px 30px #17223818;overflow:hidden}
header{background:#2457d6;color:white;padding:22px}header h1{margin:0 0 6px}
#chat{height:390px;overflow:auto;padding:18px;background:#fafcff}
.msg{padding:11px 14px;border-radius:12px;margin:9px 0;max-width:82%;line-height:1.4}
.bot{background:#e8eefb;margin-right:auto}.user{background:#2457d6;color:white;margin-left:auto}
form{display:flex;padding:14px;border-top:1px solid #e4e9f1;gap:8px}
input{flex:1;padding:13px;border:1px solid #ccd4e0;border-radius:8px;font-size:16px}
button{background:#2457d6;color:white;border:0;border-radius:8px;padding:0 20px;cursor:pointer}
small{color:#dce6ff}
</style></head><body><div class="wrap"><div class="panel">
<header><h1>CloudAssist</h1><small>AI-style retrieval chatbot · Website support demo</small></header>
<div id="chat"><div class="msg bot">Hello! I'm CloudAssist. Ask me about pricing, features, support hours, contact details, or refunds.</div></div>
<form id="form"><input id="message" autocomplete="off" placeholder="Type your message..." required><button>Send</button></form>
</div></div>
<script>
const form=document.getElementById('form'), input=document.getElementById('message'), chat=document.getElementById('chat');
function bubble(text,who){const d=document.createElement('div');d.className='msg '+who;d.textContent=text;chat.appendChild(d);chat.scrollTop=chat.scrollHeight;}
form.addEventListener('submit',async e=>{e.preventDefault();const message=input.value.trim();if(!message)return;bubble(message,'user');input.value='';
try{const r=await fetch('/chat',{method:'POST',headers:{'Content-Type':'application/json'},body:JSON.stringify({message})});const data=await r.json();bubble(data.reply,'bot');}
catch(err){bubble('Sorry, the service is temporarily unavailable. Please try again.','bot');}});
</script></body></html>
"""

@app.route("/")
def home():
    return render_template_string(PAGE)

@app.route("/chat", methods=["POST"])
def chat():
    data = request.get_json(silent=True) or {}
    message = str(data.get("message", ""))[:500]
    return jsonify({"reply": get_reply(message)})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001, debug=False)

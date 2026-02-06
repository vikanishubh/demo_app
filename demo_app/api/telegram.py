import frappe
import requests

@frappe.whitelist(allow_guest=True)
def bot_webhook():
    data = frappe.request.get_json()
    
    # Log incoming request (important for debugging)
    frappe.log_error(frappe.as_json(data), "Telegram Webhook Hit")
    
    if not data:
        return "ok"

    # If this is from Telegram
    message = data.get("message")
    if message:
        chat_id = message["chat"]["id"]
        text = message.get("text", "")
        
        BOT_TOKEN = "8334976836:AAGiVMrBg9nq0DlVbc9N2nS4i11zHL9-OFI"
        
        requests.post(
            f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage",
            json={
                "chat_id": chat_id,
                "text": f"You said: {text}"
            },
            timeout=5
        )
    
    # If this is from ERPNext webhook (optional)
    # You can read `data['message']` from ERPNext webhook JSON as well
    
    return "ok"

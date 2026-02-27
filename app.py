from flask import Flask, request, jsonify
import os

app = Flask(__name__)

VERIFICATION_TOKEN = "this_is_my_scraper_token_ebay_pls"

@app.route("/", methods=["GET", "POST"])
def webhook():
    token = request.args.get("verification_token")
    if token == VERIFICATION_TOKEN:
        return VERIFICATION_TOKEN, 200
    return jsonify({"status": "ok"}), 200

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8000))
    # Use threaded=True to prevent Gunicorn sync worker issues
    app.run(host="0.0.0.0", port=port, threaded=True)
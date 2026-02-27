from flask import Flask, request, jsonify

app = Flask(__name__)

VERIFICATION_TOKEN = "this_is_my_scraper_token_ebay_pls"

@app.route("/", methods=["GET", "POST"])
def webhook():
    # eBay GET verification
    token = request.args.get("verification_token")
    if token == VERIFICATION_TOKEN:
        return VERIFICATION_TOKEN, 200  # must return token exactly

    # Normal webhook POST logic
    return jsonify({"status": "ok"}), 200

if __name__ == "__main__":
    import os
    port = int(os.environ.get("PORT", 8000))
    app.run(host="0.0.0.0", port=port)
import hashlib
from flask import Flask, request, jsonify

app = Flask(__name__)

VERIFICATION_TOKEN = "this_is_my_scraper_token_ebay_pls"
ENDPOINT_URL = "https://YOUR-RAILWAY-URL.up.railway.app/ebay-deletion"

@app.route("/ebay-deletion", methods=["GET", "POST"])
def ebay_deletion():
    challenge_code = request.args.get("challenge_code")

    if challenge_code:
        # eBay verification handshake
        combined = challenge_code + VERIFICATION_TOKEN + ENDPOINT_URL
        response_hash = hashlib.sha256(combined.encode()).hexdigest()

        return jsonify({
            "challengeResponse": response_hash
        })

    # Future real notifications
    return jsonify({"status": "ok"}), 200


@app.route("/")
def home():
    return "Webhook is running", 200


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
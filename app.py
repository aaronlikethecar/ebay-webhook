from flask import Flask, request, jsonify
import hashlib

app = Flask(__name__)

import os

VERIFICATION_TOKEN = os.environ.get("VERIFICATION_TOKEN")
ENDPOINT_URL = os.environ.get("ENDPOINT_URL")

@app.route("/", methods=["GET", "POST"])
def webhook():

    challenge_code = request.args.get("challenge_code")

    if challenge_code:
        # Must hash in THIS order:
        # challengeCode + verificationToken + endpoint
        to_hash = challenge_code + VERIFICATION_TOKEN + ENDPOINT_URL
        hashed = hashlib.sha256(to_hash.encode("utf-8")).hexdigest()

        return jsonify({"challengeResponse": hashed}), 200

    return "", 200


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
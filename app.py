from flask import Flask, request, jsonify
import hashlib

app = Flask(__name__)

import os

VERIFICATION_TOKEN = os.environ.get("VERIFICATION_TOKEN")
ENDPOINT_URL = os.environ.get("ENDPOINT_URL")

@app.route("/", methods=["GET", "POST"])
def webhook():

    challenge_code = request.args.get("challenge_code")
    print("CHALLENGE CODE:", challenge_code)
    print("TOKEN:", VERIFICATION_TOKEN)
    print("ENDPOINT:", ENDPOINT_URL)

    if challenge_code:
        to_hash = challenge_code + VERIFICATION_TOKEN + ENDPOINT_URL
        print("STRING TO HASH:", to_hash)
        hashed = hashlib.sha256(to_hash.encode("utf-8")).hexdigest()
        print("HASHED:", hashed)
        return jsonify({"challengeResponse": hashed}), 200

    return "", 200

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
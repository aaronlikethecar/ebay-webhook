from flask import Flask, request, Response

app = Flask(__name__)

VERIFICATION_TOKEN = "this_is_my_scraper_token_ebay_pls"

@app.route("/", methods=["GET", "POST"])
def webhook():
    token = request.args.get("verification_token")
    if token == VERIFICATION_TOKEN:
        # Return plain text explicitly for eBay validation
        return Response(VERIFICATION_TOKEN, status=200, mimetype="text/plain")
    
    # Normal webhook POST logic
    return Response('ok', status=200, mimetype="application/json")
from flask import Flask, request, jsonify
app = Flask(__name__)

@app.route("/")
def home():
    html = "<h1> Prediction Birth Weights: Google Pipelines (Continuous Delivery)</h1><h3> Course MSDS434 Final Project</h3>"
    return html.format(format)

# https://msds434-webapp.uc.r.appspot.com
if __name__ == "__main__":
    app.run(host='localhost', port=8080, debug=True)



from flask import Flask, request, jsonify
app = Flask(__name__)

@app.route("/")
def home():
    html = "<h1> Prediction : Google Pipelines (Continuous Delivery)</h1><h3> Course MSDS434 Final Project: German Credit Data</h3><h2>Insert data query</h2><form><input></form>"
    return html.format(format)

# https://msds434-webapp.uc.r.appspot.com
if __name__ == "__main__":
    app.run(host='localhost', port=8080, debug=True)



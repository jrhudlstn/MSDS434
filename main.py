from flask import Flask, request, jsonify
app = Flask(__name__)

@app.route("/")
def home():
    html = "<h3> Prediction : From Google Pipelines (Continuous Delivery)</h3>"
    return html.format(format)
#!/usr/bin/env python

import webapp2

class MainHandler(webapp2.RequestHandler):
    def get(self):
        self.response.write('I update automatically!')

app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)

if __name__ == "__main__":
    app.run(host='localhost', port=8080, debug=True)
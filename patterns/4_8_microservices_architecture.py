
'''
Definition: Decomposes applications into independent services.
Use case: Scalable cloud applications.

'''

from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/user")
def get_user():
 return jsonify({"id": 1, "name": "John Doe"})




#if __name__ == "__main__":
# app.run(port=5000)

app.run(port=5000)
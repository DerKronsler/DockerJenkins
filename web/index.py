from flask import Flask 
helloworld = Flask(__name__)
@helloworld.route("/")
def run():
    return "{\"message\":\"Hey there python\"}"

if __name__ == "__main__":
    helloworld.run(host="10.7.19.1", port=int("10000"), debug=True)

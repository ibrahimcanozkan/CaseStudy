from flask import Flask, jsonify, request


app = Flask(__name__)

@app.route("/",methods=['GET'])
def get():
    return jsonify({'firstname': 'Ibrahim Can', 'lastname': 'Ozkan'})

@app.route("/whoami",methods=['GET'])
def whoami():
    firstname = request.args.get("firstname")
    lastname = request.args.get("lastname")

    return jsonify({'firstname': firstname, 'lastname': lastname})



if __name__== "__main__":
    app.run(host='0.0.0.0', port=4040)
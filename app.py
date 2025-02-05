from flask import Flask, jsonify, request, make_response


app = Flask(__name__)

businesses = [
    {
    "ID":1,
    "Name":"Ruchira Tex",
    "Location":"Gravesend",
    "Ratings":"5",
    "Reviews":[]
},

 {
    "ID":2,
    "Name":"Ruwani tex",
    "Location":"Farringdon",
    "Ratings":"5",
    "Reviews":[]
},

{
    "ID":3,
    "Name":"Ravindu tex",
    "Location":"London",
    "Ratings":"5",
    "Reviews":[]
}]

@app.route('/', methods=['GET'])
def home():
    return jsonify({"message": "Welcome to COM661"})

@app.route('/businesses', methods=['GET'])
def get_all_businesses():
    return make_response (jsonify({"businesses":businesses }),200)

@app.route("/businesses/raw",methods=['POST'])
def add_business():
    data = request.get_json()
    ID = businesses[-1]["ID"]+1
    new_business = {
        "ID":ID,
        "Name":data["Name"],
        "Location":data["Location"],
        "Ratings":data.get("Ratings",0),
        "Reviews":[]
    }
    businesses.append(new_business)
    return make_response(jsonify(new_business),201) 


#if __name__ == '__main__':
app.run(debug=True)

#python app.py
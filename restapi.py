from flask import Flask ,render_template,request,session,jsonify


#this application repressent web application 
app=Flask(__name__)


#when user open site / or open slash the function below it executes
#decorater
#jsonify display in json format
@app.route("/")
def index():
    T=['hello',3.7,8]
    return jsonify(T)


#when user open site / or open slash the function below it executes
#decorater
@app.route("/david",methods=["GET","POST"])
def david():
    if(request.method=="Post"):
        body=request.get_json()
        return jsonify({"you sent some  ": body}),201
    else:
        return jsonify({"return":"hello"})


#run while server is runing
#curl  http://127.0.0.1:5000/wajaht/ahmed
#it would return json 
@app.route("/<string:name>/<string:name2>")   
def hello(name,name2):
    T=name + name2;
    return jsonify({"name":T})


if __name__ == "__main__":
   app.run(debug = True)


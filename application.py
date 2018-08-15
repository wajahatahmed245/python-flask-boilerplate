from flask import Flask ,render_template,request,session


#this application repressent web application 
app=Flask(__name__)


#when user open site / or open slash the function below it executes
#decorater
@app.route("/")
def index():
     return render_template("test.html")


#when user open site / or open slash the function below it executes
#decorater
@app.route("/david",methods=["POST"])
def david():

    body=request.form.get("box1")
    return render_template("index.html",body=body)



@app.route("/form")
def formF():
   
    return render_template("forms.html")


#when user open site / or open slash the function below it executes
#decorater
#<string:name> what ever you write on url get in variable name and used later 
#f"hello {name}!" forma string
#name=name.capitalize() it will captilize name
@app.route("/<string:name>")
def hello(name):
    name=name.capitalize()
    return f"hello {name}!"



if __name__ == '__main__':
   app.run(debug = True)


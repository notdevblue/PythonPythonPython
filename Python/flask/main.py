from flask import Flask, render_template
app = Flask(__name__)

@app.route("/")
def hello_world():
   return "Hello World!"

@app.route("/home")
def home():
   return '''
   <b><h1>Install Gentoo</h1></b>
   <p> Hello </p>
   <a href="https://www.github.com/notDevblue"> 두둥탁</a>
   '''

@app.route("/gentoo")
def gentoo():
   return "You did it"

@app.route("/user/<user_name>/<int:user_id>")
def user(user_name, user_id):
   return f'<h1>Hello, {user_name}({user_id})!</h1>'

@app.route("/render_template/<int:number>")
def index(number):
   return render_template("index.html", template_name="name");

if __name__ == "__main__":
   app.run(debug=True)

import threading
import time;

from flask import Flask, render_template
app = Flask(__name__);

@app.route("/")
def hello_world():
   return "Hello World!"
#end def hello_world();

@app.route("/home")
def home():
   return '''
   <b><h1>Install Gentoo</h1></b>
   <p> Hello </p>
   <a href="https://www.github.com/notDevblue"> 두둥탁</a>
   '''
#end def home();

@app.route("/gentoo")
def gentoo():
   return render_template("gentoo.html");
#end def gentoo();

@app.route("/user/<user_name>/<int:user_id>")
def user(user_name, user_id):
   return f'<h1>Hello, {user_name}({user_id})!</h1>'
#end def user(user_name, user_id);

@app.route("/render_template/<int:number>")
def index(number):
   return render_template("index.html", template_name="name");
#end def index(number);

# @app.context_processor
# def keep_change_h_tag():
#    htag = 1;
#    while True:
#       time.sleep(1.0);
#       htag = (htag + 1) % 10 + 1;
#       return(f"<h{htag}>인스톨 젠투</h{htag}>");


if __name__ == "__main__":
   app.run(debug=True)

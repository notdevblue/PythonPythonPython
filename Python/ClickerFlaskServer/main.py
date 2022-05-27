from flask import Flask;
import pymysql;
from savescore import savescore;
from getscore import getscore;

app = Flask(__name__);
conn = pymysql.connect(host="localhost",
                       user="han",
                       password="0225",
                       db="pypypy",
                       charset="utf8");
cur = conn.cursor();


@app.route("/save", methods=["POST"])
def save():
   return savescore(cur, conn);

@app.route("/get", methods=["POST"])
def get():
   return getscore(cur, conn);


# @app.route("/test")
# def test():
#    # return savescore(cur, conn);
#    return getscore(cur, conn);


if __name__ == "__main__":
   app.run(host="0.0.0.0", port=48000, debug=True);

from flask import request;

def savescore(cur, conn):
   score = "";
   name = "";
   try:
      score = request.form["score"];
      name = request.form["name"];
   except:
      return "#ERROR#;";

   sql = "SELECT id FROM pypypy.Clicker WHERE name=%s";
   vals = (name,);
   cur.execute(sql, vals);
   row = cur.fetchone();

   if (row == None):
      sql = "INSERT INTO pypypy.Clicker (`name`, `score`) VALUES(%s, %s);";
      vals = (name, score,);
      cur.execute(sql, vals);
      conn.commit();
      return "ADDED";

   else:
      sql = "UPDATE pypypy.Clicker SET `score`=%s WHERE `id`=%s";
      vals = (score, row[0]);
      cur.execute(sql, vals);
      conn.commit();
      return "UPDATED"
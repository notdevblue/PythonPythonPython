from flask import request;

def getscore(cur, conn):
   range = "";
   try:
      range = request.form["range"];
      str_list = [];
   except:
      return "#ERROR#;";

   sql = "SELECT `name`, `score` FROM `Clicker` WHERE 1 ORDER BY `score` DESC";
   if (range > 0):
      sql += "LIMIT 0, %s";
   
   vals = (range,);
   cur.execute(sql, vals);
   row = cur.fetchall();

   if (row == None):
      return "#ERROR#;";
   
   
   for item in row:
      str_list.append(f"#RESULT#$NAME={item[0]}$SCORE={item[1]};");

   return ''.join(str_list);

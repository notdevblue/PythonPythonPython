from flask import request;

def getscore(cur, conn):
   range = "";
   name = "";
   try:
      range = request.form["range"];
      name = request.form["name"];
      str_list = [];
   except Exception as e:
      return f"#ERROR#; {e}";

   sql = "SELECT `name`, `score` FROM `Clicker` ";

   if (name != ""):
      sql += "WHERE name=%s";
      cur.execute(sql, [name]);

   else:
      sql += "WHERE 1 ORDER BY `score` DESC ";
      if (int(range) > 0):
         sql += "LIMIT 0, %s";
      #endif
      cur.execute(sql, int(range));
   #endelse

   row = cur.fetchall();

   if (row == None):
      return "#ERROR#;";
   
   if name != "":
      str_list.append(f"#MYSCORE#$NAME={row[0][0]}$SCORE={row[0][1]}&;");
   else:
      str_list.append("#SCOREDATA#");
      idx = 0;
      for item in row:
         # print(f"#SCOREDATA#$NAME={item[0]}$SCORE={item[1]}&;");
         str_list.append(f"$NAME{idx}={item[0]}$SCORE{idx}={item[1]}");
         idx += 1;
      str_list.append("&;");

   return ''.join(str_list);

# Python / Flask / Unity 3D 통한 클리커 게임

<image src="https://cdn.discordapp.com/attachments/888797035468308550/979765216772497408/Clicker.gif"/>

* * *

### 5.15.41-gentoo-x86_64 를 사용해 Python 3.9.12 로 작성된 코드입니다.

* * *

## 폴더 구조 (서버)
ROOT
* getscore.py
* main.py
* savescore.py
<br/><br/>

## 폴더 구조 (클라이언트)
Assets
* Scripts
   * Handlers
      * OnPacketEvent.cs
      * ScoreHandler.cs
   * UI
      * Clicker.cs
      * ScoreRenderer.cs
   * GameManager.cs
   * MonoSingleton.cs
   * PacketHandler.cs
   * PacketManager.cs
   * RequestSender.cs

* * * 

## 분석

### 서버 <br/>

#### 페킷 정의

```
#타입#
$변수명

= <= 뒤와 앞을 변수명과 값으로 구분함
& <= 구조체의 끝
; <= 페킷의 끝

예시:
   #TYPE#$A=wa sans$B=ori;#TYPE#$A=I'm ori$B=jemmun&;
   #LOGIN#$id=id$pw=pw&;
   #SCORE#$id=id$score=score&;
```

```
+ conn : DB 와의 연결
+ cur  : 커셔 (conn.cursor())

```

<details>
   <summary>getscore.py</summary>

```py
sql = "SELECT `name`, `score` FROM `Clicker` ";

# 이름이 있는 요청 (개인 데이터 요청))
if (name != ""):
   sql += "WHERE name=%s";
   cur.execute(sql, [name]);

else: # 이름이 없는 요청 (리더보드 요청)
   sql += "WHERE 1 ORDER BY `score` DESC ";
   if (int(range) > 0):
      sql += "LIMIT 0, %s";
   #endif

   cur.execute(sql, int(range));
```
SQL 쿼리 로직<br/><br/>

```py
if name != "": # 개인 데이터 하나만 보내는 경우
   str_list.append(f"#MYSCORE#$NAME={row[0][0]}$SCORE={row[0][1]}&;");

else: # 리더보드 보내는 경우
   str_list.append("#SCOREDATA#");
   idx = 0;

   for item in row: #변수명 구분을 위해 인덱스를 추가
      str_list.append(f"$NAME{idx}={item[0]}$SCORE{idx}={item[1]}");
      idx += 1;
   #endfor

   str_list.append("&;"); #페킷 끝을 나타냄
```
페킷 생성 로직<br/><br/>

</details>

<details>
   <summary>savescore.py</summary>

```py
sql = "SELECT id FROM pypypy.Clicker WHERE name=%s";
vals = (name,);
cur.execute(sql, vals);
row = cur.fetchone();
```
SQL 쿼리 로직<br/><br/>

```py
if (row == None): # 기존 데이터가 없음
   sql = "INSERT INTO pypypy.Clicker (`name`, `score`) VALUES(%s, %s);";
   vals = (name, score,);
   cur.execute(sql, vals);
   conn.commit();
   return "#MESSAGE#$MSG=Added;";

else: # 기존 데이터가 있음
   sql = "UPDATE pypypy.Clicker SET `score`=%s WHERE `id`=%s";
   vals = (score, row[0]);
   cur.execute(sql, vals);
   conn.commit();
   return "#MESSAGE#$MSG=Updated;"
```
기존 데이터 유무에 따른 데이터 처리 로직<br/><br/>

</details>

<details>
   <summary>main.py</summary>

```py
from flask import Flask;
import pymysql;

# 저장과 불러오기 기능을 담은 모듈 import
from savescore import savescore;
from getscore import getscore;

...

@app.route("/save", methods=["POST"])
def save():
   return savescore(cur, conn);

@app.route("/get", methods=["POST"])
def get():
   return getscore(cur, conn);
```
Flask 를 사용한 라우팅<br/><br/>

</details>

* * *


### 클라이언트 <br/>

<details>
   <summary>UUID</summary>

```cs
string path = Application.persistentDataPath + "/uuid";

if (!File.Exists(path))
{ // UUID 가 없는 경우
   System.Guid guid = System.Guid.NewGuid();
   uuid = guid.ToString();
   File.WriteAllText(path, uuid);
}
else
{ // UUID 가 있는 경우
   uuid = File.ReadAllText(path);
}

Debug.Log(uuid);
```
UUID 저장 및 생성<br/><br/>

</details>

<details>
   <summary>페킷 파싱</summary>

```cs
public void ParsePacket(string data)
{
   string[] datas = data.Split(TERMINATOR);

   for (int i = 0; i < datas.Length - 1; ++i)
   {
      if (datas[i][0] == TYPE)
      {
         /// 타입
         // # 의 끝 인덱스를 찾음
         int typeEndIdx = datas[i].IndexOf(TYPE, 1);

         if (typeEndIdx <= 0) throw _invalidPacketException;

         string type = datas[i].Substring(1, typeEndIdx - 1);

         if (datas[i].Length <= typeEndIdx + 1)
         { // 타입만 가진 페킷인 경우
            OnHandlePacket(type, (null, null));
            return;
         } 

         /// 멤버 그룹

         // 잘못된 페킷 검증
         if (datas[i][typeEndIdx + 1] != MEMBER) throw _invalidPacketException;

         int memberStartIdx = typeEndIdx + 1;

         // & (멤버)의 끝을 찾음
         int memberEndIdx = datas[i].IndexOf(ENDOFMEMBER, memberStartIdx + 1);

         if (memberEndIdx <= memberStartIdx) throw _invalidPacketException;

         string member = datas[i].Substring(memberStartIdx + 1, memberEndIdx - memberStartIdx - 1);

         // 파싱이 완료된 페킷을 전달함
         OnHandlePacket(type, ParseMember(member));
      }
      else
      {
         throw _invalidPacketException;
      }
   }
}

private (List<string>, List<string>) ParseMember(string data)
{
   // 변수 단위로 나눔
   string[] members   = data.Split(MEMBER);

   string[] temp      = new string[2];
   List<string> name  = new List<string>();
   List<string> value = new List<string>();

   for (int i = 0; i < members.Length; ++i)
   {
      // = 를 기준으로 변수명과 값을 나눔
      temp = members[i].Split(VALUE);
      name.Add(temp[0]);
      value.Add(temp[1]);
   }

   return (name, value);
}
```

</details>

<details>
   <summary>페킷 헨들링</summary>

```cs
public void Handle(string type, (List<string>, List<string>) members)
{   
   // 헨들링 될 수 있는 타입인지 검증
   if(!_packetHandlerDictionary.ContainsKey(type))
      throw _keyNotFoundException;

   // 헨들러 Dictionary 로 넘김
   _packetHandlerDictionary[type](members);
}

public void AddHandler(string type, Action<(List<string>, List<string>)> callback)
{
   if (_packetHandlerDictionary.ContainsKey(type))
      _packetHandlerDictionary[type] += callback;
   else
      _packetHandlerDictionary.Add(type, callback);
}
```
</details>


<details>
   <summary>페킷 헨들러 예시</summary>

```cs
PacketHandler.Instance.AddHandler("페킷 타입", members => {
   // 페킷 멤버의 대한 처리
});
```

</details>


<h1>Python / Websocket 통한 Echo 서버</h1>

<image src="https://cdn.discordapp.com/attachments/888797035468308550/979181173840441364/Python_Echo_server.gif"/>

* * *

### 5.15.41-gentoo-x86_64 를 사용해 Python 3.9.12 로 작성된 코드입니다.
#### Python 배운 첫날에 작성한 서버라 부족한 점이 있을 수 있어요.

* * *

## 폴더 구조
ROOT
- handlers
   * echo.py
   * test.py
* client.py
* server.py


* * * 


## 분석

### 서버<br/>

<details>
   <summary>Packet Handler</summary>

```py
# 동적 헨들러 import
for (dirpath, dirnames, filenames) in walk("./handlers"):
   for name in filenames:
      
      filename = Path(name).stem;
      module = __import__(filename);

      handlers[filename] = getattr(module, filename);
      print(f"Loaded {name}");
   break;
```
handlers 폴더 안 모든 handler 를 import 한 뒤,<br/>
handlers Dictionary 에 확장자 없는 파일 이름 (페킷 타입) 으로 추가함.<br/><br/>
</details>

<details>
   <summary>Handler 구조</summary>

```py
import json

# example echo handler
class echo:
   async def handle(ws, data):
      await ws.GLOBAL.broadcast(json.dumps({
         # 페킷 타입
         "type": "echo",

         # payload
         "payload": data
      }));
```
모든 헨들러는 파일 이름과 동일한 클레스를 가지고, <br/>
handle(ws, data); 라는 공통적인 함수를 가지며, <br/>
파일 이름과 동일한 타입의 페킷을 Json 형식으로 처리함. <br/><br/>
</details>

<details>
   <summary>on connect</summary>

```py
# uuid
global clientId;
clientId += 1;

# Dictionary 추가
clients[clientId] = ws;
ws.clientId = clientId;

# global 오브젝트 할당
ws.GLOBAL = gObject;

# log
print(f"Client {ws.clientId} connected.");
await ws.send("Hello");
```
새 클라이언트가 접속 시 uuid 를 할당하고, <br/>
clients dictionary 에 추가한 뒤, <br/>
global 오브젝트를 할당함. <br/><br/>

</details>

<details>
   <summary>on recv</summary>

```py
# json 변환
data = json.loads(message);

# 받은 데이터의 페킷 타입에 대한 헨들러가 있는지
if (data["type"] in handlers):
   await handlers[data["type"]].handle(ws, data["payload"]);
else:
   print(f"Type {data['type']} is not defined");
```
받은 페킷을 Json 형식에서 변환한 뒤, <br/>
페킷의 타입에 대한 헨들러가 있다면 페킷의 payload 를 넘김. <br/><br/>

</details>

<details>
   <summary>GLOBAL</summary>

```py
class GLOBAL:
   @staticmethod
   async def broadcast(data):
      try:
         for ws in clients.copy().values():
            await ws.send(data);

      # 연결이 끊긴 클라이언트 처리
      except websockets.exceptions.ConnectionClosed:
         print(f"Client {ws.clientId} disconencted");

         # clients dictionary 에서 제거
         clients.pop(ws.clientId);
         pass;
```
broadcast 기능을 가지고 있는 클레스. <br/>

</details>

* * *

### 클라이언트<br/>

<details>
   <summary>send thread</summary>

```py
while True:
   # 사용자 입력
   data = str(input());

   # Json 형식으로 send
   ws.send(json.dumps({
      "type": "echo",
      "payload": data
   }));
```
유저의 입력을 저장한 뒤 Json 형식의 페킷으로 보냄 <br/><br/>

</details>

<details>
   <summary>recv thread</summary>

```py
while True:
   # 받은 message 를 출력함
   print("\r\nMessage: " + ws.recv());
```

</details>
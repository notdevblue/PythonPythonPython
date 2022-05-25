import json;
import threading;
from websocket import create_connection;

ws = create_connection("ws://localhost:38000");

def send(ws):
   while True:
      data = str(input());
      ws.send(json.dumps({
         "type": "echo",
         "payload": data
      }));
# end def send(ws);

def recv(ws):
   while True:
      print("\r\nMessage: " + ws.recv());
# end def recv(ws);

send_thread = threading.Thread(target=send, args=(ws,));
recv_thread = threading.Thread(target=recv, args=(ws,));

send_thread.start();
recv_thread.start();


send_thread.join();
recv_thread.join();

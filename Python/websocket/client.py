import json
import time;
import websocket

def on_message(ws, message):
   print(message);

def on_error(ws, error):
   print(error);

def on_open(ws):
   print("Opened Connection");
   while True:
      buffer = str(input("Message: "));
      ws.send(json.dumps({
         "type": "echo",
         "payload": buffer
      }));


if __name__ == "__main__":
   # websocket.enableTrace(True);
   ws = websocket.WebSocketApp("ws://localhost:38000",
                               on_message=on_message,
                               on_open=on_open,
                               on_error=on_error);
   ws.run_forever();

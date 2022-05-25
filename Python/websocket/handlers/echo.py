import json

class echo:
   async def handle(ws, data):
      await ws.GLOBAL.broadcast(json.dumps({
         "type": "echo",
         "payload": data
      }));  
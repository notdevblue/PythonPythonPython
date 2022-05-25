import asyncio
from asyncore import dispatcher;
import websockets;
import json; # packet

from sys import path; # path
path.insert(1, "./handlers");

from os import walk; # to get all the handlers
from pathlib import Path; # stem

clients  = {};
clientId = 0;
handlers = {};
port = 38000;

# dynamic handler importing
for (dirpath, dirnames, filenames) in walk("./handlers"):
   for name in filenames:
      
      filename = Path(name).stem;
      module = __import__(filename);

      handlers[filename] = getattr(module, filename);
      print(f"Loaded {name}");
   break;
#end for

print(f"Server started on port {port}.");

class GLOBAL:
   @staticmethod
   async def broadcast(data):
      try:
         for ws in clients.copy().values():
            await ws.send(data);
      except websockets.exceptions.ConnectionClosed:
         print(f"Client {ws.clientId} disconencted");
         clients.pop(ws.clientId);
         pass;
   #end async def broadcast(data);
#end class GLOBAL;

gObject = GLOBAL();

async def on(ws):
   global clientId;
   clientId += 1;

   clients[clientId] = ws;
   ws.clientId = clientId;
   ws.GLOBAL = gObject;
   
   print(f"Client {ws.clientId} connected.");
   await ws.send("Hello");

   async for message in ws:
      try:
         data = json.loads(message);

         if (data["type"] in handlers):
            await handlers[data["type"]].handle(ws, data["payload"]);
         else:
            print(f"Type {data['type']} is not defined");

      except websockets.exceptions.ConnectionClosed:
         print(f"Client {ws.clientId} disconencted");
         clients.pop(ws.clientId);
   pass;
#end def on(ws);

async def main():
   async with websockets.serve(on, "localhost", port):
      await asyncio.Future(); # run forever
   pass;
#end def main();

if __name__ == "__main__":
   asyncio.run(main());
#end if
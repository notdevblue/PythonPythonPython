import asyncio
import threading;
import websocket;
import json; # packet

send_thread = 0;
recv_thread = 0;
main_thread = 0;
ws = 0;
lock = threading.Lock();

# async def on():
#    global send_thread;
#    global recv_thread;
#    global ws;

#    ws = await websockets.connect("ws://localhost:38000");
#    # with websockets.connect("ws://localhost:38000") as ws:
   

#    send_thread = threading.Thread(target=asyncio.run, args=(send(),));
#    recv_thread = threading.Thread(target=asyncio.run, args=(recv(),));

#    send_thread.start();
#    # recv_thread.start();

#    send_thread.join();
#    # recv_thread.join();

# # def send_caller():
# #    loop = asyncio.new_event_loop();
# #    asyncio.set_event_loop(loop);
# #    loop.run_until_complete(send());

# #    loop.close();
# #    pass;

# # def recv_caller():
# #    loop = asyncio.new_event_loop();
# #    asyncio.set_event_loop(loop);
# #    loop.run_until_complete(recv());

# #    loop.close();
# #    pass;

# async def send():
#    while True:
#       data = str(input("Input: "));

#       lock.acquire();
#       await ws.send(json.dumps({
#          "type": "echo",
#          "payload": data
#       }));
#       lock.release();
#    #end while True;
# #end dev send(ws);

# async def recv():
#    while True:
#       lock.acquire();
#       print(await ws.recv());
#       lock.release();
#    #end while True;
# #end def recv(ws);

# if __name__ == "__main__":
#    asyncio.run(on());
# #end if


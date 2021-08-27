# Copyright (c) 2021 Johnathan P. Irvin
# 
# Permission is hereby granted, free of charge, to any person obtaining
# a copy of this software and associated documentation files (the
# "Software"), to deal in the Software without restriction, including
# without limitation the rights to use, copy, modify, merge, publish,
# distribute, sublicense, and/or sell copies of the Software, and to
# permit persons to whom the Software is furnished to do so, subject to
# the following conditions:
# 
# The above copyright notice and this permission notice shall be
# included in all copies or substantial portions of the Software.
# 
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
# EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
# MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND
# NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE
# LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION
# OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION
# WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
from fastapi import FastAPI, WebSocket, WebSocketDisconnect
from viking.connections import ConnectionManager
from viking.events import EventBus, subscribe
from viking.messaging import MessageReceivedEvent, TextChannel
from viking.minecraft.computers import Computer
from viking.minecraft.events.programs import ProgramExecutedEvent
from websockets.exceptions import ConnectionClosed

app = FastAPI()
bus = EventBus()
manager = ConnectionManager(bus)
channel = TextChannel(bus)

@subscribe(ProgramExecutedEvent, bus)
async def handle_program_executed(event: ProgramExecutedEvent):
    await channel.send(event.output)

@subscribe(MessageReceivedEvent, bus)
async def broadcast(event: MessageReceivedEvent):
    for socket in await manager.get_connections():
        try:
            await socket.send_text(event.message.value)
        except WebSocketDisconnect:
            await manager.disconnect(socket)
        except ConnectionClosed:
            await manager.disconnect(socket)

@app.websocket("/ws/{client_id}")
async def websocket_endpoint(websocket: WebSocket, client_id: str):
    await manager.connect(websocket)
    computer = Computer(websocket, bus)
    try:
        while True:
            message = await websocket.receive_text()
            await channel.send(message)

            if message.lower().startswith('run '):
                message = message[4:]
                await computer.run_program(message)

    except WebSocketDisconnect:
        await manager.disconnect(websocket)

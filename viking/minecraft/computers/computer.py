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
from viking.connections.interfaces import AbstractSocket
from viking.events.interfaces import AbstractEventBus

from ..events import ProgramExecutedEvent
from ..interfaces import AbstractComputer


class Computer(AbstractComputer):
    def __init__(self, socket: AbstractSocket, event_bus: AbstractEventBus):
        """
        The computer connection over a socket.

        Args:
            socket (AbstractSocket): The socket to use to communicate with the computer.
            event_bus (AbstractEventBus): The event bus for internal events.
        """
        self._socket = socket
        self._event_bus = event_bus
    
    async def run_program(self, program: str) -> str:
        await self._socket.send_text(program)
        received = await self._socket.receive_text()
        await self._event_bus.publish(ProgramExecutedEvent(self, program, received))
        return received

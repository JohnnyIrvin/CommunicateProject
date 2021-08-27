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
from typing import List

from starlette.types import Message

from ..interfaces import AbstractSocket


class FakeSocket(AbstractSocket):
    """A fake socket implementation that is used to test the socket"""

    def __init__(self, messages: List[Message] = []) -> None:
        """
        Args:
            messages (list): A list of fake messages to initialize with.
        """
        self._messages: List[Message] = messages
        self.closed = True

    async def send(self, message: Message) -> None:
        """
        Send data to the socket.

        Args:
            message (Message): The message to send.
        """
        self._messages   
        return

    async def receive(self) -> Message:
        """
        Receive data from the socket.

        Returns:
            Message: The message received.
        """
        return self._messages[-1]

    async def accept(self) -> None:
        """
        Accept a connection.
        """
        self.closed = False
        return

    def close(self) -> None:
        """
        Close the socket.
        """
        self.closed = True
        return

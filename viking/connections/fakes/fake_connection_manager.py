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

from ..interfaces import AbstractConnectionManager, AbstractSocket


class FakeConnectionManager(AbstractConnectionManager):
    def __init__(self) -> None:
        """
        Initialize the connection manager.
        """
        self._connections: List[AbstractSocket] = []

    async def connect(self, socket: AbstractSocket) -> None:
        """
        Connect a socket to the manager.

        Args:
            socket (AbstractSocket): The socket to connect.
        """        
        self._connections.append(socket)

    async def disconnect(self, socket: AbstractSocket) -> None:
        """
        Disconnect a socket from the manager.

        Args:
            socket (AbstractSocket): The socket to disconnect.
        """        
        self._connections.remove(socket)

    async def get_connections(self) -> List[AbstractSocket]:
        """
        Return a list of all socket connected to the manager.

        Returns:
            List[AbstractSocket]: A list of all socket connected to the manager.
        """        
        return self._connections

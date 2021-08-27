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
from typing import Generator, List, Union

from viking.events import AbstractEventBus

from ..events import MessageReceivedEvent
from ..interfaces import AbstractChannel
from ..values import Message


class TextChannel(AbstractChannel):
    def __init__(self, event_bus: AbstractEventBus) -> None:
        self._history: List[Message] = []
        self._event_bus = event_bus
    
    async def send(self, message: Union[Message, str]) -> None:
        if isinstance(message, str):
            message = Message(message)
        self._history.append(message)
        await self._event_bus.publish(MessageReceivedEvent(message))

    def history(self) -> Generator[Message, None, None]:
        for msg in self._history:
            yield msg

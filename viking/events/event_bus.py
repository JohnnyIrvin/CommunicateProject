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
from inspect import isawaitable
from typing import Coroutine, Type, Union

from .interfaces import AbstractEvent, AbstractEventBus


class EventBus(AbstractEventBus):
    def __init__(self):
        """
        Initialize the event bus.
        """
        self._subscribers = {}

    def subscribe(self, event_type: Type[AbstractEvent], callback: Union[callable, Coroutine]) -> None:
        """
        Subscribe to an event.

        Args:
            event_type (Type[AbstractEvent]): The event type.
            callback (callable): The callback.
        """
        subscribers = self._subscribers.get(event_type, [])
        subscribers.append(callback)
        self._subscribers[event_type] = subscribers

    def unsubscribe(self, event_type: Type[AbstractEvent], callback: Union[callable, Coroutine]) -> None:
        """
        Unsubscribe from an event.

        Args:
            event_type (Type[AbstractEvent]): The event type.
            callback (callable): The callback.
        """
        subscribers = self._subscribers.get(event_type, [])
        subscribers.remove(callback)
        self._subscribers[event_type] = subscribers

    async def publish(self, event: AbstractEvent) -> None:
        """
        Publish an event.

        Args:
            event (AbstractEvent): The event.
        """
        for subscriber in self._subscribers.get(type(event), []):
            func = subscriber(event)
            if isawaitable(func):
                await func

    def get_subscribers(self, event_type: Type[AbstractEvent]) -> list:
        """
        Get all subscribers for an event.

        Args:
            event_type (Type[AbstractEvent]): The event type.
        """
        return self._subscribers.get(event_type, [])

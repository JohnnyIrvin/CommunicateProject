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

import pytest
from viking.events.interfaces import AbstractEvent, AbstractEventBus


@pytest.mark.asyncio
async def test_subscribe_new_event(bus: AbstractEventBus, event: AbstractEvent):
    """
    Subscribe to a new event.

    Args:
        bus (AbstractEventBus): The bus to subscribe to.
        event (AbstractEvent): The event to subscribe to.
    """    
    # Arrange
    success = False
    def create_success(event: AbstractEvent):
        nonlocal success
        success = True

    bus.subscribe(type(event), create_success)

    # Act
    await bus.publish(event)

    # Assert
    assert success

@pytest.mark.asyncio
async def test_unsubscribe_from_event(bus: AbstractEventBus, event: AbstractEvent):
    """
    Unsubscribe from an event.

    Args:
        bus (AbstractEventBus): The bus to subscribe to.
        event (AbstractEvent): The event to subscribe to.
    """
    # Arrange
    success = False
    def create_success(event: AbstractEvent):
        nonlocal success
        success = True

    bus.subscribe(type(event), create_success)
    bus.unsubscribe(type(event), create_success)

    # Act
    await bus.publish(event)

    # Assert
    assert not success  

def test_has_subscriber(bus: AbstractEventBus, event: AbstractEvent):
    """
    Test if an event has a subscriber.

    Args:
        bus (AbstractEventBus): The bus to subscribe to.
        event (AbstractEvent): The event to subscribe to.
    """
    # Arrange
    success = False
    def create_success(event: AbstractEvent):
        nonlocal success
        success = True

    bus.subscribe(type(event), create_success)

    # Act
    subscribers: List[callable] = bus.get_subscribers(type(event))

    # Assert
    assert subscribers == [create_success]

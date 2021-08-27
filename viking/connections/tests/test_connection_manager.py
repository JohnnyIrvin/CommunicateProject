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
import pytest
from viking.connections.fakes import FakeSocket


@pytest.mark.asyncio
async def test_connection_manager_has_no_connections(connection_manager):
    # Act
    connections = await connection_manager.get_connections()

    # Assert
    assert len(connections) == 0

@pytest.mark.asyncio
async def test_new_connection_is_added_to_manager(connection_manager):
    # Arrange
    fake_socket = FakeSocket()

    # Act
    await connection_manager.connect(fake_socket)
    connections = await connection_manager.get_connections()

    # Assert
    assert len(connections) == 1
    assert connections[0] == fake_socket

@pytest.mark.asyncio
async def test_multiple_new_connections_are_added_to_manager(connection_manager):
    # Arrange
    fake_socket1 = FakeSocket()
    fake_socket2 = FakeSocket()

    # Act
    await connection_manager.connect(fake_socket1)
    await connection_manager.connect(fake_socket2)
    connections = await connection_manager.get_connections()

    # Assert
    assert len(connections) == 2
    assert connections == [fake_socket1, fake_socket2]

@pytest.mark.asyncio
async def test_connect_disconnect_connection(connection_manager):
    # Arrange
    fake_socket = FakeSocket()

    # Act
    await connection_manager.connect(fake_socket)
    await connection_manager.disconnect(fake_socket)
    connections = await connection_manager.get_connections()

    # Assert
    assert len(connections) == 0

@pytest.mark.asyncio
async def test_connect_disconnect_multiple_connections(connection_manager):
    # Arrange
    fake_socket1 = FakeSocket()
    fake_socket2 = FakeSocket()

    # Act
    await connection_manager.connect(fake_socket1)
    await connection_manager.connect(fake_socket2)
    await connection_manager.disconnect(fake_socket1)
    await connection_manager.disconnect(fake_socket2)
    connections = await connection_manager.get_connections()

    # Assert
    assert len(connections) == 0

@pytest.mark.asyncio
async def test_add_two_remove_first_connection(connection_manager):
    # Arrange
    fake_socket1 = FakeSocket()
    fake_socket2 = FakeSocket()

    # Act
    await connection_manager.connect(fake_socket1)
    await connection_manager.connect(fake_socket2)
    await connection_manager.disconnect(fake_socket1)
    connections = await connection_manager.get_connections()

    # Assert
    assert len(connections) == 1
    assert connections[0] == fake_socket2
    assert connections == [fake_socket2]

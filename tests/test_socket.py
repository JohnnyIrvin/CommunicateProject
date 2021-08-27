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

def test_websocket_communication_with_text(client):
    """
    Test that we can connect to a websocket
    
    Args:
        client (TestClient): 
    """
    # Arrange
    with client.websocket_connect("/ws/test_1") as websocket:

        # Act
        websocket.send_text("Hello")
        
        # Assert
        assert 'Hello' in websocket.receive_text()

def test_two_websocket_first_communication(client):
    """
    Test that we can connect to two websockets
    
    Args:
        client (TestClient): 
    """
    # Arrange
    with client.websocket_connect("/ws/test_1") as websocket1:
        with client.websocket_connect("/ws/test_2") as websocket2:

            # Act
            websocket1.send_text("Hello")
            
            # Assert
            assert 'Hello' in websocket2.receive_text()

def test_two_websockets_second_communication(client):
    """
    Test that we can connect to two websockets
    
    Args:
        client (TestClient): 
    """
    # Arrange
    with client.websocket_connect("/ws/test_1") as websocket1:
        with client.websocket_connect("/ws/test_2") as websocket2:

            # Act
            websocket2.send_text("Hello")

            # Assert
            assert 'Hello' in websocket1.receive_text()

def test_ten_messages_in_a_row(client):
    """
    Test that we can send 10 messages in a row
    
    Args:
        client (TestClient): 
    """
    # Arrange
    with client.websocket_connect("/ws/test_1") as websocket:
        for i in range(10):
            websocket.send_text(f"Hello {i}")

            # Assert
            assert f'Hello {i}' in websocket.receive_text()

def test_ten_messages_read_by_another_socket(client):
    """
    Test that we can send 10 messages in a row
    
    Args:
        client (TestClient): 
    """
    # Arrange
    with client.websocket_connect("/ws/test_1") as websocket2:
        with client.websocket_connect("/ws/test_2") as websocket1:
            for i in range(10):
                websocket1.send_text(f"Hello {i}")

                # Assert
                assert f'Hello {i}' in websocket2.receive_text()
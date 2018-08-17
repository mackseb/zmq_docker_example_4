import zmq
import os

context = zmq.Context()
address = os.environ['ADDRESS']
print(address)
#  Socket to talk to server
socket = context.socket(zmq.SUB)
socket.connect(address)
socket.setsockopt_string(zmq.SUBSCRIBE, '')

#  Do 10 requests, waiting each time for a response
for _ in range(1000):
    print("sub received: " + socket.recv_string())
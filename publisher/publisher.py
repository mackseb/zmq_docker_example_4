import time
import zmq

context = zmq.Context()
socket = context.socket(zmq.PUB)
socket.bind("tcp://0.0.0.0:5555")
print("server started")

for i in range(2000):
       socket.send_string("Hello"+str(i))
       time.sleep(1)
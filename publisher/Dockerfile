FROM python:3.6

RUN pip install zmq

COPY . .

EXPOSE 5555

CMD [ "python", "publisher.py"]
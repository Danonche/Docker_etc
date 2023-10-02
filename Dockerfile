FROM python:3

WORKDIR /app

COPY . .

RUN pip3 install numpy

CMD [ "python", "your-daemon-or-script.py" ]
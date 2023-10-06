FROM python:3.11-slim-bullseye

WORKDIR /app

COPY your-daemon-or-script.py .

RUN pip3 install numpy

CMD [ "python", "your-daemon-or-script.py" ]
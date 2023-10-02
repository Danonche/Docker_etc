FROM python:3

WORKDIR /app

COPY . .

CMD [ "python", "your-daemon-or-script.py" ]
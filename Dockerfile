FROM python:3

WORKDIR /app

COPY requirements.txt /app/
RUN pip3 install -r /app/requirements.txt

COPY bot.py /app/
COPY bot.properties /app/

ENTRYPOINT [ "python3", "./bot.py" ]

FROM python:3.8.4-slim-buster
WORKDIR /opt/testapp
COPY . .
RUN apt update
RUN apt install libcurl4-openssl-dev libssl-dev gcc -y
RUN pip install --no-cache-dir -r requirements.txt
CMD [ "python", "tester.py" ]
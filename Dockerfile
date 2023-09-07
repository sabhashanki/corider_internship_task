FROM python:slim-bookworm
COPY . /app
WORKDIR /app
RUN apt update && apt install -y curl
RUN pip3 install -r requirements.txt
EXPOSE 5000
CMD ["flask", "--app", "app.py", "run"]
FROM python:3.10-alpine

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /opt/pacer-app
COPY pacer-app .

RUN pip3 install --upgrade pip && \
    pip3 install --no-cache-dir -r requirements.txt

EXPOSE 8000

ENTRYPOINT ["/bin/sh", "entrypoint.sh"]

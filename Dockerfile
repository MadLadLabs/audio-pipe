FROM python:3.7

RUN apt-get update && apt-get install -y \
    python3 \
    python3-pip \
    libsox-fmt-all \
    sox

RUN pip3 install \
    pyyaml \
    sox

COPY /src /app

WORKDIR /app

CMD python3 app.py
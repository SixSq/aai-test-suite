FROM python:3-slim

WORKDIR /opt

COPY * .

RUN pip install -r requirements.txt

RUN python -m playwright install firefox

RUN apt update && \
    apt install -y \
      libx11-dev \
      libglib2.0-dev \
      libgtk-3-dev \
      libxt-dev \
      libdbus-glib-1-dev && \
    rm -rf /var/lib/apt/lists/*

ENTRYPOINT ["./sixsq-nuvla.py"]
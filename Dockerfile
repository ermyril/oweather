FROM ubuntu:22.04

RUN apt-get update && \
    apt-get install -y --no-install-recommends \
    texlive-base
RUN apt-get install -y --no-install-recommends \
    pandoc
RUN apt-get install -y --no-install-recommends \
    gawk
RUN apt-get install -y --no-install-recommends \
    python3 \
    python3-aiohttp \
    && rm -rf /var/lib/apt/lists/*

COPY ./src/main.py /app/
COPY ./src/entrypoint.sh /app/

RUN chmod +x /app/entrypoint.sh
RUN mkdir /output

WORKDIR /app
ENTRYPOINT ["/app/entrypoint.sh"]

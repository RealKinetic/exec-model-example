FROM alpine:3.9 as base

RUN apk add python3

FROM base as builder

RUN apk add build-base python3-dev libffi-dev openssl-dev

RUN mkdir /install
WORKDIR /install

COPY requirements.txt /requirements.txt

RUN pip3 install --install-option="--prefix=/install" -r /requirements.txt

FROM base

RUN apk add libffi openssl

COPY --from=builder /install /usr
COPY src /app

WORKDIR /app

CMD ["python3", "./main.py"]

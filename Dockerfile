FROM python:3-alpine

WORKDIR /app

ADD . .

RUN pip install --no-cache-dir --upgrade pip setuptools wheel

RUN python3 setup.py install

ENTRYPOINT ["python3", "takeover.py"]
CMD ["-v"]

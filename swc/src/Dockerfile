FROM python:3.8.12-slim

RUN pip3 install --upgrade pip

WORKDIR /swc/src

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 8000

CMD ["python3", "./swc/start.py"]


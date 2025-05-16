FROM python

WORKDIR /app

COPY ./src/requirements.txt ./

RUN pip3 install --upgrade pip -r requirements.txt

COPY . .

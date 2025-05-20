FROM python

WORKDIR /app

COPY ./requirements.txt ./

RUN pip3 install --upgrade pip -r requirements.txt

COPY . .

#Install Headless browser with linux kernel
FROM python:3

#Install python

#Work directory
WORKDIR /app
#install python dependencies
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

#Copy files into directory
COPY . ./app
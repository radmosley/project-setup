FROM selenium/standalone-chrome:3.141.59-neon
COPY requirements.txt .
RUN pip3 install requirements.txt
COPY . .
EXPOSE 4444

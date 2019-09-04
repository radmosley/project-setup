#Install Headless browser with linux kernel
FROM ubuntu:18.10

#Update apt-get and dependencies (curl, unzip, xvfb, tinywm, wget)
RUN apt-get -yqq update \
    && apt-get -yqq install curl unzip \
    && apt-get -yqq install xvfb tinywm \
    && apt-get -yqq install wget 

# RUN apt-get -yqq install chromium

#Install Nodejs
RUN apt-get -yqq install nodejs

#Install Python
RUN apt-get install -y python3-pip python3-dev \
    && cd /usr/local/bin \
    && ln -s /usr/bin/python3 python \
    && pip3 install --upgrade pip

#Install firefox browser
RUN wget -q "https://ftp.mozilla.org/pub/firefox/releases/67.0/linux-x86_64/en-US/firefox-67.0.tar.bz2" -0 /tmp/firefox-67.0.tar.bz2 \
    && tar zxf firefox-67.0.tar.bz2 -C /usr/local/bin \
    && ln -s /tmp/firefox/firefox /usr/lib/firefox/firefox \
    && rm -fr /tmp/firefox

# GeckoDriver v0.19.1
RUN wget -q "https://github.com/mozilla/geckodriver/releases/download/v0.23.0/geckodriver-v0.23.0-linux64.tar.gz" -O /tmp/geckodriver.tgz \
    && tar zxf /tmp/geckodriver.tgz -C /usr/local/bin \
    && rm /tmp/geckodriver.tgz \
    && chmod +x geckodriver

# chromeDriver v2.35
RUN wget -q "https://chromedriver.storage.googleapis.com/76.0.3809.68/chromedriver_linux64.zip" -O /tmp/chromedriver.zip \
    && unzip /tmp/chromedriver.zip -d /usr/local/bin \
    && rm /tmp/chromedriver.zip

# xvfb - X server display
ADD xvfb-chromium /usr/bin/xvfb-chromium
RUN ln -s /usr/bin/xvfb-chromium /usr/bin/google-chrome \
    && chmod +x /usr/local/bin/xvfb-chromium

# create symlinks to chromedriver and geckodriver (to the PATH)
RUN ln -s /usr/bin/geckodriver /usr/bin/chromium-browser \
    && chmod 777 /usr/bin/geckodriver \
    && chmod 777 /usr/bin/chromium-browser
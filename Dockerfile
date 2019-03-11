FROM python:3.6-slim

ADD requirements.txt /requirements.debian.txt
RUN set -xe && \
    cp /usr/share/zoneinfo/Asia/Shanghai /etc/localtime && echo "Asia/Shanghai" > /etc/timezone && \
    pip install --no-cache-dir -r /requirements.debian.txt

WORKDIR /code
ADD app /code/app
ADD extra /code/extra
ADD run_download.py /code
ADD wsgi.py /code
ADD entrypoint.sh /entrypoint.sh

EXPOSE 8080
ENV IP_DATA_FILE /tmp/ip.dat
RUN python run_download.py

ENTRYPOINT ["/entrypoint.sh"]
CMD gunicorn -w 4 -b :8080 wsgi:app -k eventlet

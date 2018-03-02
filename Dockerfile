FROM python:3-alpine3.7

ADD requirements.txt /requirements.txt
RUN set -xe && \
    #sed -i "s|dl-cdn.alpinelinux.org|mirrors.tuna.tsinghua.edu.cn|g" /etc/apk/repositories && \
    apk add -U tzdata libc6-compat && \
    cp /usr/share/zoneinfo/Asia/Shanghai /etc/localtime && echo "Asia/Shanghai" > /etc/timezone && \
    apk add -U -t xxbuild gcc g++ musl-dev && \
    pip install -r /requirements.txt -i https://pypi.tuna.tsinghua.edu.cn/simple && \
    apk del xxbuild && \
    rm -rf /var/cache/apk/*

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

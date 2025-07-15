FROM python:3.13-slim
COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /bin/

ADD requirements.txt /requirements.debian.txt
RUN set -xe && \
    cp /usr/share/zoneinfo/Asia/Shanghai /etc/localtime && echo "Asia/Shanghai" > /etc/timezone && \
    uv pip install --system --no-cache-dir -r /requirements.debian.txt

WORKDIR /code
ADD https://github.com/lionsoul2014/ip2region/raw/master/data/ip2region.xdb /code/data/
ADD app /code/app
ADD extra /code/extra
ADD wsgi.py /code
ADD entrypoint.sh /entrypoint.sh

EXPOSE 8080

ENTRYPOINT ["/entrypoint.sh"]
CMD gunicorn -w 4 -b :8080 wsgi:app -k gevent

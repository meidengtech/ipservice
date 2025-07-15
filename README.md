
使用方式
```
# docker build -t ipservice .
# docker run -d --name ipservice -p 8888:8080 ipservice
# curl -qs -X POST http://127.0.0.1:8888/q --data "ips=202.114.0.242,202.114.5.36" | jq
{
  "ret": {
    "202.114.0.242": [
      "中国 湖北省 武汉市",
      "教育网"
    ],
    "202.114.5.36": [
      "中国 湖北省 武汉市",
      "教育网"
    ]
  },
  "success": 1
}
```

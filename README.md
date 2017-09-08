### 这是一个抓取cz88.net的IP数据库并且包装成一个http查询接口的服务

使用方式
```
# docker build -t ipservice .
# docker run -d --name ipservice -p 8888:8080 ipservice
# curl -v -X POST http://ip.goodtp.com/q --data "ips=202.114.0.242,202.114.5.36" | jq
{
  "ret": {
    "202.114.0.242": [
      "湖北省武汉市",
      "华中科技大学DNS服务器"
    ],
    "202.114.5.36": [
      "湖北省武汉市",
      "华中科技大学"
    ]
  },
  "success": 1
}
```

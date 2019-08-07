
"""
URLError的使用
"""
from urllib import request, error


if __name__ == "__main__":
    url = "http://www.sjnsjacjaa.com"

    try:
        req = request.Request(url)
        rsp = request.urlopen(req)
        html = rsp.read().decode("gbk")
        print(html)

    except error.URLError as e:
        print("URLError: {0}".format(e.reason))
        print("URLError: {0}".format(e))
    except Exception as e:
        print(e)
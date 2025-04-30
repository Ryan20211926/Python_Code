# coding:utf-8
# @Time    : 2024/11/27 20:31
# @Author  : Ryan
# @FileName: ryan_requests.py
import requests

class Requests:
    def __init__(self):
        self.s = requests.Session()

    def request(self,url,method='get',**kwargs):
        if method == 'get':
            return requests.Session().request(url=url,method=method,**kwargs)
        elif method == 'post':
            return requests.Session().request(url=url,method=method,**kwargs)
        elif method == 'delete':
            return requests.Session().request(url=url,method=method,**kwargs)
        elif method == 'put':
            return requests.Session().request(url=url,method=method,**kwargs)

    def get(self,url,**kwargs):
        return self.request(url=url,**kwargs)

    def post(self,url,**kwargs):
        return self.request(url=url,method='post',**kwargs)

    def delete(self,url,**kwargs):
        return self.request(url=url,method='delete',**kwargs)

    def put(self,url,**kwargs):
        return self.request(url=url,method='put',**kwargs)

class RequestUtil():
    sess = requests.session()
    # 统一发送请求
    def all_send_requests(self,**kwargs):
        res = RequestUtil.sess.request(**kwargs)
        print(res.text)
        print(kwargs["method"])
        return res
if __name__ == '__main__':
    url ="http://www.baidu.com"
    requ = RequestUtil().all_send_requests(url=url,method="get")
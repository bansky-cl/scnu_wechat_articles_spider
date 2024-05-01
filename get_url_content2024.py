# coding: utf-8

from wechatarticles import ArticlesInfo
import pandas as pd

df = pd.read_csv("./article23-24/article23-24.csv")

content_list = []
if __name__ == "__main__":
    # update in 2024,5,1:
    # 1. 登录微信PC端随机打开一篇微信推送
    # 2. 打开fiddler抓包，过滤 "getappmsgext" 字段
    # 3. Headers 划到最下面获取 cookies
    # 4. Params 看到的 appmsg_token 为空则 appmsg_token = ""

    appmsg_token = ""
    cookie = "" # 必须要有
    test = ArticlesInfo(appmsg_token, cookie)

    def get_content(url):
        return test.content(url)[0]

    df['content'] = df['url'].apply(get_content)

df.to_csv("./article23-24/content23-24v3.csv", encoding='utf-8', index=None)


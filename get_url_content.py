# coding: utf-8

# 基于test/test_WechtInfo.py 进行修改
# 根据公众号平台获取到的url，再获取文章内容

import os
from pprint import pprint
import sys
from wechatarticles import ArticlesInfo
import pandas as pd
import time
import random
from tqdm import tqdm


# 从 get_article_url.py得到含url的数据
# 请自行修改路径
df = pd.read_csv("./output/article.csv")


content_list = []
if __name__ == "__main__":
    # 登录微信PC端获取文章信息
    # 下面两个参数随时更新

    # 这两个参数，我是通过PC端微信进行fiddler抓包
    # 随机点开一个微信公众号文章，再fiddler里面过滤"appmsg"的包
    # 其中 header里面含有cookie，cookie里面含有appmsg_token
    # 貌似1h换一次？有待证实

    appmsg_token = "appmsg_token"
    cookie = "cookie"

    # 想要获取微信文章点赞、评论等，可以自己查看wechatarticles包里面的ArticlesInfo类
    test = ArticlesInfo(appmsg_token, cookie)

    for article_url in tqdm(df['url']):
        content = test.content(article_url)
        content_list.append(content)
        # time.sleep(random.randint(1, 10)) 不用sleep也行

# 把文章内容存起来
df['content'] = content_list

# 请自行修改保存路径
df.to_csv("./output/content.csv", encoding='utf-8', index=None)
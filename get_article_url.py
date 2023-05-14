import json
import pandas as pd
import os

# 在微信公众号平台新建图文，插入超链接，搜索晚安华师得到文章，捉包得到respond的json，
# 每个json包含5篇文章（也就是一页），连续点击几十页就会请求超时，过段时间再试，保存至这个路径下

# 路径请自己修改
json_folder = "./respond_json"
files = os.listdir(json_folder)

url_list = []
title_list = []
tags_list = []

# 解析通过fiddler过滤"appmsg?action"得到的json
# 根据需要，我只提取了文章标题、标签、url，更多的请自行解析json

for file in files:
    json_path = json_folder + "/" + file
    print(json_path)
    with open(json_path, encoding='utf-8', mode='r') as f:
        json_dict = json.loads(f.readline())
        f.close()
        for msg in json_dict['app_msg_list']:
            title_list.append(msg['title'])
            url_list.append(msg['link'])
            tag_list = []
            for tag in msg['appmsg_album_infos']:
                tag_list.append(tag['title'])
            tags_list.append(tag_list)

df = pd.DataFrame({
    "title": title_list,
    "url": url_list,
    "tags": tags_list, # 多标签
})

# 得到的url文件名请自己修改，后续根据这个csv文件里面的url去获取对应的文章内容
df.to_csv('./output/article.csv', encoding='utf-8', index=None)

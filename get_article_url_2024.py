import json
import pandas as pd
import os
import time

json_file = "2024wanhua-clean.json"

# files = os.listdir(json_folder)

url_list = []
title_list = []
time_list = []
tags_list = []

### 2024

json_ls = []

with open(json_file, 'r', encoding='utf-8') as ipf:
    f = json.load(ipf)  # 57个
    for page in f:
        for article in page['publish_page']['publish_list']:
            # parse
            # title
            title_list.append(article['publish_info']['appmsgex'][0]['title'])
            # url
            url_list.append(article['publish_info']['appmsgex'][0]['link'])
            # time
            time_stamp = article['publish_info']['appmsgex'][0]['update_time']
            timeArray = time.localtime(time_stamp)
            otherStyleTime = time.strftime("%Y-%m-%d", timeArray)
            time_list.append(otherStyleTime)
            # tags
            current_tag_list = []
            for t in article['publish_info']['appmsgex'][0]['appmsg_album_infos']:
                current_tag_list.append(t['title'])
            tags_list.append(current_tag_list)

    ipf.close()

df = pd.DataFrame({
    "title": title_list,
    "url": url_list,
    "time": time_list,
    "tags": tags_list,
})

# 标题去重
df.drop_duplicates(subset=['title'],keep="first",inplace=True)
df.to_csv('./article23-24/article23-24.csv', encoding='utf-8', index=None)

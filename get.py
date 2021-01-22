import requests
import json


_id_ = []
_RGBurl_ = "http://musicapi.leanapp.cn/playlist/detail?id=3778678"  # 热歌榜
_BaseUrl_ = "http://music.163.com/song/media/outer/url?id="  # 解析接口

for i in range(0, 1):  # 获取榜单内歌曲id
    _id_.append(str(json.loads(requests.get(_RGBurl_).text)["playlist"]["trackIds"][i]["id"]))

for j in range(len(_id_)):
    _url_ = _BaseUrl_ + str(_id_[j]) + ".mp3"
    r = requests.get(_url_)
    with open(str(_id_[j]) + ".mp3", 'wb') as f:
        f.write(r.content)

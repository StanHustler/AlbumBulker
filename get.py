import requests
import json


def down_song(_num_, _path_):
    _id_ = []
    _name_ = []
    _RGBurl_ = "http://musicapi.leanapp.cn/playlist/detail?id=3778678"  # 热歌榜
    _DownBaseUrl_ = "http://music.163.com/song/media/outer/url?id="  # 解析接口
    _SrhBaseUrl_ = "http://musicapi.leanapp.cn/search?keywords="

    for i in range(0, _num_):  # 获取榜单内歌曲id，搜索id对应名称
        _id_.append(str(json.loads(requests.get(_RGBurl_).text)["playlist"]["trackIds"][i]["id"]))
        _name_.append(str(json.loads(requests.get(_SrhBaseUrl_ + _id_[i]).text)["result"]["songs"][0]["name"]))

    for j in range(0, len(_id_)):
        _url_ = _DownBaseUrl_ + str(_id_[j]) + ".mp3"
        r = requests.get(_url_)
        with open(_path_ + "//" + str(_name_[j]) + ".mp3", 'wb') as f:
            f.write(r.content)

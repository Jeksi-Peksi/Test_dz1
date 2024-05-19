import requests
import yaml

with open("config.yaml") as f:
    data = yaml.safe_load(f)


def test_step100500(login, title, description, content):
    header = {"X-Auth-Token": login}
    post = {"title": "Просто новый пост", "description": "Просто мой новый пост для проверки", "content": "111"}
    res = requests.post(data["address"] + "api/posts", json=post, headers=header)
    res2 = requests.get(data["address"] + "api/posts", headers=header)
    list_res2 = [i["description"] for i in res2.json()["data"]]
    assert description in list_res2



# post = {"title": "Просто новыйЙ пост", "description": "Просто мой новый пост", "content": "111"}

#def test_step2()
    #res2 = requests.post(data["address"] + "api/posts", headers=header)
    #list_res = [i["description"] for i in res2.json()["data"]]
    #assert description in list_post in list_res


#def test_step2(login, title, description, content):
    #header = {"X-Auth-Token": login}
    #res5 = requests.post(data["address"] + "api/posts, headers=")
    #list_res5 = [i["description"] for i in res5.json()["data"]]
    #assert description in list_res5
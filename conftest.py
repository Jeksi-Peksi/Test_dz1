import pytest
import yaml
import requests

with open("config.yaml") as f:
    data = yaml.safe_load(f)

@pytest.fixture()
def login():
    res1 = requests.post(data["address"] + "gateway/login", data={"username": data["username"], "password": data["password"]})
    print(res1.content)
    return res1.json()["token"]

@pytest.fixture()
def testtext1():
    print()
    return "Котиков любят все"


@pytest.fixture()
def title():
    res2 = requests.post(data["address"] + "gateway/login", data={"username": data["username"], "password": data["password"]})
    res3 = requests.post(data["address"] + "api/posts", data={"title": data["title"], "description": data["description"], "content": data["content"]})
    print(res2.content)
    print(res3.content)
    return res2.json() and res3.json()


@pytest.fixture()
def content():
    print()
    return "111"


@pytest.fixture()
def description():
    print()
    return "Просто мой новый пост для проверки"

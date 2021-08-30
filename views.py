import json
import random
from django.http import HttpResponse
from django.shortcuts import render


with open(r"C:\Users\anuto\PycharmProjects\coursovaya\templates\info.json", "r", encoding='utf-8') as file:
    text = file.read()
    file.close()
    data = json.loads(text)

with open(r"C:\Users\anuto\PycharmProjects\coursovaya\templates\users.json", "r", encoding='utf-8') as file:
    text = file.read()
    file.close()
    data2 = json.loads(text)

with open(r"C:\Users\anuto\PycharmProjects\coursovaya\templates\CurrentUser.json", "r", encoding='utf-8') as file:
    text = file.read()
    file.close()
    data3 = json.loads(text)

with open(r"C:\Users\anuto\PycharmProjects\coursovaya\templates\comments.json", "r", encoding='utf-8') as file:
    text = file.read()
    file.close()
    data4 = json.loads(text)

status = data3["user"]["status"]
log = data3["user"]["login"]

def save_data():
    dataFile = open(r"C:\Users\anuto\PycharmProjects\coursovaya\templates\info.json", "w", encoding="utf8")
    dataFile.write(json.dumps(data, ensure_ascii=False))
    dataFile.close()


def save_data2():
    dataFile = open(r"C:\Users\anuto\PycharmProjects\coursovaya\templates\users.json", "w", encoding="utf8")
    dataFile.write(json.dumps(data2, ensure_ascii=False))
    dataFile.close()


def save_data3():
    dataFile = open(r"C:\Users\anuto\PycharmProjects\coursovaya\templates\CurrentUser.json", "w", encoding="utf8")
    dataFile.write(json.dumps(data3, ensure_ascii=False))
    dataFile.close()


def save_data4():
    dataFile = open(r"C:\Users\anuto\PycharmProjects\coursovaya\templates\comments.json", "w", encoding="utf8")
    dataFile.write(json.dumps(data4, ensure_ascii=False))
    dataFile.close()



def AdminMain(request):
    org = {}
    status = data3["user"]["status"]
    org["userstat"] = status
    return render(request, 'AdminMain.html', org)

def AddCinemaTheater(request):
    req = request.GET
    org = {}
    s = []
    org["id"] = req.get("id")
    org["name"] = req.get("name")
    org["location"] = req.get("location")
    org["description"] = req.get("description")
    org["seanses"] = s
    data["cinemas"].append(org)
    save_data()
    return render(request, 'AddCinemaTheater.html', {})

def AddPerson(request):
    req = request.GET
    org = {}
    f = []
    org["id"] = req.get("id")
    org["name"] = req.get("name")
    org["sername"] = req.get("sername")
    org["lastname"] = req.get("lastname")
    org["work"] = req.get("work")
    org["films"] = f
    data["persons"].append(org)
    save_data()
    return render(request, 'AddPerson.html', {})

def AddSeans(request):
    req = request.GET
    org = {}
    org["id"] = req.get("ids")
    org["date"] = req.get("date")
    org["time"] = req.get("time")
    for i in data["films"]:
        if i["id"] == req.get("idf"):
            org["film"] = i["name"]
    for i in data["cinemas"]:
        if i["id"] == req.get("idc"):
            i["seanses"].append(org)
    save_data()
    return render(request,"AddSeans.html",{})


def AddFilm(request):
    req = request.GET
    org = {}
    org["id"] = req.get("id")
    org["name"] = req.get("name")
    org["time"] = req.get("time")
    org["description"] = req.get("description")
    data["films"].append(org)
    save_data()
    return render(request, 'AddFilm.html', {})

def DeleteCinema(request):
    req = request.GET
    for i in data["cinemas"]:
        if i ["id"] == req.get("id"):
            data["cinemas"].remove(i)
    save_data()
    return render(request,"DeleteCinemaTheater.html",{})

def DeleteFilm(request):
    req = request.GET
    for i in data["films"]:
        if i ["id"] == req.get("id"):
            data["films"].remove(i)
    save_data()
    return render(request,"DeleteFilm.html",{})

def DeleteSeans(request):
    req = request.GET
    for i in data["cinemas"]:
        if i ["id"] == req.get("idc"):
            for j in i["seanses"]:
                if j["id"] == req.get("id"):
                    i["seanses"].remove(j)
    save_data()
    return render(request,"DeleteSeans.html",{})
def DeletePerson(request):
    req = request.GET
    for i in data["persons"]:
        if i ["id"] == req.get("id"):
            data["persons"].remove(i)
    save_data()
    return render(request,"DeletePerson.html",{})

def AddInFilm(request):
    req = request.GET
    d = ""
    for i in data["films"]:
        if i["id"] == req.get("idf"):
            d = i["name"]
    for i in data["persons"]:
        if i["id"] == req.get("idp"):
            i["films"].append(d)
    save_data()
    return render(request,"AddInFilm.html",{})


def DeleteFromFilm(request):
    req = request.GET
    for i in data["persons"]:
        if i["id"] == req.get("id"):
            for j in i["films"]:
                if j == req.get("name"):
                    i["films"].remove(j)
    save_data()
    return render(request,"DeleteFromFilm.html",{})


def index(request):
    org = {}
    i = random.randint(-1,(len(data["films"])-1))
    org["name1"] = data["films"][i]["name"]
    org["text1"] = data["films"][i]["description"]
    org["image1"] = data["films"][i]["img"]
    j = random.randint(1,len(data["films"]))
    org["name2"] = data["persons"][j]["name"] + " " + data["persons"][j]["sername"] + " " + data["persons"][j]["lastname"]
    org["text2"] = data["persons"][j]["work"]
    org["image2"] = data["persons"][j]["img"]
    org["films"] = []
    status = data3["user"]["status"]
    org["userstat"] = status
    for k in range(0,len(data["persons"][j]["films"])):
        org["films"].append(data["persons"][j]["films"][k])
    return render(request,"index.html",org)


def Registration(request):
    req = request.GET
    org = {}
    error = {}
    k = 0
    for i in data2["users"]:
        if req.get("login") == i["login"]:
            k = 1
    if k == 1:
        error["error"] = "Такой логин уже зарегестрирован"
    else:
        org["login"] = req.get("login")
        org["name"] = req.get("name")
        org["sername"] = req.get("sername")
        org["status"] = "user"
        if req.get("password") == req.get("password2"):
            org["password"] = req.get("password")
            error["error"] = "Уже зарегестрировались? Войдите!"
            data2["users"].append(org)
            save_data2()
        else:
            error["error"] = "Пароли не сопрадают! Попробуйте еще раз!"
    return render(request,"Registration.html",error)


def ChangeStatus(request):
    req = request.GET
    for i in data2["users"]:
        if req.get("login") == i["login"]:
            i["status"] = req.get("status")
    save_data2()
    return render(request,"ChangeStatus.html",{})


def CinemaList(request):
    org = {}
    status = data3["user"]["status"]
    org["userstat"] = status
    org["cinemas"] = data["cinemas"]
    return render(request,"CinemaList.html",org)


def CinemaTemplate(request):
    org = {}
    req = request.GET
    status = data3["user"]["status"]
    org["userstat"] = status
    for i in data["cinemas"]:
        if i["id"] == req.get("id"):
            org["name"] = i["name"]
            org["location"] = i["location"]
            org["description"] = i["description"]
            org["seanses"] = i["seanses"]
    return render(request,"CinemaTemplate.html",org)


def FilmList(request):
    org = {}
    status = data3["user"]["status"]
    org["userstat"] = status
    org["films"] = data["films"]
    return render(request,"FilmList.html",org)


def FilmTemplate(request):
    org = {}
    com={}
    req = request.GET
    status = data3["user"]["status"]
    log = data3["user"]["login"]
    idf = str()
    for i in data["films"]:
        if i["name"] == req.get("page"):
            idf = i["id"]
    org["userlog"] = log
    org["userstat"] = status
    for i in data["films"]:
        if i["id"] == req.get("id") or i["id"] == idf:
            org["name"] = i["name"]
            org["time"] = i["time"]
            org["description"] = i["description"]
            org["img"] = i["img"]
            org["persons"] = []
    for i in data["persons"]:
        for j in i["films"]:
            if j == org["name"]:
                n = i["name"] + " " + i["sername"] + " " + i["lastname"] + "(" + i["work"] + ")"
                org["persons"].append(n)
    com["login"] = req.get("login")
    com["page"] = req.get("page")
    com["text"] = req.get("text")
    data4["comments"].append(com)
    save_data4()
    org["comments"] =[]
    for i in data4["comments"]:
        if i["page"] == org["name"]:
            org["comments"].append(i)
    return render(request,"FilmTemplate.html",org)


def PersonList(request):
    org = {}
    status = data3["user"]["status"]
    org["userstat"] = status
    org["persons"] = data["persons"]
    return render(request,"PersonList.html",org)


def PersonTemplate(request):
    org = {}
    com={}
    req = request.GET
    status = data3["user"]["status"]
    log = data3["user"]["login"]
    idf = str()
    for i in data["persons"]:
        n = i["name"] + " " + i["sername"] + " " + i["lastname"]
        if n == req.get("page"):
            idf = i["id"]
    org["userlog"] = log
    org["userstat"] = status
    for i in data["persons"]:
        if i["id"] == req.get("id") or i["id"] == idf:
            org["name"] = i["name"] + " " + i["sername"] + " " + i["lastname"]
            org["work"] = i["work"]
            org["films"] = i["films"]
            org["img"] = i["img"]
    com["login"] = req.get("login")
    com["page"] = req.get("page")
    com["text"] = req.get("text")
    data4["comments"].append(com)
    save_data4()
    org["comments"] =[]
    for i in data4["comments"]:
        if i["page"] == org["name"]:
            org["comments"].append(i)
    return render(request,"PersonTemplate.html",org)


def autorization(request):
    req = request.GET
    org = {}
    check = "false"
    org["result"] = check
    for i in data2["users"]:
        if i["login"] == req.get("login"):
            if i["password"] == req.get("password"):
                check = "right"
                org["result"] = check
                data3["user"] = i
                org["login"] = i["login"]
                org["password"] = i["password"]
                save_data3()
    return render(request,"autorization.html",org)


def exit(request):
    req = request.GET
    org = {}
    org["message"] = " "
    if req.get("des") == "Да":
        data3["user"]["login"] = None
        data3["user"]["password"] = None
        data3["user"]["name"] = None
        data3["user"]["sername"] = None
        data3["user"]["status"] = "unsigned"
        org["message"] = "Возвращайтесь к сайту"
        save_data3()
    if req.get("des") == "Нет":
        org["message"] = "Возвращайтесь к сайту"
    return render(request,"Exit.html",org)
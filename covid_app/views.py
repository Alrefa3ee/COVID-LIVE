from django.shortcuts import render
import requests
from bs4 import BeautifulSoup


def home(request):
    response = requests.get("https://www.worldometers.info/coronavirus/")
    src = response.content
    all1 = []
    soup = BeautifulSoup(src, "html.parser")
    all = soup.findAll("div",{"id":"maincounter-wrap"})
    for i in range(len(all)):
        all1.append(all[i].find("span").text)
    cases = str(all1[0])
    deaths = str(all1[1])
    recovered = str(all1[2])
    context = {"cases":cases,
               "deaths":deaths,
               "recovered":recovered}
    return render(request,"home.html",context)
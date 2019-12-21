from django.shortcuts import render
from django.http import HttpResponse
import requests
import json


# Create your views here.
def index(request):
    r = requests.get("https://api.github.com/repos/aiogram/aiogram/stats/contributors")
    json_data = json.loads(r.text)
    contributors = [
        {'total': contributor['total'],
         'login': contributor['author']['login'],
         'avatar': contributor['author']['avatar_url']}
        for contributor in json_data
    ]
    context = {'contributors': contributors}
    return render(request, 'contributors/index.html', context)

import json
import os
import faker

from django import http
from django.shortcuts import render, redirect


def read_datafile():
    filepath = os.path.join(os.path.dirname(__file__), "polls.json")
    with open(filepath) as fp:
        return json.loads(fp.read())

DATA = read_datafile()


def hello(request):
    content = '<html><body>Hello, {} from {}!</body></html>'.format(
        request.user,
        request.META['REMOTE_ADDR']
    )
    return http.HttpResponse(content, status=200)


def index(request):
    return render(request, "polls_app/index.html", {
        "polls": DATA,
        "faker": faker.Faker()
    })


def detail(request, pollname):
    if request.method == 'POST':
        return redirect('index')
    polls = (poll for poll in DATA if poll['pollName'] == pollname)
    poll = next(polls)
    return render(request, "polls_app/detail.html", {
        "poll": poll
    })

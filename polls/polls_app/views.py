import json
import os

from django import http
from django.shortcuts import render


def hello(request):
    content = '<html><body>Hello, {} from {}!</body></html>'.format(
        request.user,
        request.META['REMOTE_ADDR']
    )
    return http.HttpResponse(content, status=200)


def index(request):
    file_path = os.path.join(os.path.dirname(__file__), "polls.json")
    with open(file_path) as fp:
        polls = json.loads(fp.read())
    return render(request, "polls_app/index.html", {
        "polls": polls
    })

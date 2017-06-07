import json
import os

from django import http
from django.db.models import F
from django.shortcuts import render, redirect, get_object_or_404
from .models import Poll, Question, Choice


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
    polls_qs = Poll.objects.values('name', 'slug')
    return render(request, "polls_app/index.html", {
        "polls": polls_qs,
    })


def detail(request, slug):
    if request.method == 'POST':
        for key, value in request.POST.items():
            if key.startswith('question-'):
                Choice.objects.filter(pk=value).update(votes=F('votes') + 1)
        return redirect('result', slug=slug)
    try:
        poll = Poll.objects.prefetch_related('questions__choice_set').get(slug=slug)
    except Poll.DoesNotExist:
        return http.HttpResponse(content='Alta Intrebare', status_code=404)
    return render(request, "polls_app/detail.html", {
        "poll": poll
    })


def result(request, slug):
    try:
        poll = Poll.objects.prefetch_related('questions__choice_set').get(slug=slug)
    except Poll.DoesNotExist:
        return http.HttpResponse(content='Alta Intrebare', status_code=404)
    return render(request, "polls_app/result.html", {
        "poll": poll
    })

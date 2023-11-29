from django.shortcuts import render

# Create your views here.


def home(request):
    return render (request, 'index.html', {})


def detail(request):
    return render (request, 'detail.html', {})


def add_video(request):
    return render (request, 'addvid.html', {})


def issue_video(request):
    return render (request, 'issue.html', {})
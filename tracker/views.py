from django.shortcuts import render

def index(request):
    return render(request, 'tracker/index.html', {})

def view_logs(request):
    return render(request, 'tracker/view_logs.html', {})
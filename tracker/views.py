from django.shortcuts import render
from django.utils import timezone
from .models import Log

def index(request):
    return render(request, 'tracker/index.html', {})

def view_logs(request):
    logs = Log.objects.filter(practice_date__lte=timezone.now()).order_by('-practice_date')
    return render(request, 'tracker/view_logs.html', {'logs': logs})
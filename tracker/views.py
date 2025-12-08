from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone
from .models import Log
from .forms import LogForm

def index(request):
    return render(request, 'tracker/index.html', {})

def view_logs(request):
    logs = Log.objects.filter(date__lte=timezone.now()).order_by('-date')
    return render(request, 'tracker/view_logs.html', {'logs': logs})

def add_log(request):
    if request.method == 'POST':
        form = LogForm(request.POST)
        if form.is_valid():
            log = form.save(commit=False)
            log.user = request.user
            log.save()
            return redirect('view_logs')
    else:
        form = LogForm()
    return render(request, 'tracker/edit_log.html', {'form': form})

def edit_log(request, pk):
    log = get_object_or_404(Log, pk=pk)

    if request.method == 'POST':
        form = LogForm(request.POST, instance=log)
        if form.is_valid():
            log = form.save(commit=False)
            log.user = request.user
            log.save()
            return redirect('view_logs')
    else:
        form = LogForm(instance=log)
    return render(request, 'tracker/edit_log.html', {'form': form})
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.db.models import Sum
from django.shortcuts import render, redirect, get_object_or_404
from .models import Log
from .forms import LogForm

def index(request):
    if request.user.is_authenticated:
        time_by_song = (
            Log.objects.values('song')
            .filter(user=request.user)
            .annotate(totalTime=Sum('duration'))
            .order_by('-totalTime')
        )

        time_by_instrument = (
            Log.objects.values('instrument')
            .filter(user=request.user)
            .annotate(totalTime=Sum('duration'))
            .order_by('-totalTime')
        )

        time_by_part = (
            Log.objects.values('song', 'instrument')
            .filter(user=request.user)
            .annotate(totalTime=Sum('duration'))
            .order_by('-totalTime')
        )

        context = {
            'time_by_song': time_by_song,
            'time_by_instrument': time_by_instrument,
            'time_by_part': time_by_part,
        }

    else:
        context = {}

    return render(request, 'tracker/index.html', context)

def view_logs(request):
    if request.user.is_authenticated:
        logs = Log.objects.filter(user=request.user).order_by('-date')
        can_edit = True
    else:
        logs = Log.objects.all().order_by('-date')[:10]
        can_edit = False

    context = {
        'logs': logs,
        "can_edit": can_edit,
    }

    return render(request, 'tracker/view_logs.html', context)

@login_required
def view_specific_log(request, username):
    user_id = get_object_or_404(User, username=username)

    logs = Log.objects.filter(user=user_id).order_by('-date')

    context = {
        'logs': logs,
        'username': username,
        'can_edit': (request.user.is_superuser or user_id == request.user),
    }

    return render(request, 'tracker/view_logs.html', context)

@login_required
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

@login_required
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

@login_required
def delete_log(request, pk):
    log = get_object_or_404(Log, pk=pk)
    if request.method == 'POST':
        log.delete()
    return redirect('view_logs')
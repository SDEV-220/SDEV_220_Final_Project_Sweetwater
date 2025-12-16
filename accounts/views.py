# Thank goodness for past projects helping with accounts.

from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect


def register(request):
    """Register a new user."""
    if request.method != "POST":
        form = UserCreationForm()
    else:
        # Save the form if the user's data is sufficient.
        form = UserCreationForm(data=request.POST)
        if form.is_valid():
            new_user = form.save()
            login(request, new_user)
            return redirect("index")

    context = {"form": form}
    return render(request, "registration/register.html", context)
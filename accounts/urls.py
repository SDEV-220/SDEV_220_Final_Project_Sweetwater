from django.urls import path, include

from . import views

app_name = "accounts"

# The login and logout pages are the default Django ones. Registration is custom.
urlpatterns = [
    path("", include("django.contrib.auth.urls")),
    path("register/", views.register, name="register"),
]
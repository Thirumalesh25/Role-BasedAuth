from django.shortcuts import render, HttpResponse
from django.contrib.auth import login as django_login
from rest_framework.decorators import api_view
from django.contrib.auth.models import User


# Create your views here.
def home(req):
    return render(req, "login/home.html")


@api_view(["GET"])
def login(req):
    if req.method=="GET":
        return render(req, "login/login.html")

@api_view(["GET", "POST"])
def loginuser(request):
    if request.method == "GET":
        return HttpResponse("Not Authenticated")

    if request.method == "POST":
        password = request.POST.get("password")
        name = request.POST.get("username")
        param = {"name":name}
        try:
            user = User.objects.get(username=name)
        except User.DoesNotExist:
            return HttpResponse("User does not exist")

        if user.check_password(password):
            return render(request, "login/loginuser.html", param)
        else:
            return HttpResponse("Incorrect password")

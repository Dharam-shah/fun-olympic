from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, "homepage/homepage.html")


def user_profile(request):
    return render(request, "user/user_profile.html")
from django.shortcuts import render
from django.views.generic import CreateView

# Create your views here.
# class SignUpView(CreateView):
#     template_name = 'account/registration.html'


def register(request):
    #return HttpResponse("Homepage")
    return render(request, "account/register.html")

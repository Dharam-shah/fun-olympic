from django.shortcuts import render
from django.views.generic import CreateView
from .forms import SignUpForm
# Create your views here.
# class SignUpView(CreateView):
#     template_name = 'account/registration.html'


# def register(request):
#     #return HttpResponse("Homepage")
#     return render(request, "account/register.html")

class SignUpView(CreateView):
    form_class = SignUpForm
    template_name = 'account/register.html'

    # def post(self, request, *args, **kwargs):
    #     form = self.form_class(request.POST)
    #     if form.is_valid():
    #         user = form.save(commit=False)
    #         user.is_active = False
    #         user.save()

    #         current_site = get_current_site(request)
    #         subject = 'Click here to activate your accout'
    #         message = render_to_string(
    #             'account/activation_email.html', {
    #                 'user': user,
    #                 'domain': current_site.domain,
    #                 'uid': urlsafe_base64_encode(force_bytes(user.pk)),
    #                 'token': account_activation_token.make_token(user),

    #             })
    #         user.email_user(subject, message)
    #         messages.success(
    #             request, 'Please Confirm your email to complete registration.')
    #         return redirect('/')

    #     return render(request, self.template_name, {'form': form})

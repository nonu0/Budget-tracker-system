from django.shortcuts import render,redirect,resolve_url
from django.views.generic import FormView,View,CreateView
from authentication.forms import RegisterForm,MyLoginForm
from django.contrib.sites.shortcuts import get_current_site
from django.contrib.auth import logout,login,authenticate,get_user_model
from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_encode,urlsafe_base64_decode
from django.utils.encoding import force_bytes,force_str
from authentication.tokens import account_activation_token
from budget.utils import RegisterLoginPagesMixin,SuccessMessageMixin
from django.conf import settings
from rest_framework import permissions
from django.core.exceptions import ValidationError
from django.contrib import messages
from .tokens import account_activation_token
from django.urls import reverse_lazy
from django.core.mail import EmailMessage
from django.http import HttpResponseRedirect
# # Create your views here.

User = get_user_model()

def activation_email(User,request):
        current_site = get_current_site(request)
        email_subject = 'Activate your account'
        email_body = render_to_string('activate-email.html',{
            'User':User,
            'domain':current_site,
            'uid':urlsafe_base64_encode(force_bytes(User.pk)),
            'token':account_activation_token.make_token(User) 
        })

        
        email = EmailMessage(subject=email_subject,body=email_body,
                             from_email=settings.EMAIL_FROM_USER,to=[User.email])
        print(email)
        email.send()

class RegisterView(RegisterLoginPagesMixin,SuccessMessageMixin,CreateView):
    template_name = 'authentication/register.html'
    form_class = RegisterForm
    success_url = reverse_lazy('budget:home-user')
    permission_classes = (permissions.AllowAny, )
    success_message = 'user created successfully'

    def form_valid(self, form):
            username = form.cleaned_data.get('username')
            fname = form.cleaned_data.get('first_name')
            lname = form.cleaned_data.get('last_name')
            email = form.cleaned_data.get('owner')
            password = form.cleaned_data.get('password')
            confirm_password = form.cleaned_data.get('confirm_password')
            
            if password == confirm_password:
                
                user = User.objects.create_user(email=email,username=username,password=password)
                form.instance.user = user
                instance = form.save(commit=False)
                form.save()
                
                activation_email(user,self.request)
                messages.add_message(self.request,messages.SUCCESS,
                "We've sent you an email to verify your account")
                return redirect('authentication:login')
            else:
                raise ValidationError(self.request,'Password fields must match')
        


def activate_user(request,uidb64,token):
    try:
        uid = force_bytes(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except Exception as e:
        user=None

    if user and account_activation_token.check_token(user,token):
        user.email_verified=True
        user.save()

        messages.add_message(request,messages.SUCCESS,
        'Email verified,you can now login')
        return redirect('authentication:login')

    return render(request,'activate-failed.html',{'user':user}) 

class LoginView(RegisterLoginPagesMixin,FormView):
    """
    Display the login form and handle the login action.
    """
    next_page = 'budget:home-user'
    template_name = 'authentication/login.html'
    form_class = MyLoginForm
    success_url = reverse_lazy('budget:home-user')
    redirect_authenticated_user = False
    extra_context = None


    def dispatch(self, request, *args, **kwargs):
        if self.redirect_authenticated_user and self.request.user.is_authenticated:
            redirect_to = self.get_success_url()
            if redirect_to == self.request.path:
                raise ValueError(
                    "Redirection loop for authenticated user detected. Check that "
                    "your LOGIN_REDIRECT_URL doesn't point to a login page."
                )
            return HttpResponseRedirect(redirect_to)
        return super().dispatch(request, *args, **kwargs)

    


    def form_valid(self, form):
        uname = form.cleaned_data.get('username')
        pword = form.cleaned_data.get('password')
        usr = authenticate(self.request,username=uname,password=pword)
        if not usr.email_verified:
            messages.add_message(self.request,messages.ERROR,
            'Email is not verified')
            return render(self.request,'activate-email.html')
        if usr is not None:
            login(self.request,usr)
        else:
            return render(self.request,self.template_name,{'form':self.form_class,'error':'invalid credentials'})
        return super().form_valid(form)

    def get_default_redirect_url(self):
        """Return the default redirect URL."""
        if self.next_page:
            return resolve_url(self.next_page)
        else:
            return resolve_url(settings.LOGIN_REDIRECT_URL)


class LogoutView(View):
    def get(self,request):
        logout(request)
        return redirect('budget:home-guest')

from django.shortcuts import render,get_object_or_404,redirect
from .models import *
# from django.db import models
# from django.views.generic import TemplateView
# from django.contrib.auth.mixins import PermissionRequiredMixin
from django.contrib import messages



# class GetObjectMixin(object):
#     template_name = None
#     form_class = None
#     success_url = None
#     objs = []
#     def form_valid(self, form):
#         print('working')
#         for obj in self.objs:
#             obj = form.cleaned_data.get('obj')
#             form.instance.owner = self.request.user.owner
#             print(form.instance.owner)
#             form.instance.save()
#         # messages.success(self.request,'Debt added successfully')
#         return super().form_valid(form)
    

class FetchData(object):
    model = None
    def get_context_data(self, **kwargs):
        context =  super().get_context_data(**kwargs)
        owner = self.request.user
        model_objs = self.model.objects.using('budget').filter(owner=owner)
        context['model_objs'] = model_objs
        return context


class SuccessMessageMixin:
    """
    Add a success message on successful form submission.
    """
    success_message = ''

    def form_valid(self, form):
        response = super().form_valid(form)
        success_message = self.get_success_message(form.cleaned_data)
        if success_message:
            messages.success(self.request, success_message)
        return response

    def get_success_message(self, cleaned_data):
        return self.success_message % cleaned_data

class RegisterLoginPagesMixin(object):
    template_name = None
    form_class = None
    def dispatch(self,request,*args,**kwargs):
        if request.user.is_authenticated:
            print('user is authenticated')
            return redirect('budget:home-user')
        return super().dispatch(request,*args,**kwargs)


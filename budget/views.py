# from django.shortcuts import render,HttpResponse
from budget.models import Owner,Income,Expenses,Debt,UserProfile
from budget.forms import IncomeForm,ExpenseForm,DebtForm,UserImageForm
# from django.core.exceptions import ValidationError
from budget.multiforms import MultiFormsView
from django.views.generic import TemplateView,CreateView
# from budget.utils import RegisterLoginPagesMixin
from django.urls import reverse_lazy
from .utils import FetchData
from django.http import HttpResponseRedirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models.functions import Extract

# # Create your views here.


class HomeView(TemplateView):
    template_name = 'home-user.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        owner = self.request.user
        print('owner',owner)
        income = Income.objects.filter(owner=owner)
        debt = Debt.objects.filter(owner=owner)
        expense = Expenses.objects.filter(owner=owner)
        expense_total = [expense_total.actual_amount for expense_total in expense]
        expense_months = list(Expenses.objects.annotate(month_stamp=Extract('date_added','month')).values_list('month_stamp',flat=True))
        # months = calendar.month_abbr[expense_months]
        gross_expense = sum(expense_total)
        # print(type(months))
        debt_total = [debt_total.actual_amount for debt_total in debt]
        gross_debt = sum(debt_total)
        actual_income = [actual_income.actual_amount for actual_income in income]
        gross_income = sum(actual_income)
        net_income = gross_income - gross_debt
        context['expense_total'] = expense_total
        context['actual_income'] = actual_income
        context['debt_total'] = debt_total
        context['gross_income'] = gross_income
        context['gross_debt'] = gross_debt
        context['net_income'] = net_income
        context['gross_expense'] = gross_expense
        context['expense_months'] = expense_months
        context['owner'] = owner
        return context


class MyUserProfile(LoginRequiredMixin,CreateView):
    template_name = 'user-profile.html'
    login_url = 'budget:login'
    redirect_field_name = 'budget:login'
    success_url = reverse_lazy('budget:user-profile')
    form_class = UserImageForm

    def form_valid(self,form):
        image = form.cleaned_data.get('image')
        pro_pic = UserProfile.objects.create(
          owner=self.request.user,image=image
        )
        form.instance.user = self.request.user
        form.instance.save()
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        owner = self.request.user
        context['owner'] = owner
        return context


           
class AllForms(LoginRequiredMixin,MultiFormsView):
    template_name = 'forms.html'
    login_url = 'authentication:login'
    redirect_field_name = 'authentication:login'
   
    form_classes = {'income': IncomeForm,
                    'expense': ExpenseForm,
                    'debt': DebtForm,
                    }

    success_urls = {
        'income': reverse_lazy('budget:forms'),
        'expense': reverse_lazy('budget:forms'),
        'debt': reverse_lazy('budget:forms'),
    }

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        owner = self.request.user
        context['owner'] = owner
        return context

    def income_form_valid(self, form):
        source = form.cleaned_data.get('source')
        planned_amount = form.cleaned_data.get('planned_amount')
        actual_amount = form.cleaned_data.get('actual_amount')
        form_name = form.cleaned_data.get('action')
        form.instance.owner = self.request.user
        form.instance.save()
        return HttpResponseRedirect(self.get_success_url(form_name))
    
    def expense_form_valid(self, form):
        category = form.cleaned_data.get('category')
        name_of_expense = form.cleaned_data.get('name_of_expense')
        planned_amount = form.cleaned_data.get('planned_amount')
        actual_amount = form.cleaned_data.get('actual_amount')
        form_name = form.cleaned_data.get('action')
        form.instance.owner = self.request.user
        form.instance.save()
        return HttpResponseRedirect(self.get_success_url(form_name))

    def debt_form_valid(self, form):
        paid_to = form.cleaned_data.get('paid_to')
        planned_amount = form.cleaned_data.get('planned_amount')
        actual_amount = form.cleaned_data.get('actual_amount')
        form_name = form.cleaned_data.get('action')
        form.instance.owner = self.request.user
        form.instance.save()
        return HttpResponseRedirect(self.get_success_url(form_name))


class  HomeGuest(TemplateView):
    template_name = 'home-guest.html'



class DebtView(LoginRequiredMixin,TemplateView):
    template_name = 'budget:widgets.html'


class AllTables(LoginRequiredMixin,FetchData,TemplateView):
    template_name = 'tables.html'
    login_url = 'authentication:login'
    redirect_field_name = 'login.html'
    model = Income
    
    def get_context_data(self, **kwargs):

        context = super().get_context_data(**kwargs)
        owner = self.request.user
        household_cat = Expenses.objects.filter(category=1).filter(owner=owner)
        food_cat = Expenses.objects.filter(category=2).filter(owner=owner)
        transportation_cat = Expenses.objects.filter(category=3).filter(owner=owner)
        personal_cat = Expenses.objects.filter(category=4).filter(owner=owner)
        subscriptions_cat = Expenses.objects.filter(category=5).filter(owner=owner)
        savings_cat = Expenses.objects.filter(category=6).filter(owner=owner)
        medical_cat = Expenses.objects.filter(category=7).filter(owner=owner)
        context['household_cat'] = household_cat
        context['food_cat'] = food_cat
        context['transportation_cat'] = transportation_cat
        context['personal_cat'] = personal_cat
        context['subscriptions_cat'] = subscriptions_cat
        context['savings_cat'] = savings_cat
        context['medical_cat'] = medical_cat
        context['owner'] = owner
        return context

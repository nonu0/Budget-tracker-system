from budget.models import Owner,Income,Debt,Expenses,UserProfile
from django import forms
from django.forms import  ModelForm



class MultipleForm(forms.Form):
    action = forms.CharField(max_length=60, widget=forms.HiddenInput())

class IncomeForm(MultipleForm,forms.ModelForm):
    class Meta:
        model = Income
        fields = ['source','planned_amount','actual_amount']

class DebtForm(MultipleForm,forms.ModelForm):
    class Meta:
        model = Debt
        fields = ['paid_to','planned_amount','actual_amount']

class ExpenseForm(MultipleForm,forms.ModelForm):
    class Meta:
        model = Expenses
        fields = ['category','name_of_expense','planned_amount','actual_amount']
        

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = Owner
        fields = ['first_name','last_name','username','owner','gender','town','county','phone_no','address','code']

class UserImageForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['image']
from django.shortcuts import render
from formsApp import forms

# Create your views here.
def UserRegistrationView(request):
    form=forms.UserRegistrationForm()
    if request.method=='POST':
        form=forms.UserRegistrationForm(request.POST)
        if form.is_valid():
            print("form is valid")
            print("First Name",form.cleaned_data['firstName'])
            print("Last Name",form.cleaned_data['lastName'])
            print("Email address",form.cleaned_data['Email_ID'])


    return render(request,'UserRegistration.html',{'form':form})

from django.shortcuts import render

# Create your views here.

def renderTemplates(request):
    return render(request,'templatesApp/firstTemplates.html')

def renderEmployee(request):
    myDict={"id": 500,"name":"John","salary":50000,"Designation":"Software Engineer"}
    return render(request,'templatesApp/employeeTemplate.html',myDict)

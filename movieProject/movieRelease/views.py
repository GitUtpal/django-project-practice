from django.shortcuts import render
from movieRelease.models import Movie
from movieRelease.forms import MovieForm

# Create your views here.

def index(request):
    return render(request,'moviePages/index.html')

def listMoview(request):
    moviewList=Movie.objects.all()
    return render(request,'moviePages/listMovies.html',{'movies':moviewList})

# def addMovie(request):
#     form=MovieForm()
#     if request.method=='POST':
#         form=movieRelease(request.POST)
#         if form.isValid():
#             form.save()
#         return index(request)
#     return render(request,'moviePages/addMovie.html',{'form':form})
#
# if request.method=='POST':
#     form=ProjectForm(request.POST)
#     if form.is_valid():
#         form.save()
#     return index(request)

def addMovie(request):
    form=MovieForm()
    if request.method=='POST':
        form=MovieForm(request.POST)
        if form.is_valid():
            form.save()
        return index(request)

    return render(request,'moviePages/addMovie.html',{'form':form})

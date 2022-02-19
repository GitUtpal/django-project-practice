from django.shortcuts import render
from passengerApp.models import PassengerList

# Create your views here.
def passengerData(request):
    passenger=PassengerList.objects.all()
    pass_dict={'passengerlist':passenger}
    return render(request,'passengerlist.html',pass_dict)

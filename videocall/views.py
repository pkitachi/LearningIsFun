from django.shortcuts import render

# Create your views here.

def vhome(request):
    return render(request,'videocall/VidyoConnector.html')
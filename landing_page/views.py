from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    if request.method == "POST":
        return HttpResponse("Great job; this was a post request")
    else:
        return HttpResponse(request.method)
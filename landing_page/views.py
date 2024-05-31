from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    if request.method == "GET":
        return HttpResponse("Great job Lilian; this was a get request")
    else request.method == "POST":
        return HttpResponse("This was a post request")
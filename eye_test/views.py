from django.http import HttpResponse

def index(request):
    return HttpResponse("<h1>THIS IS THE INDEX PAGE FOR EYETEST DRF</H1>")
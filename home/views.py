from django.shortcuts import render, HttpResponse

def index(request):
    return render(request, 'index.html')
    #return HttpResponse("this is login page")

def hm(request):
    return HttpResponse("this is home page")

def taskm(request):
    return render(request, 'taskm.html')
def filem(request):
    return render(request, 'filem.html')
def fileupload(request):
    return render(request, 'fileup.html')
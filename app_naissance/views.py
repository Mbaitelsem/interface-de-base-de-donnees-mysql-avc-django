from django.http import HttpResponse
from django.shortcuts import render


def home_view(request):
    #return HttpResponse('hello')
    return render(request, 'home.html')

def contact_view(request):
    # return HttpResponse('hello')
    return render(request, 'contacte.html')
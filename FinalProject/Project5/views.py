from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader, Template

def index(request):
    print(request.POST)
    if (request.POST.get('highlight1')):
        string = getHighlight(1)
    elif (request.POST.get('highlight2')):
        string = getHighlight(2)
    elif (request.POST.get('highlight3')):
        string = getHighlight(3)
    else:
        string = "<h4>Click a button above to run the code!</h4>"
    return render(request, 'Project5/index.html', {'string': string})

def getHighlight(num):
    string = '<h4>Highlight '+ str(num) + ': </h4> <br>' + '<p> example: patient needs to take <mark>20mg</mark> of <mark>ibuprofen</mark> daily. </p>'
    return string



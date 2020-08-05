from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return render(request,'index.html')

def analyze(request):

    text = request.POST.get('text','default')
    
     # Check checkbox values
    removepunc = request.POST.get('removepunc', 'off')
    fullcaps = request.POST.get('fullcaps', 'off')
    newlineremover = request.POST.get('newlineremover', 'off')
    extraspaceremover = request.POST.get('extraspaceremover', 'off')

    #Check which checkbox is on
    if removepunc == "on":
        punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        analyzed = ""
        for char in text:
            if char not in punctuations:
                analyzed = analyzed + char
        text=analyzed
    if(fullcaps=="on"):
        analyzed = ""
        for char in text:
            analyzed = analyzed + char.upper()
        text=analyzed
    if (newlineremover=="on"):
        analyzed = ""
        for char in text:
            if char!='\n' and char!='\r':
                analyzed = analyzed + char
            else:
                analyzed = analyzed + ' '
        text=analyzed
    if(extraspaceremover=="on"):
        analyzed = ""
        for index, char in enumerate(text):
            if not(text[index] == " " and text[index+1]==" "):
                analyzed = analyzed + char
        text=analyzed
    
    
    params = {'analyzed_text': text}
    return render(request, 'index.html', params)

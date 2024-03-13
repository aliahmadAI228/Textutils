
from django.http import HttpResponse
from django.shortcuts import render
def hello(request):
    return render(request,"index.html")
#     # return HttpResponse("<h1>home</h1> <button>Click Me!</button>")
# def analyzer(request):
#     return HttpResponse("my first application")
# def contact(request):
#     return HttpResponse("03153846366")
def analyze(request):
    if request.method=="POST":
        djtext=request.POST.get('text','default')
        print(djtext)
        removepunc=request.POST.get('removepunc','off')
        Uppercase=request.POST.get('fullcaps','off')
        newlineremover=request.POST.get('newlineremover','off')
        print(removepunc)
        if removepunc=="on":
          punctuations='''(),"-?[]!@#$%^&*_<>'''
          analyzed=" "
          for char in djtext:
           if char not in punctuations: 
             analyzed=analyzed+char 
           params={'purpose':"remove punc","analyzed_text":analyzed}
           djtext=analyzed
           
        if(Uppercase=="on"):
          analyzed=""
          for char in djtext:
           analyzed=analyzed+char.upper()
          params={'purpose':"upper case","analyzed_text":analyzed}
          djtext=analyzed
          
        if(newlineremover=="on"):
          analyzed=""
          for char in djtext:
           if char !='\n' and char!='\r':
              analyzed=analyzed+char
          params={'purpose':"Remove new line","analyzed_text":analyzed}
          djtext=analyzed
          
        return render(request,'analyze.html',params)
    # 
# def charcount(request):
#     return HttpResponse("<button>Click Me!</button>")
# def capfirst(request):
#     return HttpResponse("capitalizefirst")
# def newline(request):
#     return HttpResponse("newlineremove")
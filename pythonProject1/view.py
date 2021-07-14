#I have created this file-prasad
from django.http import HttpResponse
from django.shortcuts import render
def nav(request):
    return HttpResponse('''<h1>Hello   I am Prasad...</h1> <a href='https://www.youtube.com/channel/UCeVMnSShP_Iviwkknt83cww'> Django Codewith Harry 
    <h2></h2> <a href='https://www.microsoft.com/en-in/'> microsoft
    <h2></h2> <a href='https://www.google.com/'> google
    <h2></h2> <a href='https://www.tcsion.com/LX'> tcs
    <h2></h2> <a href='https://www.infosys.com'> infosys 
    <h2></h2> <a href='http://127.0.0.1:8000/spaceremove/'> spaceremove      
    <h2></h2> <a href='http://127.0.0.1:8000/charcount/'>  charcount 
     </a> ''')


def index(request):
    param = {'name':'prasad','place': 'mars'}
    return render(request,'index.html', param)

def about(request):
    return HttpResponse('About  me...')

def removepunc(request):
    return HttpResponse("remove punc")


def capitalizefirst(request):
    return HttpResponse("capitalize first")

def newlineremove(request):

    return HttpResponse("New line remove")

def spaceremove(request):

    return HttpResponse("space remover  <a href='/'>back</a>")#//

def charcount(request):
 #    print(request.GET.get('text','default')
     return HttpResponse("charcount ")
def analyze(request):

    djtext = request.GET.get('text', 'off')


    removepunc = request.GET.get('removepunc','off')
    fullcaps = request.GET.get('fullcaps','off')
    newlineremover = request.GET.get('newlineremover', 'off')
    charcount = request.GET.get('charcount', 'off')

    print(removepunc)
    print(djtext)
    if  removepunc=="on":
        punctuations='''!();:'"\,<>./?@?#$%^@&'''
        analyzed =""
        for char in djtext:
            if char not in punctuations:

               analyzed = analyzed + char
        param={'purpose':'removed pun','analyzed_text': analyzed}
        return render(request ,'analyze.html', param )
    elif (newlineremover == "on"):
        analyzed = ""
        for char in djtext:
            analyzed = analyzed + char
        param = {'purpose': 'New line Remover', 'analyzed_text': analyzed}
        return render(request, 'analyze.html', param)
    elif (charcount == "on"):
        analyzed = ""
        count = 0
        for char in djtext:
           if char.isspace() != True:
               count = count + 1
        print(count)
        param = {'purpose': 'charater count', 'analyzed_text': analyzed}
        return render(request, 'analyze.html', param)
    elif(fullcaps =="on"):
       analyzed =""
       for char in djtext:
             analyzed = analyzed + char.upper()
       param = {'purpose': 'change to uppercase', 'analyzed_text': analyzed}
       return render(request, 'analyze.html', param)
    else:
        return HttpResponse('Error')
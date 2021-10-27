from django.shortcuts import render
from django.http import HttpResponse
from . import util
import markdown2


def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

def show_article(request,url):
    
    text = util.get_entry(url)
    if text :
        text = markdown2.markdown(text)
        return render(request, 'encyclopedia/article.html', {'text':text})
    else:
        return render(request, 'encyclopedia/notfound.html', {'url':url})

def find(request):
    #return HttpResponse("Hello, world!")
    findStr = request.GET['q']
    text = util.get_entry(findStr)
    if text :
        text = markdown2.markdown(text)
        return render(request, 'encyclopedia/article.html', {'text':text})
    else:
        list_found = util.list_res_find(findStr)
        if len(list_found):
            return render(request, "encyclopedia/found.html", {'findStr':request.GET['q'],'list_found':list_found})

    return HttpResponseRedirect(reverse("tasks:index"))
    

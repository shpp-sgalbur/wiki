from django.shortcuts import render
from django.http import HttpResponse
from . import util
import markdown


def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

def show_article(request,url):
    
    text = util.get_entry(url)
    if text :
        text = markdown.markdown(text)
        return render(request, 'encyclopedia/article.html', {'text':text})
    else:
        return render(request, 'encyclopedia/notfound.html', {'url':url})

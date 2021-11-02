from django.shortcuts import render
from django.http import HttpResponse
from . import util
import markdown2
from django import forms
from django.urls import reverse
from django.http import HttpResponseRedirect
import os

class NewPageForm(forms.Form):
    title = forms.CharField(label="Title")
    text = forms.CharField(widget=forms.Textarea)

def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

def show_article(request,url):
    
    text = util.get_entry(url)
    if text :
        text = markdown2.markdown(text)
        return render(request, 'encyclopedia/article.html', {'title':url,'text':text})
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
        else:
            return render(request, 'encyclopedia/notfound.html', {'url':findStr})

def createPage(request):
    if request.method == "POST":
        form = NewPageForm(request.POST)
        if form.is_valid():     
            title = form.cleaned_data['title']       
            file_name = 'entries/'+ title + '.md'            
            if os.path.exists(file_name):
                return render(request, "encyclopedia/page_exists.html", {"file_name": file_name})
            else:
                
                text = form.cleaned_data['text']
                file = open(file_name, "w")
                file.write("#" + title + "\r\n" + text)
                file.close()
                return HttpResponseRedirect(reverse("show_article", kwargs={'url':title}))
        else:
            return render(request, "encyclopedia/new_page.html", {"form": form.as_p})

    return render(request, "encyclopedia/new_page.html", {"form": NewPageForm().as_p})
    
def edit_page(request, url):
    
    text = util.get_entry(url)
    return render(request, "encyclopedia/edit_page.html", {'form':NewPageForm({'title':url, 'text':text}), 'title':url})
    return render(request, "encyclopedia/article.html", {"form": NewPageForm().as_p})

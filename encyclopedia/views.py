from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
import markdown2
from . import util
from django.contrib import messages

def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

def page(request,title):
    md = markdown2.Markdown()
    entry = util.get_entry(title)
    storage = messages.get_messages(request)
    messags = []
    for message in storage:
        messags.append(message)
    if entry is None:
        return render(request,"encyclopedia/error.html")
    html = md.convert(entry)
    return render(request,"encyclopedia/page.html",{"title":title,"html":html,"messages":messags})

def search(request):
    q = request.POST['q']
    page = util.get_entry(q)
    if page is not None:
        return HttpResponseRedirect(reverse('page',args=[q,]))
    else:
        entries = util.search_entries(q)
        if len(entries)==0:
            entries.append("No Results Found!")
        context = {"q":q,"entries":entries}
        return render(request,"encyclopedia/search.html",context)


def newPage(request):
    return render(request,"encyclopedia/newPage.html")

def savePage(request):
    title = request.POST["title"]
    content = request.POST["content"]
    entry = util.get_entry(title)
    if entry is not None:
        return render(request,"encyclopedia/sorryItExist.html",{"title":title})
    else:
        util.save_entry(title,content)
        messages.add_message(request,messages.SUCCESS,"Page Successfully Created!!")
        return HttpResponseRedirect(reverse('page',args=[title,]))

def editPage(request,title):
    if request.method == "GET":
        content = util.get_entry(title)
        if content is None:
            return render(request,"encyclopedia/error.html")
        return render(request,"encyclopedia/editPage.html",{"title":title,"content":content})
    else:
        content = request.POST["content"]
        util.save_entry(title,content)
        messages.add_message(request,messages.SUCCESS,"Page Successfully Edited!!")
        return HttpResponseRedirect(reverse('page',args=[title,]))

def random(request):
    md = markdown2.Markdown()
    entry = util.random_entry()
    messags = []
    if entry is None:
        return render(request,"encyclopedia/error.html")
    html = md.convert(entry[1])
    title = entry[0]
    return render(request,"encyclopedia/page.html",{"title":title,"html":html,"messages":messags})

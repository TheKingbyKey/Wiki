from django.shortcuts import render
import markdown2
from . import util


def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

def page(request,title):
    md = markdown2.Markdown()
    html = md.convert(util.get_entry(title))
    return render(request,"encyclopedia/page.html",{"html":html})

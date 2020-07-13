from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("wiki/<str:title>/",views.page,name="page"),
    path("wiki/searchResults",views.search,name="search"),
    path("wiki/createNewPage",views.newPage,name="newPage"),
    path("wiki/savePage",views.savePage,name="savePage"),
    path("wiki/edit/<str:title>",views.editPage,name="editPage"),
    path("wiki/random",views.random,name="random")
]

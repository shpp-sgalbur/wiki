from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path('<str:url>',views.show_article, name ='show_article'),
    path("find/", views.find, name="find"),
    path("create/", views.createPage, name='new_page'),
    path('<str:url>/edit/',views.edit_page, name ='edit_page')
    
]

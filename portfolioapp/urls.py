from django import views
from django.urls import path,include
from . import views
urlpatterns = [
    path('',views.home,name='/'),
    path('add',views.add,name='add'),
    path('query',views.query,name='query')
]

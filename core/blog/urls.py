from django.urls import path , include
from .views import *
from django.views.generic import TemplateView

urlpatterns = [
    path('fbv-index', indexView , name='fbv-index'),
    path('cbv-index', TemplateView.as_view(template_name= "index.html", extra_context= {'name':'abedi', 'title':'cbv'}))
    
]

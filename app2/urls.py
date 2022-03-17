from django.urls import path
from . import views
urlpatterns = [
    path('',views.hi,name='home-page'),
    path('output',views.output,name='outpage'),
    path('conti',views.conti,name='home-page1'),
    path('output1',views.output1,name='outpage1')   
]

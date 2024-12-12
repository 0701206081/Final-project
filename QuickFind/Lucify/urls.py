from django.urls import path 
from . import views

app_name = 'Lucify'


urlpatterns = [
    path('',views.index,name='index'),
    # path('contact/', views.contact_view, name='contact'),
    path('business/', views.business_list, name='business_list'),
    path('open/', views.business_detail, name='business_detail'),
    
]















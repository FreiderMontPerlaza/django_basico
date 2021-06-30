

from django.urls import path
from . import views 

urlpatterns = [
    path('',views.home),
    path('galeria/',views.galeria),
    path('product/',views.product),
    path('contact/',views.contact),

   


]
#*******ROUTING STEPS*********
#In this way you will be able to add paths that will render pages to the user.
#Fot this you have to import (in this case home function)the function from the view module .
#In this case it will call the the home function.
#The same variable can take in the different pages to be displayed.
#It will in then be taken as a parameter to the path function.

from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='blog-home'),
    path('about/', views.about, name='blog-about')
]

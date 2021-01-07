from django.shortcuts import render
from django.http import HttpResponse
from .models import Post

# Create your views here.


#***TEMPLATE ADDITION STEPS****
#Here you create a page to be displayed. For this you must render an HTML file.
#HTML, XML, IMAGES and other Files can be returned as HTTP response.
#STEPS
#-----
#STEP 1:For this you will have to create an HTML file in the app folder. 
#STEP 2:In this case the folder is called Templates.
#STEP 3:The template must be saved as an HTML file. --> In this case the 'Home.html'
#STEP 4:Create a function with the render method imported from 'django.shortcuts'
#STEP 5:Pass in the request and the 'blog/Home.html' as a string.
#STEP 6:Check 'APPS.PY' for further steps. 



def home(request):
    context = {
        'posts': Post.objects.all()
    }
    return render(request, 'blog/Home.html', context)

def about(request):
    return render(request, 'blog/About.html')

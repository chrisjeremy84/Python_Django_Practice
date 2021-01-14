from django.shortcuts import render, get_object_or_404
from django.views.generic import (ListView, 
                                DetailView, 
                                CreateView,
                                UpdateView,
                                DeleteView)
from django.http import HttpResponse
from django.contrib.auth.mixins import (LoginRequiredMixin,
                                        UserPassesTestMixin)
from .models import Post
from django.contrib.auth.models import User

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

"""
Here a listview is being created.
By default the PostListView looks for a template of a certain type.
And usually the template is named as  <app>/<model>_<Viewtype>.html
In this case the template would be blog/Post_ListView.html
However we can always change the template being looked for.
In the current file 'views.py' you can assign the template to 
the variable named template_name.
"""
class PostListView(ListView):
    model = Post
    template_name = 'blog/home.html' #---<app>/<model>_<viewtype>.html
    context_object_name = 'posts'
    ordering = ['-date_posted']
    paginate_by = 2


class UserPostListView(ListView):
    model = Post
    template_name = 'blog/user_posts.html' #---This will still show all posts
    context_object_name = 'posts'         #---What needs tp be done is to filter the posts for a specific user.
    ordering = ['-date_posted']
    paginate_by = 2

    def get_queryset(self) :
        user = get_object_or_404(User, username=self.kwargs.get('username'))#Gets the username pasted into the url
        return Post.objects.filter(author=user).order_by('-date_posted')#filters the posts by that user and sorts them according to time
class PostDetailView(DetailView):
    model = Post #Shows the details of the post

class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['title', 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user#Checks for current User
        return super().form_valid(form)#This runs the form after Cheking the user
    
class PostUpdateView(LoginRequiredMixin, UpdateView, UserPassesTestMixin):
    model = Post
    fields = ['title', 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user#Checks for current User
        return super().form_valid(form)#This runs the form after Cheking the user

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False


class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post #Shows the details of the post
    success_url = '/'
    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False
    
def about(request):
    return render(request, 'blog/About.html')

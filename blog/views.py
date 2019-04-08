from django.shortcuts import render,redirect,get_object_or_404,HttpResponseRedirect,HttpResponse
from .models import Post
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.
from django.views.generic import (ListView,TemplateView,CreateView
                                    ,UpdateView,DetailView,DeleteView)

from django.core.urlresolvers import reverse_lazy,reverse

class About(TemplateView):
    template_name="blog/about.html"

class PostList(ListView):
    model=Post
        
class PostCreate(LoginRequiredMixin, CreateView):
    login_url='/login'
    model=Post
    fields=('author','title','text')

class PostUpdate(UpdateView):
    model=Post
    fields=("author",'title','text')

class PostDetail(DetailView):
    context_object_name='post_detail'
    model=Post

    template_name="blog/post_detail.html"
class PostDelete(DeleteView):
    model=Post
    success_url=reverse_lazy('blog:post_list')
    
class PostDraftList(LoginRequiredMixin,ListView):
    model=Post
    def get_queryset(self):
        return Post.objects.filter(published_date__isnull=True).order_by('-created_date')


def publish_post(request,pk):
    post=get_object_or_404(Post,pk=pk)
    print(post)
    print(pk)
    post.publish()

    return redirect('blog:post_detail',pk=post.pk)
    # return HttpResponse("jdskhgjkdghdfk")
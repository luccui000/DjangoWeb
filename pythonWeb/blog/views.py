from django.shortcuts import render
from .models import Post

# Create your views here.
def postList(request):
    data_list = {'Posts' : Post.objects.all().order_by('-date')}
    return render(request, 'blog/index.html', data_list)

def postNews(request, id):
    post_news = Post.objects.get(id = id)
    return render(request, 'blog/post.html',{'post_news': post_news})
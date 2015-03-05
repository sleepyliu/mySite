from django.shortcuts import get_object_or_404,render

# Create your views here.
# from django.template import loader,Context
from django.http import HttpResponse
from django.http import Http404
from blog.models import BlogsPost


# def index(request):
#     return HttpResponse("Hello, world. You're at the blog index.")

def blog(request):
    posts = BlogsPost.objects.all()
    context = {'posts':posts}
    return render(request,'blog/blog.html',context)    
    # posts = BlogsPost.objects.order_by('-timestamp')[:5]

def detail(request, title_id):
    post = get_object_or_404(BlogsPost, pk=title_id)
    return render(request, 'blog/detail.html', {'post':post})
    # try:
    #     post = BlogsPost.objects.get(id = title_id)
    # except BlogsPost.DoesNotExist:
    #     raise Http404("Article does not exist")
    # context = {'post':post}
    # return render(request,'blog/detail.html',context)

def archive(request):
    posts = BlogsPost.objects.all()
    context = {'posts':posts}
    return render(request,'blog/archive.html',context)
    # template = loader.get_template("blog/archive.html")
    # context = Context({'posts':posts})
    # return HttpResponse(template.render(context))


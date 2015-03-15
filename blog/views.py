from django.shortcuts import get_object_or_404,render,redirect
# from django.template import loader,Context
from django.http import HttpResponse,Http404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.core.urlresolvers import reverse
from django.utils import timezone
from blog.models import BlogsPost
from blog.forms import PostForm


def index(request):
    posts = BlogsPost.objects.all()[:3]
    return render(request,'blog/index.html',{'posts':posts})


def blog(request):
    post_list = BlogsPost.objects.all()
    paginator = Paginator(post_list,4)
    page = request.GET.get('page')
    try:
        posts = paginator.page(page)
    except PageNotAnInteger: 
        # If page is not an integer, deliver first page.
        posts = paginator.page(1)
    except EmptyPage: 
        # If page is out of range (e.g. 9999), deliver last page of results.
        posts = paginator.page(paginator.num_pages)
    return render(request,'blog/blog.html',{'posts':posts})


def detail(request, pk):
    post = get_object_or_404(BlogsPost, pk = pk)
    if 'vote' in request.POST:
        post.votes += 1
        post.save()
    num = str(post.votes)
    return render(request, 'blog/detail.html',{'post':post,'num':num})


def archive(request):
    post_list = BlogsPost.objects.all()
    paginator = Paginator(post_list, 5)
    page = request.GET.get('page')
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)
    return render(request,'blog/archive.html',{'posts':posts})


def search_by_day(request):
    posts = BlogsPost.objects.filter(timestamp__day=timezone.now().day)
    if len(posts)>=1:
        return render(request,'blog/search.html',{'posts':posts})
    else:
        raise Http404("Sorry, no results")

def search_by_month(request):
    posts = BlogsPost.objects.filter(timestamp__month=timezone.now().month)
    if len(posts)>=1:
        return render(request,'blog/search.html',{'posts':posts})
    else:
        raise Http404("Sorry, no results")

def search_by_year(request):
    posts = BlogsPost.objects.filter(timestamp__year=timezone.now().year)
    if len(posts)>=1:
        return render(request,'blog/search.html',{'posts':posts})
    else:
        raise Http404("Sorry, no results")


def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            return redirect('blog:detail', pk=post.pk)
    else:
        form = PostForm()
    return render(request, 'blog/post_edit.html', {'form': form})


def post_edit(request, pk):
    post = get_object_or_404(BlogsPost, pk = pk)
    if request.method == "POST":
        form = PostForm(request.POST,instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            return redirect('blog:detail', pk=post.pk)
    else:
        form = PostForm(instance = post)
    return render(request, 'blog/post_edit.html', {'form': form})


def post_del(request, pk):
    post = get_object_or_404(BlogsPost, pk = pk)
    if post:
        post.delete()
        return redirect('blog:blog')
    posts = Blog.objects.all()
    return render(request, 'blog/blog.html', {'posts':posts})
    

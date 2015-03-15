from django.shortcuts import get_object_or_404,render,redirect
# from django.template import loader,Context
from django.http import HttpResponse,Http404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.core.urlresolvers import reverse
from django.utils import timezone
from blog.models import BlogsPost,Tag
from blog.forms import PostForm,TagForm


def index(request):
    tags = Tag.objects.all()
    posts = BlogsPost.objects.all()[:3]
    return render(request,'blog/index.html',{'posts':posts,'tags':tags})


def blog(request):
    tags = Tag.objects.all()
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
    return render(request,'blog/blog.html',{'posts':posts,'tags':tags})


def detail(request, pk):
    tags = Tag.objects.all()
    post = get_object_or_404(BlogsPost, pk = pk)
    if 'vote' in request.POST:
        post.votes += 1
        post.save()
    num = str(post.votes)
    return render(request, 'blog/detail.html',{'post':post,'num':num,'tags':tags})


def archive(request):
    tags = Tag.objects.all()
    post_list = BlogsPost.objects.all()
    paginator = Paginator(post_list, 5)
    page = request.GET.get('page')
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)
    return render(request,'blog/archive.html',{'posts':posts,'tags':tags})


def search_by_day(request):
    tags = Tag.objects.all()
    posts = BlogsPost.objects.filter(timestamp__day=timezone.now().day)
    if len(posts)>=1:
        return render(request,'blog/search.html',{'posts':posts,'tags':tags})
    else:
        raise Http404("Sorry, no results")

def search_by_month(request):
    tags = Tag.objects.all()
    posts = BlogsPost.objects.filter(timestamp__month=timezone.now().month)
    if len(posts)>=1:
        return render(request,'blog/search.html',{'posts':posts,'tags':tags})
    else:
        raise Http404("Sorry, no results")

def search_by_year(request):
    tags = Tag.objects.all()
    posts = BlogsPost.objects.filter(timestamp__year=timezone.now().year)
    if len(posts)>=1:
        return render(request,'blog/search.html',{'posts':posts,'tags':tags})
    else:
        raise Http404("Sorry, no results")


def post_new(request):
    tags = Tag.objects.all()
    if request.method == "POST":
        form = PostForm(request.POST)
        tag = TagForm(request.POST)
        if form.is_valid() and tag.is_valid():
            tagc= tag.cleaned_data
            tagname = tagc['tag_name']
            for taglist in tagname.split():
                Tag.objects.get_or_create(tag_name=taglist.strip())
            post = form.save(commit=False)
            post.save()
            for taglist in tagname.split():
                post.tags.add(Tag.objects.get(tag_name=taglist.strip()))
                post.save()
            return redirect('blog:detail', pk=post.pk)
    else:
        form = PostForm()
        tag = TagForm()
    return render(request, 'blog/post_edit.html', {'form': form,'tag': tag,'tags':tags})


def post_edit(request, pk):
    tags = Tag.objects.all()
    post = get_object_or_404(BlogsPost, pk = pk)
    if request.method == "POST":
        form = PostForm(request.POST,instance=post)
        tag = TagForm(request.POST)
        if form.is_valid() and tag.is_valid():
            tagc= tag.cleaned_data
            tagname = tagc['tag_name']
            tagnamelist = tagname.split()
            for taglist in tagnamelist:
                Tag.objects.get_or_create(tag_name=taglist.strip())
            post = form.save(commit=False)
            post.save()
            for taglist in tagnamelist:
                post.tags.add(Tag.objects.get(tag_name=taglist.strip()))
                post.save()
            tags = post.tags.all()
            for tagname in tags:
                tagname = unicode(str(tagname), "utf-8")
                if tagname not in tagnamelist:
                    notag = post.tags.get(tag_name=tagname)
                    post.tags.remove(notag)
            return redirect('blog:detail', pk=post.pk)
    else:
        form = PostForm(instance = post)
        tags = post.tags.all()
        if tags:
            taginit = ''
            for x in tags:
                taginit += str(x) + ' '
            tag = TagForm(initial={'tag_name': taginit})
        else:
            tag = TagForm()
    return render(request, 'blog/post_edit.html', {'form': form,'tag': tag,'tags':tags})


def post_del(request, pk):
    tags = Tag.objects.all()
    post = get_object_or_404(BlogsPost, pk = pk)
    if post:
        post.delete()
        return redirect('blog:blog')
    posts = Blog.objects.all()
    return render(request, 'blog/blog.html', {'posts':posts,'tags':tags})
    

def tag_filter(request,id):
    tags = Tag.objects.all()
    tag = Tag.objects.get(id = id)
    posts = tag.blogspost_set.all()
    return render(request, 'blog/tag_filter.html', {'posts':posts,'tag':tag,'tags':tags})


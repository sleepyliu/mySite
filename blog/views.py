from django.shortcuts import get_object_or_404,render

# Create your views here.
# from django.template import loader,Context
from django.http import HttpResponse
from django.http import Http404
from blog.models import BlogsPost,Favor

from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


# def index(request):
#     return HttpResponse("Hello, world. You're at the blog index.")

def blog(request):
    post_list = BlogsPost.objects.all()
    paginator = Paginator(post_list, 2)

    page = request.GET.get('page')

    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        posts = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        posts = paginator.page(paginator.num_pages)

    context = {'posts':posts}
    return render(request,'blog/blog.html',context)    
    # posts = BlogsPost.objects.order_by('-timestamp')[:5]

def detail(request, title_id):
    post = get_object_or_404(BlogsPost, pk=title_id)
    fav = post.favor_set.all()[0]
    # if len(fav) == 0:
    #     fav.like = 0
    # else:
    #     num = fav.like 
    if 's' in request.POST:
        post.favor_set.update(like = fav.like + 1)
    num = str(fav.like)
    context = {'post':post,'fav':num}
    return render(request, 'blog/detail.html',context)
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

def display_meta(request):
    values = request.META.items()
    values.sort()
    html = []
    for k, v in values:
        html.append('<tr><td>%s</td><td>%s</td></tr>' % (k, v))
    return HttpResponse('<table>%s</table>' % '\n'.join(html))

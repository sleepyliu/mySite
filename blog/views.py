from django.shortcuts import get_object_or_404,render
# from django.template import loader,Context
# from django.http import HttpResponse,Http404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from blog.models import BlogsPost


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

    # template = loader.get_template("blog/blog.html")
    # context = Context({'posts':posts})
    # return HttpResponse(template.render(context))
    context = {'posts':posts}
    return render(request,'blog/blog.html',context)


def detail(request, title_id):
    post = get_object_or_404(BlogsPost, pk = title_id)
    # try:
    #     post = BlogsPost.objects.get(id = title_id)
    # except BlogsPost.DoesNotExist:
    #     raise Http404("Article does not exist")
    if 'vote' in request.POST:
        post.votes += 1
        post.save()
    num = str(post.votes)
    context = {'post':post,'num':num}
    return render(request, 'blog/detail.html',context)


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

    context = {'posts':posts}
    return render(request,'blog/archive.html',context)


# def display_meta(request):
#     values = request.META.items()
#     values.sort()
#     html = []
#     for k, v in values:
#         html.append('<tr><td>%s</td><td>%s</td></tr>' % (k, v))
#     return HttpResponse('<table>%s</table>' % '\n'.join(html))

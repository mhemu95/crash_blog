from django.shortcuts import render
from blog.models import Post
from django.views.generic import ListView
from blog.models import Post


# def frontpage(request):
#     posts = Post.objects.filter(status=Post.Status.PUBLISHED)
#
#     return render(request, "core/frontpage.html", {'posts': posts})


class FrontpageView(ListView):
    queryset = Post.published.all()
    context_object_name = 'posts'
    # paginate_by
    template_name = 'core/frontpage.html'


def about(request):
    return render(request, "core/about.html")

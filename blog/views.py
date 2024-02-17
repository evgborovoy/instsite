from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render, get_object_or_404
from django.views.decorators.http import require_POST
from django.views.generic import ListView

from blog.forms import EmailPostForms, CommentForm
from blog.models import Post, Comment


class PostListView(ListView):
    queryset = Post.objects.all()
    context_object_name = "posts"
    paginate_by = 3
    template_name = "blog/post/list.html"


def post_list(request):
    posts = Post.published.all()
    paginator = Paginator(posts, 3)
    page_number = request.GET.get("page", 1)
    try:
        posts = paginator.page(page_number)
    except PageNotAnInteger:
        posts = paginator.page(1)

    except EmptyPage:
        posts = paginator.page(paginator.num_pages)
    return render(request, "blog/post/list.html", context={"posts": posts})


def post_detail(request, year, month, day, post):
    post = get_object_or_404(
        Post,
        status=Post.Status.PUBLISHED,
        publish__year=year,
        publish__month=month,
        publish__day=day,
        slug=post
    )
    comments = post.comments.filter(active=True)
    form = CommentForm()
    return render(request, "blog/post/detail.html", context={"post": post,
                                                             "comments": comments,
                                                             "form": form})


# def post_share(request, post_id):
#     post = get_object_or_404(Post,
#                              id=post_id,
#                              status=Post.Status.PUBLISHED
#                              )
#     if request.method == "POST":
#         form = EmailPostForms(request.POST)
#         if form.is_valid():
#             cd = form.cleaned_data
#     else:
#         form = EmailPostForms()
#     return render(request, "blog/post.share.html", context={"post": post, "form": form})

@require_POST
def post_comment(request, post_id):
    post = get_object_or_404(Post,
                             id=post_id,
                             status=Post.Status.PUBLISHED)
    comment = None
    form = CommentForm(data=request.POST)
    if form.is_valid():
        comment = form.save(commit=False)
        comment.post = post
        comment.save()
    return render(request, 'blog/post/comment.html', context={'post': post,
                                                              'form': form,
                                                              'comment': comment})

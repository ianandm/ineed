from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from .models import Post, Comment
from .forms import PostForm, CommentForm


def home(request):
    form = PostForm(request.POST, request.FILES or None)
    comment_form = CommentForm(request.POST, request.FILES or None)

    if request.method == "POST" and 'main_form' in request.POST:
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            filepath = request.FILES.get('myImage')
            if filepath is not None:
                post.myImage = filepath
            else:
                post.myImage = None
            post.save()
            return redirect('ineed-home')

    elif request.method == "POST" and 'comment_form' in request.POST:
        # comment has been added
        post_id = request.POST.get('comcomment')
        posts = Post.objects.get(id=post_id)
        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False)
            new_comment.comcomment = posts
            new_comment.comauthor = request.user
            new_comment.save()
            return redirect('ineed-home')
    else:
        form = PostForm()
        comment_form = CommentForm()
        comments = Comment.objects.order_by("-created")
        posts = Post.objects.order_by("-date_posted")

    return render(request, 'ineed/home.html', {'posts': posts, 'form': form, 'comment_form': comment_form, 'comments': comments})


def about(request):
    return render(request, 'ineed/about.html')


def providehelp(request):
    return render(request, 'ineed/providehelp.html')


def loginandregister(request):
    return render(request, 'users/register.html')


def offerings(request):
    return HttpResponse('<h1> Our Offerings </h1>')


def ineedthese(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect('ineed-these')
    else:
        form = PostForm()
    return render(request, 'ineed/ineedthese.html', {'form': form})

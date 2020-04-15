from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Post
from .forms import PostForm


def home(request):
    if request.method == "POST":
        form = PostForm(request.POST, request.FILES)
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
    else:
        form = PostForm()
        posts = Post.objects.order_by("-date_posted")

    return render(request, 'ineed/home.html', {'posts': posts, 'form': form})


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

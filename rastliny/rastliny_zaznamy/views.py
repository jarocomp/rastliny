from django.shortcuts import render
from .models import Post
from django.utils import timezone
from .forms import PostForm
from django.shortcuts import render, get_object_or_404
from django.shortcuts import redirect


def post_list(request):
    posts = Post.objects.filter(created_date__lte=timezone.now()).order_by('created_date')
    return render(request, 'rastliny_zaznamy/post_list.html', {'posts': posts})

def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)





            post.created_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm()
    return render(request, 'rastliny_zaznamy/post_edit.html', {'form': form})

def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.created_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'rastliny_zaznamy/post_edit.html', {'form': form})

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'rastliny_zaznamy/post_detail.html', {'post': post})


def skuska(request):
    if request.method == "POST":
        val = request.POST.get('name')
        values = val.split(' ')
    return render(request,'rastliny_zaznamy/skuska.html', {'val':values[0]})

def post_search(request):
    val = ''
    if request.method == "POST":
        val = request.POST.get('name')

    posts = Post.objects.filter(title__startswith=val)

    return render(request, 'rastliny_zaznamy/post_search.html', {'posts': posts})



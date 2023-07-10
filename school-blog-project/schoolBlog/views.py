from django.shortcuts import render, redirect
from .models import Post, Comment
from django.utils import timezone

# Create your views here.
def test(req):
    return render(req, 'index.html')

def index(req):
    if req.method == 'POST' and req.POST.get('title'):
        title = req.POST.get('title')
        image = req.FILES.get('image')
        content = req.POST.get('content')
        Post.objects.create(
            image=image,
            content=content,
            title=title,
            writer=req.user,
        )
    post_all = Post.objects.all()
    context = {
        'post_all': post_all
    }
    return render(req, 'index.html', context)

def detail(req, id):
    post = Post.objects.get(id=id)
    context = {
        'post': post,
    }
    return render(req, 'post_detail.html', context)

def delete(req, id):
    post = Post.objects.get(id=id)

    if req.method == 'GET':
        context = {'post': post}
        return render(req, 'post_delete.html', context)
    elif req.method == 'POST':
        post.delete()
        return redirect('index')
    
def update(req, id):
    post = Post.objects.get(id=id)

    if req.method == 'GET':
        context = {'post': post}
        return render(req, 'post_update.html', context)
    elif req.method == 'POST':
        image = req.FILES.get('image')
        content = req.POST.get('content')
        title = req.POST.get('title')
        time = timezone.now()

        if image:
            post.image.delete()
            post.image = image
        
        post.title = title
        post.content = content
        post.created_at = time
        post.save()
        context = {'post': post}
        return render(req, 'post_detail.html', context)
    
def comment(req, id):
    post = Post.objects.get(id=id)
    text = req.POST['text']
    time = timezone.now()
    Comment.objects.create(
        post=post, 
        content=text,
        created_at=time,
    )
    context = {'post': post}
    return render(req, 'post_detail.html', context)

def comment_delete(req, post_id, comment_id):
    comment = Comment.objects.get(id=comment_id)
    comment.delete()

    post = Post.objects.get(id=post_id)
    context = {'post': post}
    return render(req, 'post_detail.html', context)


from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.shortcuts import render, get_object_or_404
from django.shortcuts import redirect
from django.utils import timezone
from .models import Post, Comment, Category, CategoryBundle
from .forms import PostForm, CommentForm, CategoryForm, CategoryBundleForm


#Post actions section

def post_list(request):
    categories = get_category_list()
    bundles = get_category_bundle_list()
    posts = Post.objects.filter(published_date__isnull=False).order_by('-published_date')
    return render(request, 'blog/post_list.html', {'posts': posts, 'categories': categories, 'category_bundles': bundles})

def post_detail(request, pk):
    categories = get_category_list()
    bundles = get_category_bundle_list()
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', {'post': post, 'categories': categories, 'category_bundles': bundles})

@login_required
def post_new(request):
    categories = get_category_list()
    bundles = get_category_bundle_list()
    if request.method == "POST":
        form = PostForm(request.POST)
        if (form.is_valid):
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm()
    return render(request, 'blog/post_edit.html', {'form': form})

@login_required
def post_draft_list(request):
    categories = get_category_list()
    bundles = get_category_bundle_list()
    posts = Post.objects.filter(published_date__isnull=True).order_by('-created_date')
    return render(request, 'blog/post_draft_list.html', {'posts': posts, 'categories': categories, 'category_bundles': bundles})

@login_required
def post_publish(request, pk):
    post = get_object_or_404(Post, pk=pk)
    post.publish()
    return redirect('post_detail', pk=pk)

@login_required
def post_remove(request, pk):
    post = get_object_or_404(Post, pk=pk)
    post.delete()
    return redirect('post_list')

@login_required
def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    categories = get_category_list()
    bundles = get_category_bundle_list()
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if (form.is_valid()):
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'blog/post_edit.html', {'form': form, 'categories': categories, 'category_bundles': bundles})

#comment actions section

def add_comment_to_post(request, pk):
    post = get_object_or_404(Post, pk=pk)
    categories = get_category_list()
    bundles = get_category_bundle_list()

    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = CommentForm()
    return render(request, 'blog/add_comment_to_post.html', {'form': form, 'categories': categories, 'category_bundles': bundles})

@login_required
def comment_approve(request, pk):
    comment = get_object_or_404(Comment, pk=pk)
    comment.approve()
    return redirect('post_detail', pk=comment.post.pk)

@login_required
def comment_remove(request, pk):
    comment = get_object_or_404(Comment, pk=pk)
    comment.delete()
    return redirect('post_detail', pk=comment.post.pk)

#category actions section
@login_required
def category_new(request):
    categories = get_category_list()
    bundles = get_category_bundle_list()
    if request.method == "POST":
        form = CategoryForm(request.POST)
        if (form.is_valid):
            category = form.save(commit=False)
            category.save()
            return redirect('post_list')
    else:
        form = CategoryForm()
    return render(request, 'blog/category_edit.html',{'form': form,'categories': categories,'category_bundles': bundles})
    
@login_required
def category_bundle_new(request):
    categories = get_category_list()
    bundles = get_category_bundle_list()
    if request.method == "POST":
        form = CategoryBundleForm(request.POST)
        if (form.is_valid):
            category_bundle = form.save(commit=False)
            category_bundle.save()
            return redirect('post_list')
    else:
        form = CategoryBundleForm()
    return render(request, 'blog/category_bundle_edit.html',{'form': form,'categories': categories,'category_bundles': bundles})

@login_required
def category_edit(request, pk):
    category = get_object_or_404(Category, pk=pk)
    categories = get_category_list()
    bundles = get_category_bundle_list()
    if request.method == "POST":
        form = CategoryForm(request.POST, instance=category)
        if (form.is_valid()):
            category = form.save(commit=False)
            category.save()
            return redirect('post_list')
    else:
        form = CategoryForm(instance=category)
    return render(request, 'blog/category_edit.html', {'is_update':True,'form': form, 'categories': categories, 'category_bundles': bundles})

@login_required
def category_bundle_edit(request, pk):
    category_bundle = get_object_or_404(CategoryBundle, pk=pk)
    categories = get_category_list()
    bundles = get_category_bundle_list()
    if request.method == "POST":
        form = CategoryBundleForm(request.POST, instance=category_bundle)
        if (form.is_valid()):
            category_bundle = form.save(commit=False)
            category_bundle.save()
            return redirect('post_list')
    else:
        form = CategoryBundleForm(instance=category_bundle)
    return render(request, 'blog/category_bundle_edit.html', {'is_update':True,'form': form, 'categories': categories, 'category_bundles': bundles})

@login_required
def category_remove(request, pk):
    category = get_object_or_404(Category, pk=pk)
    category.delete()
    return redirect('post_list')

@login_required
def category_bundle_remove(request, pk):
    category_bundle = get_object_or_404(CategoryBundle, pk=pk)
    category_bundle.delete()
    return redirect('post_list')

def category_list(request):
    categories = get_category_list()
    bundles = get_category_bundle_list()
    return render(request, 'blog/category_list.html', {'categories': categories, 'category_bundles': bundles})

def get_category_list():
    categories = list(Category.objects.order_by('created_date'))
    return categories

def get_category_bundle_list():
    bundles = list(CategoryBundle.objects.order_by('created_date'))
    return bundles

def category_posts(request, pk):
    categories = get_category_list()
    bundles = get_category_bundle_list()
    category = get_object_or_404(Category, pk=pk)
    posts = Post.objects.filter(category=category,published_date__isnull=False).order_by('-published_date')
    return render(request, 'blog/post_list.html', {'categories': categories, 'category_bundles': bundles, 'posts': posts})
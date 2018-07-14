from django.contrib.auth.decorators import login_required

from django.shortcuts import get_object_or_404, render, redirect

from django.http import HttpResponse, Http404

from django.views.generic.detail import DetailView


from posts.models import Post
from .forms import PostForm

# Create your views here.





class PostDetailView(DetailView):

	model = Post

def index(request):
	latest_post_list = Post.objects.order_by('-pub_date')[:5]
	context = {
	    'latest_post_list': latest_post_list,
	}
	
	return render(request, 'posts/index.html', context)

def home(request):
	latest_post_list = Post.objects.order_by('-pub_date')[:5]
	context = {
	    'latest_post_list': latest_post_list,
	}
	
	return render(request, 'home.html', context)
	

	


def create_posts(request):
	form = PostForm(request.POST or None)

	if form.is_valid():
		form.save()
		return redirect('home')

	return render(request, 'posts-form.html', {'form': form})


def update_post(request, id):
	post = Post.objects.get(id=id)
	form = PostForm(request.POST or None, instance=post)

	if form.is_valid():
		form.save()
		return redirect('home')
	return render(request, 'posts-form.html', {'form': form, 'post': post})

def delete_post(request, id):
	post = Post.objects.get(id=id)

	if request.method == 'POST':
		post.delete()
		return redirect('home')
	return render(request, 'post-delete-confirm.html', {'post': post})




#def detail(request, post_id):
	#post = get_object_or_404(Post, pk=post_id)
#	return render(request, 'posts/detail.html', {'post': post})


def about(request):
    return render(request, 'about.html', {})


def privacy(request):
	return render(request, 'privacy.html', {})

#def contact(request):
	#return render(request, 'contact.html', {})

def terms(request):
	return render(request, 'terms.html', {})

@login_required
def userProfile(request):
	user = request.user
	context = {'user': user}
	return render(request, 'profile.html', context)
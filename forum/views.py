from django.shortcuts import render, redirect
from .models import Post, Comment
from .forms import PostForm, CommentForm
from django.core.paginator import Paginator
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.urls import reverse_lazy

def posts(request):
    forum_posts = {'posts': Post.objects.all(), 'title': 'Forum posts'}
    return render(request, 'forum/forum.html', forum_posts)


class PostListView(ListView):
    model = Post
    template_name = 'forum/forum.html'
    context_object_name = 'posts'
    ordering = ['-timesubmitted']
    paginate_by = 5

class PostDetailView(DetailView):
    model = Post
    template_name = 'forum/post_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        post = self.get_object()
        comments = post.comments.all()  

        paginator = Paginator(comments, 10)  
        page_number = self.request.GET.get('page')
        comment_page = paginator.get_page(page_number)

        context['comment_form'] = CommentForm() 
        context['comment_page'] = comment_page
        return context

class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    form_class = PostForm

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)
    
class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    form_class = PostForm

    def test_func(self):
        post = self.get_object()
        return self.request.user == post.user

class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    success_url = '/forums/posts'

    def test_func(self):
        post = self.get_object()
        return self.request.user == post.user

class CommentCreateView(CreateView):
    template_name = 'forum/post_detail.html'
    form_class = CommentForm

    def form_valid(self, form):
        post_id = self.kwargs['pk']  
        comment = form.save(commit=False)
        comment.post_id = post_id  
        comment.usercomment = self.request.user  
        comment.save()
        return redirect('forums:post-detail', pk=post_id)
    
class CommentDeleteView(DeleteView):
    model = Comment
    template_name = 'forum/comment_confirm_delete.html'

    def get_success_url(self):
        post = self.object.post
        return reverse_lazy('forums:post-detail', kwargs={'pk': post.pk})
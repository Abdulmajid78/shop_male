from django.shortcuts import render, reverse, get_object_or_404
from .models import BlogModel, BlogTagsModel
from django.views.generic import ListView, CreateView, DetailView
from .forms import CommentForm


class BlogListView(ListView):
    template_name = 'blog.html'
    paginate_by = 6

    def get_queryset(self):
        qs = BlogModel.objects.all()
        tag = self.request.GET.get('tag', '')
        if tag:
            qs = qs.filter(tags=tag)

        return qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        tag = self.request.GET.get('tag', '')
        if tag:
            context['tag'] = get_object_or_404(BlogTagsModel, pk=tag)

        return context



class BlogDetailView(DetailView):
    template_name = 'blog-details.html'
    model = BlogModel

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['comment_form'] = CommentForm()
        return context


class CommentCreateView(CreateView):
    form_class = CommentForm
    template_name = 'blog-details.html'

    def form_valid(self, form):
        blog = get_object_or_404(BlogModel, pk=self.kwargs.get('pk'))
        form.instance.blog = blog
        form.instance.save()
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('blogs:detail', kwargs={'pk': self.kwargs.get('pk')})

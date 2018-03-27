# -*- coding: utf-8 -*-
from django.contrib.messages.views import SuccessMessageMixin
from django.views.generic import DetailView, ListView, CreateView

from blog.forms import PostForm
from blog.models import PostModel


class PostDetailView(DetailView):
    template_name = "blog/post.html"
    model = PostModel
    context_object_name = "post"
    slug_field = "title"


class PostListView(ListView):
    template_name = "blog/index.html"
    model = PostModel
    queryset = PostModel.objects.all()
    context_object_name = "posts"
    allow_empty = True
    paginate_orphans = 10
    page_kwarg = "p"

    def get_context_data(self, **kwargs):
        context = super(PostListView, self).get_context_data(**kwargs)
        context['search'] = self.request.GET.get('q', '')

        if context['search']:
            # TODO: сделать поиск по нескольким полям в стиле SQL-конструкции `LIKE`
            self.queryset = PostModel.objects.filter(title__icontains=context['search'])
        else:
            self.queryset = PostModel.objects.all()
        context[self.context_object_name] = self.queryset
        return context


class PostCreateView(SuccessMessageMixin, CreateView):
    template_name = "blog/upload.html"
    model = PostModel
    form = None
    fields = ["title", "entry", "content"]
    success_url = "../"
    success_message = u"Article \"<a href=\"{href}\">{title}</a>\" created!"

    def get_success_message(self, cleaned_data):
        post = PostModel.objects.get(**cleaned_data)
        return self.success_message.format(href=post.getUrl(), title=cleaned_data['title'])

    def get_context_data(self, **kwargs):
        context = super(PostCreateView, self).get_context_data(**kwargs)
        context["form"] = self.form
        return context

    def get(self, request, *args, **kwargs):
        self.form = PostForm()
        return super(PostCreateView, self).get(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        self.form = PostForm(request.POST)
        return super(PostCreateView, self).post(request, *args, **kwargs)

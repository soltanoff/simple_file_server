# -*- coding: utf-8 -*-
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.messages import add_message
from django.http import Http404
from django.shortcuts import redirect
from django.utils.translation import gettext as _
from django.views.decorators.csrf import csrf_protect
from django.views.generic import DetailView, ListView, CreateView, UpdateView

from blog.generic.mixins import TagMixin
from blog.generic.views import BasePostView
from blog.models import PostModel


# TODO: soltanoff: use the thumbnails for article, add new field to the PostModel: `icon`


class PostCreateView(BasePostView, CreateView):
    template_name = "blog/upload.html"
    success_message = _(u"Article \"<a href=\"{href}\">{title}</a>\" created!")


class PostUpdateView(BasePostView, UpdateView):
    template_name = "blog/edit.html"
    success_message = _(u"Article \"<a href=\"{href}\">{title}</a>\" updated!")


class PostDetailView(TagMixin, DetailView):
    template_name = "blog/post.html"
    model = PostModel
    context_object_name = "post"
    slug_field = "title"


# TODO: soltanoff: use paginator
class PostListView(TagMixin, ListView):
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


@csrf_protect
@login_required
def remove(request, post_id):
    if request.user.is_active and request.user.is_staff:
        post = PostModel.objects.get(id=post_id)
        post.delete()
        add_message(
            request,
            messages.WARNING,
            _("Post \"<b>{title}</b>\" is removed!").format(title=post.title)
        )
        return redirect("/")
    else:
        raise Http404

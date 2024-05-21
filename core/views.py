from django.http import HttpResponse
from datetime import datetime

from django.shortcuts import render
from django.views.generic import TemplateView, ListView, RedirectView
from core import models


def index(request):
    return render(request, 'core/index.html')


class ClassBasedIndex(TemplateView):
    template_name = 'core/index.html'

    def get_context_data(self, **kwargs):
        contex = super().get_context_data(**kwargs)
        from django.utils.timezone import now
        contex["additional_info"] = now()
        return contex


class Userlist(ListView):
    model = models.User
    context_object_name = "user"
    template_name = 'core/user_list.html'


class Postlist(ListView):
    model = models.Post
    context_object_name = "post"
    template_name = 'core/_list.html'


class Redirect(RedirectView):
    query_string = True
    url = 'https://www.youtube.com/watch?v=dQw4w9WgXcQ&pp=ygUYTmV2ZXIgR29ubmEgR2l2ZSBZb3UgVXAu'


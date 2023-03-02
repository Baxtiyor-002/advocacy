from django.http import request
from django.shortcuts import get_object_or_404
from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView
from .models import Initiative, Comment
from django.views.generic.base import View
from django.http import HttpResponseRedirect
from django.urls import reverse

from .forms import CommentForm
# Create your views here.


def InitiativeLike(request, pk):
    post = get_object_or_404(Initiative, id=request.POST.get('initiative_id'))
    if post.likes.filter(id=request.user.id).exists():
        post.likes.remove(request.user)
    else:
        post.likes.add(request.user)

    return HttpResponseRedirect(reverse('initiative_detail', args=[str(pk)]))

class HomePageView(ListView):
    model = Initiative
    template_name = 'home.html'


class InitiativeDetailView(DetailView):
    model = Initiative
    template_name = 'initiative_detail.html'

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)

        likes_connected = get_object_or_404(Initiative, id=self.kwargs['pk'])
        liked = False
        if likes_connected.likes.filter(id=self.request.user.id).exists():
            liked = True
        data['number_of_likes'] = likes_connected.number_of_likes()
        data['post_is_liked'] = liked
        return data


class Comment(View):

    def post(self, request, pk):
        form = CommentForm(request.POST)
        if form.is_valid():
            form = form.save(commit=False)
            form.initiative_id = pk
            form.save()
        return redirect("/")

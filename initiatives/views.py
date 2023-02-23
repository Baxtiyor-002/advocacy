from django.http import request
from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView
from .models import Initiative, Comment
from django.views.generic.base import View

from .forms import CommentForm
# Create your views here.

class HomePageView(ListView):
    model = Initiative
    template_name = 'home.html'


class InitiativeDetailView(DetailView):
    model = Initiative
    template_name = 'initiative_detail.html'
    # queryset = Initiative.objects.filter(comments__draft=False)

    # def get_queryset(self):
    #     return Initiative.objects.filter(comments__draft=True)

# class InitiativeDetailView(DetailView):
#     model1 = Initiative
#     model2 = Comment
#     template = 'initiative_detail.html'
#     context = {}
#
#     def get(self, *args, **kwargs):
#         self.context = {
#             'initiative': self.model1.objects.all(),
#             'comments': self.model2.objects.all()
#         }
#         return(render(request, self.template, self.context))


class Comment(View):

    def post(self, request, pk):
        form = CommentForm(request.POST)
        if form.is_valid():
            form = form.save(commit=False)
            form.initiative_id = pk
            form.save()
        return redirect("/")

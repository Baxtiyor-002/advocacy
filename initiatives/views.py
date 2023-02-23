from django.http import request
from django.shortcuts import render
from django.views.generic import ListView, DetailView,View
from .models import Initiative, Comment


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

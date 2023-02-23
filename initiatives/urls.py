from django.urls import path
from . import views


from .views import HomePageView, InitiativeDetailView

urlpatterns = [
    path('<int:pk>/', InitiativeDetailView.as_view(), name='initiative_detail'),
    path('', HomePageView.as_view(), name='home.html'),
    path('comment/<int:pk>/', views.Comment.as_view(), name="add_comment"),
]
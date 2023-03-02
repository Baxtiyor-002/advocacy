from django.urls import path
from . import views


from .views import HomePageView, InitiativeDetailView, InitiativeLike

urlpatterns = [
    path('<int:pk>/', InitiativeDetailView.as_view(), name='initiative_detail'),
    path('', HomePageView.as_view(), name='home.html'),
    path('initiative-like/<int:pk>', views.InitiativeLike, name="initiative_like"),
    path('comment/<int:pk>/', views.Comment.as_view(), name="add_comment"),
]
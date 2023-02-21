from django.urls import path



from .views import HomePageView, InitiativeDetailView

urlpatterns = [
    path('<int:pk>/', InitiativeDetailView.as_view(), name='initiative_detail'),
    path('', HomePageView.as_view(), name='home.html'),
]
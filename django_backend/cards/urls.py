
from django.urls import path
from .views import CardCreateView, CardDeleteView

urlpatterns = [
    path('cards/', CardCreateView.as_view()),
    path('cards/<int:pk>/', CardDeleteView.as_view()),
]
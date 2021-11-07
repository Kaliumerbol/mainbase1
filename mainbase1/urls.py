from django.urls import path
from .views import Mainbase1ListCreateView, Mainbase1DetailUpdateDestroy
urlpatterns = [
    path('', Mainbase1ListCreateView.as_view()),
    path('<int:id>', Mainbase1DetailUpdateDestroy.as_view()),
]
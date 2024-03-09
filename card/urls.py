from django.urls import path
from . import views

urlpatterns = [
    path('self/', views.dispatcher),
    path('<int:cardId>', views.carddetail),
]

from django.urls import path
from . import views

urlpatterns = [
    path('get', views.send_questions),
    path('add', views.add_question),
    path('score', views.calculate_score)
]
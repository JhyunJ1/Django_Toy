from django.urls import path
from . import views

urlpatterns = [
    # Generic view에 의해 pk라고 설정
    path("/", views.OrderListView.as_view()),
    path("/<int:pk>", views.OrderDetailView().as_view()),
    path("/<int:pk>/comment", views.CommentListView().as_view()),
    path("/comment", views.CommentCreateView().as_view()),
]   

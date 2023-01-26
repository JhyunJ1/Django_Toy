from django.urls import path
from member import views

urlpatterns = [
    path("", views.CreateMember.as_view()),
    path("/password", views.ChangePassword.as_view()),
]

from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import status
from rest_framework import mixins, generics

from .models import Member
from .serializers import CreateMemberSerializer

# Create your views here.

class CreateMember(
    mixins.CreateModelMixin,
    generics.GenericAPIView
):
    serializer_class = CreateMemberSerializer

    def get_queryset(self):
        return Member.objects.all()
    
    def post(self, request, *args, **kwargs):
        return self.create(request, args, kwargs)


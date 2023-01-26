from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import status
from rest_framework import mixins, generics
from rest_framework.views import APIView

from django.contrib.auth.hashers import check_password

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

class ChangePassword(
    APIView
):

    def put(self, request, *args, **kwargs):
        username = request.data.get('username')
        currentpassword = request.data.get('currentpassword')
        password = request.data.get('password')
        passwordcheck = request.data.get('passwordcheck')

        if password != passwordcheck:
            return Response({
                'detail':'Different password'
            }, status=status.HTTP_400_BAD_REQUEST)

        if not Member.objects.filter(username=username).exists():
            return Response({
                'detail':'No account'
            }, status=status.HTTP_404_NOT_FOUND)
        
        member = Member.objects.get(username=username)

        if check_password(currentpassword, member.password):
            return Response({
                'detail':'Wrong Password'
            }, status=status.HTTP_400_BAD_REQUEST)
        
        member.password = make_password(password)
        member.save()

        return Response(status=status.HTTP_200_OK)




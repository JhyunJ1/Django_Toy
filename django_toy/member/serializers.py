from rest_framework import serializers
from django.contrib.auth.hashers import make_password
from .models import Member


class CreateMemberSerializer(serializers.ModelSerializer):
    def validate(self, attrs):
        if len(attrs['password']) < 8:
            raise serializers.ValidationError('Too short password')
    
        
        attrs['password'] = make_password(attrs['password'])
        
        return attrs
    
    class Meta:
        model = Member
        fields = ('id', 'username', 'tel', 'password')
        extra_kwargs = {
            'id' : {
                'read_only': True,
            },
            'password' : {
                'write_only': True,
            },
        }
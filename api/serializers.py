from rest_framework import serializers
from .models import User, Profile
from django.contrib.auth.password_validation import validate_password
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer



class UserSerializer(serializers.Serializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email']

class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
    
        token = super().get_token(user)
        
        token['full_name'] = user.profile.full_name
        token['username'] = user.username
        token['email'] = user.email
        token['bio'] = user.profile.bio
        token['image'] = user.profile.image
        token['varified'] = user.profile.verified
        
        return token
    
class RegisterSerializer(serializers.Serializer):
    password = serializers.CharField(write_only=True, required=True, validators = [validate_password])
    password2 = serializers.CharField(write_only=True, required=True)
    
    class Meta:
        model = User
        fields = ['email', 'username', 'password', 'password2']
        
        def validate(self, attrs):
            if attrs['password'] != attrs('password2'):
                serializers.ValidationError(
                    {'password':"Password do not match"}
                )
                return attrs
            
        def create(self, validate_data):
            user = User.objects.create(
                username = validate_data['username'],
                email = validate_data['email']
            )
            user.set_password(validate_data['password'])
            user.save()
            
            return user    
        
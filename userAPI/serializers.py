from rest_framework import serializers
from django.contrib.auth.models import User

class UserRegSerializer(serializers.ModelSerializer):
    password2 = serializers.CharField(write_only=True)
    class Meta:
        model = User
        fields = ['username', 'email', 'password', 'password2']
        extra_kwargs = {
            'password': {'write_only': True}
        }

    def save(self):
        username = self.validated_data['username']
        email = self.validated_data['email']
        password1 = self.validated_data['password']
        password2 = self.validated_data['password2']

        if password1 != password2:
            raise serializers.ValidationError({'error': 'Passwords must match.'})
        if User.objects.filter(email=email).exists():
            raise serializers.ValidationError({'error': 'Email already exists.'})
            
        account = User(username=username, email=email)
        account.set_password(password1)
        account.save()

        return account
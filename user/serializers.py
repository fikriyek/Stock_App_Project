from rest_framework import serializers
from rest_framework.validators import UniqueValidator  # for unique property

from django.contrib.auth.models import User

class RegisterSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(required=True, 
                                   validators=[UniqueValidator(queryset=User.objects.all())])
    
    password = serializers.CharField(write_only=True)
    password2 = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = User
        fields = (
            'id',
            'username',
            'first_name',
            'last_name',
            'email',
            'password',
            'password2',
        )

    def validate(self, data):
        if data['password'] != data['password2']:
            raise serializers.ValidationError({
                'message': 'Password fields did not match!'
            })
        return data
    
    def create(self, validated_data):
        # password2 was deleted
        validated_data.pop('password2')
        # password was deleted temporarily
        password = validated_data.pop('password')
        # user with first name, last name and email information was created
        user = User.objects.create(**validated_data)
        # password was added to information of user
        user.set_password(password)
        # save user
        user.save()

        return user

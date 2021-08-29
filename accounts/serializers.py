from django.contrib.auth import authenticate, get_user_model
from rest_framework import serializers
from .models import Account
from django.utils.translation import ugettext_lazy as _


class AccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = ('email', 'username')
        read_onlyfields = ('email', 'username')


class RegisterSerializer(serializers.ModelSerializer):

    class Meta:
        model = Account
        fields = ("email", "username", "password")
        extra_kwargs = {
            'password': {
                'write_only': True,
                'min_length': 8,
                'style': {
                    'input_type': 'password'
                }
            }
        }

    def create(self, validated_data):
        return get_user_model().objects.create_user(**validated_data)

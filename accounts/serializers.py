from rest_framework import serializers
from .models import Account


class AccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = ('email', 'username')
        read_onlyfields = ('email', 'username')


class RegisterSerializer(serializers.ModelSerializer):
    password2 = serializers.CharField(write_only=True, style={
                                      'input_type': "password"})

    class Meta:
        model = Account
        fields = ("email", "username", "password", "password2")
        extra_kwargs = {
            'password': {
                'write_only': True,
                'min_length': 8,
                'style': {
                    'input_type': 'password'
                }
            }
        }

    def save(self):
        account = Account(
            email=self.validated_data["email"], username=self.validated_data["username"])
        password = self.validated_data['password']
        password2 = self.validated_data['password2']
        # Check password and password2 are equal
        if not (password == password2):
            raise serializers.ValidationError(
                "Mismatch of passwords")

        account.set_password(password)
        account.save()
        return account

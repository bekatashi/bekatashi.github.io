from rest_framework import serializers
from django.contrib.auth import get_user_model

CustomUser = get_user_model()


class RegistrationSerializer(serializers.ModelSerializer):
    password2 = serializers.CharField(min_length=8, required=True, write_only=True)

    class Meta:
        model = CustomUser
        fields = ('email', 'password', 'password2',)

    def validate(self, attrs):
        password2 = attrs.pop('password2')
        if attrs['password'] != password2:
            raise serializers.ValidationError('Passwords didn\'t match please try again')
        if not password2.isalnum():
            raise serializers.ValidationError('Password should contain letters and nums')
        return attrs

    def create(self, validated_data):
        user = CustomUser.objects.create_user(**validated_data)

        return user


class UserDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ('email', 'first_name', 'password', 'password2', ' last_name',)


class SuperUserCreateSerializer(serializers.ModelSerializer):
    password2 = serializers.CharField(min_length=4, required=True, write_only=True)

    class Meta:
        model = CustomUser
        fields = ('email', 'password', 'password2',)

    def validate(self, attrs):
        password2 = attrs.pop('password2')
        if attrs['password'] != password2:
            raise serializers.ValidationError('Passwords didn\'t match please try again')
        if not password2.isalnum():
            raise serializers.ValidationError('Password should contain letters and nums')
        return attrs

    def create(self, validated_data):
        user = CustomUser.objects.create_superuser(**validated_data)

        return user

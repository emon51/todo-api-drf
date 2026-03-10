import pytest
from apps.users.serializers import RegisterSerializer


@pytest.mark.django_db
class TestRegisterSerializer:

    def test_valid_data(self):
        data = {"name": "John", "email": "john@example.com", "password": "secret123"}
        serializer = RegisterSerializer(data=data)
        assert serializer.is_valid()

    def test_missing_email(self):
        data = {"name": "John", "password": "secret123"}
        serializer = RegisterSerializer(data=data)
        assert not serializer.is_valid()
        assert "email" in serializer.errors

    def test_missing_password(self):
        data = {"name": "John", "email": "john@example.com"}
        serializer = RegisterSerializer(data=data)
        assert not serializer.is_valid()
        assert "password" in serializer.errors

    def test_password_too_short(self):
        data = {"name": "John", "email": "john@example.com", "password": "123"}
        serializer = RegisterSerializer(data=data)
        assert not serializer.is_valid()
        assert "password" in serializer.errors

    def test_duplicate_email(self, user):
        data = {"name": "John", "email": "test@example.com", "password": "secret123"}
        serializer = RegisterSerializer(data=data)
        assert not serializer.is_valid()
        assert "email" in serializer.errors

    def test_email_normalized(self):
        data = {"name": "John", "email": "JOHN@EXAMPLE.COM", "password": "secret123"}
        serializer = RegisterSerializer(data=data)
        assert serializer.is_valid()
        assert serializer.validated_data["email"] == "john@example.com"
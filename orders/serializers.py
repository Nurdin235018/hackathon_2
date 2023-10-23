from rest_framework import serializers
from .models import Order
from django.contrib.auth import get_user_model
from .utils import send_order_email


class OrderSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source='user.name')

    class Meta:
        model = Order
        fields = '__all__'

    def create(self, validated_data):
        request = self.context.get('request')
        validated_data['user'] = request.user
        instance = super().create(validated_data)
        instance.create_activation_code()
        send_order_email(request.user.email, instance.activation_code, request.user.name)
        return instance


User = get_user_model()


class OrderConfirmSerializer(serializers.Serializer):
    email = serializers.CharField(required=True)
    code = serializers.CharField(required=True)

    def validate(self, attrs):
        email = attrs.get('email')
        code = attrs.get('code')
        if not User.objects.filter(email=email, activation_code=code).exists():
            raise serializers.ValidationError('User didn\'t found')
        return attrs

    def activate(self):
        email = self.validated_data.get('email')
        user = User.objects.get(email=email)
        user.is_active = True
        user.activation_code = ''
        user.save()


from rest_framework import serializers
from ..models import Cliente, Conta


class ClienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cliente
        fields = "__all__"


class ContaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Conta
        fields = "__all__"

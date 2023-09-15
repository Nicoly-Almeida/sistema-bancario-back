from rest_framework import viewsets

from rest_framework.decorators import action
from rest_framework.response import Response

from . import serializers
from .. import models

from decimal import Decimal

from rest_framework.pagination import PageNumberPagination


class CustomPageNumberPagination(PageNumberPagination):
    page_size_query_param = "pageSize"

    def get_paginated_response(self, data):
        return Response(data)


class ClienteViewSet(viewsets.ModelViewSet):
    queryset = models.Cliente.objects.all()
    serializer_class = serializers.ClienteSerializer
    pagination_class = CustomPageNumberPagination


class ContaViewSet(viewsets.ModelViewSet):
    queryset = models.Conta.objects.all()
    serializer_class = serializers.ContaSerializer
    pagination_class = CustomPageNumberPagination

    @action(detail=True, methods=["post"])
    def deposito(self, request, pk=None):
        valor = request.data.get("valor")
        if not valor:
            return Response({"error": "Informe o valor do depósito."}, status=400)

        try:
            valor = Decimal(valor)
        except ValueError:
            return Response(
                {"error": "O valor do depósito deve ser um número válido."}, status=400
            )

        conta = self.get_object()
        conta.saldo += valor
        conta.save()

        return Response({"message": "Depósito realizado com sucesso."}, status=200)

    @action(detail=True, methods=["post"])
    def saque(self, request, pk=None):
        valor = request.data.get("valor")
        if not valor:
            return Response({"error": "Informe o valor do saque."}, status=400)

        try:
            valor = Decimal(valor)
        except ValueError:
            return Response(
                {"error": "O valor do saque deve ser um número válido."}, status=400
            )

        conta = self.get_object()

        if conta.saldo < valor:
            return Response(
                {"error": "Saldo insuficiente para realizar o saque."}, status=400
            )

        conta.saldo -= valor
        conta.save()

        return Response({"message": "Saque realizado com sucesso."}, status=200)

    @action(detail=True, methods=["post"])
    def transferencia(self, request, pk=None):
        valor = request.data.get("valor")
        conta_destino_pk = request.data.get("conta_destino")

        if not valor or not conta_destino_pk:
            return Response(
                {"error": "Informe o valor e a conta de destino para a transferência."},
                status=400,
            )

        try:
            valor = Decimal(valor)
        except ValueError:
            return Response(
                {"error": "O valor da transferência deve ser um número válido."},
                status=400,
            )

        conta_origem = self.get_object()
        conta_destino = models.Conta.objects.get(pk=conta_destino_pk)

        if conta_origem.saldo < valor:
            return Response(
                {"error": "Saldo insuficiente para realizar a transferência."},
                status=400,
            )

        conta_origem.saldo -= valor
        conta_destino.saldo += valor

        conta_origem.save()
        conta_destino.save()

        return Response({"message": "Transferência realizada com sucesso."}, status=200)

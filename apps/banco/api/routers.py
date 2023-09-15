from rest_framework import routers

from . import viewsets

router = routers.DefaultRouter()

router.register(r"clientes", viewsets.ClienteViewSet, basename="api-clientes")
router.register(r"contas", viewsets.ContaViewSet, basename="api-contas")

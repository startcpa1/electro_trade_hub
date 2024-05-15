from rest_framework import generics

from networks.models import Factory, RetailNetwork, IndividualEntrepreneur
from networks.permissions import IsActive
from networks.serializers import FactorySupplierSerializer, EntrepreneurSupplierSerializer, \
    RetailSupplierSerializer


class FactoryListAPIView(generics.ListAPIView):
    """Список заводских поставщиков (GET)"""
    serializer_class = FactorySupplierSerializer
    queryset = Factory.objects.all()
    permission_classes = [IsActive]


class FactoryCreateAPIView(generics.CreateAPIView):
    """Создание нового заводского поставщика (POST)"""
    serializer_class = FactorySupplierSerializer
    queryset = Factory.objects.all()
    permission_classes = [IsActive]


class FactoryUpdateAPIView(generics.UpdateAPIView):
    """Обновление информации о заводском поставщике (PUT, PATCH)"""
    serializer_class = FactorySupplierSerializer
    queryset = Factory.objects.all()
    permission_classes = [IsActive]


class FactoryDetailView(generics.RetrieveAPIView):
    """Просмотр деталей заводского поставщика (GET)"""
    serializer_class = FactorySupplierSerializer
    queryset = Factory.objects.all()
    permission_classes = [IsActive]


class FactoryDeleteAPIView(generics.DestroyAPIView):
    """Удаление заводского поставщика (DELETE)"""
    serializer_class = FactorySupplierSerializer
    queryset = Factory.objects.all()
    permission_classes = [IsActive]


class RetailListAPIView(generics.ListAPIView):
    """Список поставщиков розничной сети (GET)"""
    serializer_class = RetailSupplierSerializer
    queryset = RetailNetwork.objects.all()
    permission_classes = [IsActive]


class RetailCreateAPIView(generics.CreateAPIView):
    """Создание нового поставщика розничной сети (POST)"""
    serializer_class = RetailSupplierSerializer
    queryset = RetailNetwork.objects.all()
    permission_classes = [IsActive]


class RetailUpdateAPIView(generics.UpdateAPIView):
    """Обновление информации о розничном поставщике (PUT, PATCH)"""
    serializer_class = RetailSupplierSerializer
    queryset = RetailNetwork.objects.all()
    permission_classes = [IsActive]


class RetailDetailView(generics.RetrieveAPIView):
    """Просмотр деталей розничного поставщика (GET)"""
    serializer_class = RetailSupplierSerializer
    queryset = RetailNetwork.objects.all()
    permission_classes = [IsActive]


class RetailDeleteAPIView(generics.DestroyAPIView):
    """Удаление поставщика розничной сети (DELETE)"""
    serializer_class = RetailSupplierSerializer
    queryset = RetailNetwork.objects.all()
    permission_classes = [IsActive]


class EntrepreneurListAPIView(generics.ListAPIView):
    """Список поставщиков ИП (GET)"""
    serializer_class = EntrepreneurSupplierSerializer
    queryset = IndividualEntrepreneur.objects.all()
    permission_classes = [IsActive]


class EntrepreneurCreateAPIView(generics.CreateAPIView):
    """Создание нового поставщика ИП (POST)"""
    serializer_class = EntrepreneurSupplierSerializer
    queryset = IndividualEntrepreneur.objects.all()
    permission_classes = [IsActive]


class EntrepreneurUpdateAPIView(generics.UpdateAPIView):
    """Обновление информации о поставщике ИП (PUT, PATCH)"""
    serializer_class = EntrepreneurSupplierSerializer
    queryset = IndividualEntrepreneur.objects.all()
    permission_classes = [IsActive]


class EntrepreneurDetailView(generics.RetrieveAPIView):
    """Просмотр деталей поставщика ИП (GET)"""
    serializer_class = EntrepreneurSupplierSerializer
    queryset = IndividualEntrepreneur.objects.all()
    permission_classes = [IsActive]


class EntrepreneurDeleteAPIView(generics.DestroyAPIView):
    """Удаление поставщика ИП (DELETE)"""
    serializer_class = EntrepreneurSupplierSerializer
    queryset = IndividualEntrepreneur.objects.all()
    permission_classes = [IsActive]

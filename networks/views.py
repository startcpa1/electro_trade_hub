from rest_framework import generics, status
from rest_framework.response import Response

from networks.models import Factory, RetailNetwork, IndividualEntrepreneur
from users.permissions import UserIsActive
from networks.serializers import FactorySupplierSerializer, EntrepreneurSupplierSerializer, \
    RetailSupplierSerializer


class FactoryListAPIView(generics.ListAPIView):
    """Список заводских поставщиков (GET)"""
    serializer_class = FactorySupplierSerializer
    queryset = Factory.objects.all()
    permission_classes = [UserIsActive]


class FactoryCreateAPIView(generics.CreateAPIView):
    """Создание нового заводского поставщика (POST)"""
    serializer_class = FactorySupplierSerializer
    queryset = Factory.objects.all()
    permission_classes = [UserIsActive]


class FactoryUpdateAPIView(generics.UpdateAPIView):
    """Обновление информации о заводском поставщике (PUT, PATCH)"""
    serializer_class = FactorySupplierSerializer
    queryset = Factory.objects.all()
    permission_classes = [UserIsActive]

    def partial_update(self, request, *args, **kwargs):
        instance = self.get_object()

        # Проверка исключения обновления поля 'debt'
        if 'debt' in request.data and (request.method == 'PUT' or request.method == 'PATCH'):
            # Запрет обновления поля 'debt'
            return Response({'error': 'Обновление поля debt запрещено вам.'}, status=status.HTTP_400_BAD_REQUEST)

        serializer = self.get_serializer(instance, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)

        return Response(serializer.data)


class FactoryDetailView(generics.RetrieveAPIView):
    """Просмотр деталей заводского поставщика (GET)"""
    serializer_class = FactorySupplierSerializer
    queryset = Factory.objects.all()
    permission_classes = [UserIsActive]


class FactoryDeleteAPIView(generics.DestroyAPIView):
    """Удаление заводского поставщика (DELETE)"""
    serializer_class = FactorySupplierSerializer
    queryset = Factory.objects.all()
    permission_classes = [UserIsActive]


class RetailListAPIView(generics.ListAPIView):
    """Список поставщиков розничной сети (GET)"""
    serializer_class = RetailSupplierSerializer
    queryset = RetailNetwork.objects.all()
    permission_classes = [UserIsActive]


class RetailCreateAPIView(generics.CreateAPIView):
    """Создание нового поставщика розничной сети (POST)"""
    serializer_class = RetailSupplierSerializer
    queryset = RetailNetwork.objects.all()
    permission_classes = [UserIsActive]


class RetailUpdateAPIView(generics.UpdateAPIView):
    """Обновление информации о розничном поставщике (PUT, PATCH)"""
    serializer_class = RetailSupplierSerializer
    queryset = RetailNetwork.objects.all()
    permission_classes = [UserIsActive]


class RetailDetailView(generics.RetrieveAPIView):
    """Просмотр деталей розничного поставщика (GET)"""
    serializer_class = RetailSupplierSerializer
    queryset = RetailNetwork.objects.all()
    permission_classes = [UserIsActive]


class RetailDeleteAPIView(generics.DestroyAPIView):
    """Удаление поставщика розничной сети (DELETE)"""
    serializer_class = RetailSupplierSerializer
    queryset = RetailNetwork.objects.all()
    permission_classes = [UserIsActive]


class EntrepreneurListAPIView(generics.ListAPIView):
    """Список поставщиков ИП (GET)"""
    serializer_class = EntrepreneurSupplierSerializer
    queryset = IndividualEntrepreneur.objects.all()
    permission_classes = [UserIsActive]


class EntrepreneurCreateAPIView(generics.CreateAPIView):
    """Создание нового поставщика ИП (POST)"""
    serializer_class = EntrepreneurSupplierSerializer
    queryset = IndividualEntrepreneur.objects.all()
    permission_classes = [UserIsActive]


class EntrepreneurUpdateAPIView(generics.UpdateAPIView):
    """Обновление информации о поставщике ИП (PUT, PATCH)"""
    serializer_class = EntrepreneurSupplierSerializer
    queryset = IndividualEntrepreneur.objects.all()
    permission_classes = [UserIsActive]


class EntrepreneurDetailView(generics.RetrieveAPIView):
    """Просмотр деталей поставщика ИП (GET)"""
    serializer_class = EntrepreneurSupplierSerializer
    queryset = IndividualEntrepreneur.objects.all()
    permission_classes = [UserIsActive]


class EntrepreneurDeleteAPIView(generics.DestroyAPIView):
    """Удаление поставщика ИП (DELETE)"""
    serializer_class = EntrepreneurSupplierSerializer
    queryset = IndividualEntrepreneur.objects.all()
    permission_classes = [UserIsActive]

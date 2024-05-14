from rest_framework import generics

from networks.models import Factory
from networks.permissions import IsActive
from networks.serializers import SupplierSerializer


class SupplierListAPIView(generics.ListAPIView):
    serializer_class = SupplierSerializer
    queryset = Factory.objects.all()
    permission_classes = [IsActive]


class SupplierCreateAPIView(generics.CreateAPIView):
    serializer_class = SupplierSerializer
    queryset = Factory.objects.all()
    permission_classes = [IsActive]


class SupplierUpdateAPIView(generics.UpdateAPIView):
    serializer_class = SupplierSerializer
    queryset = Factory.objects.all()
    permission_classes = [IsActive]


class SupplierDetailView(generics.RetrieveAPIView):
    serializer_class = SupplierSerializer
    queryset = Factory.objects.all()
    permission_classes = [IsActive]


class SupplierDeleteAPIView(generics.DestroyAPIView):
    serializer_class = SupplierSerializer
    queryset = Factory.objects.all()
    permission_classes = [IsActive]

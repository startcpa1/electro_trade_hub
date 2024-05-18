from rest_framework import generics, status
from rest_framework.response import Response

from networks.models import NetworkNode
from networks.serializers import NetworkNodeSerializer
from users.permissions import UserIsActive


class NetworkNodeListAPIView(generics.ListAPIView):
    """Список поставщиков (GET)"""
    serializer_class = NetworkNodeSerializer
    queryset = NetworkNode.objects.all()
    permission_classes = [UserIsActive]


class NetworkNodeCreateAPIView(generics.CreateAPIView):
    """Создание нового поставщика (POST)"""
    serializer_class = NetworkNodeSerializer
    queryset = NetworkNode.objects.all()
    permission_classes = [UserIsActive]


class NetworkNodeUpdateAPIView(generics.UpdateAPIView):
    """Обновление информации о поставщике (PUT, PATCH)"""
    serializer_class = NetworkNodeSerializer
    queryset = NetworkNode.objects.all()
    permission_classes = [UserIsActive]

    def partial_update(self, request, *args, **kwargs):
        instance = self.get_object()

        # Проверка исключения обновления поля 'debt'
        if 'debt' in request.data and (request.method == 'PUT' or request.method == 'PATCH'):
            # Запрет обновления поля 'debt'
            return Response({'error': 'Обновление поля debt доступно только через админ-панель.'},
                            status=status.HTTP_400_BAD_REQUEST)

        serializer = self.get_serializer(instance, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)

        return Response(serializer.data)


class NetworkNodeDetailView(generics.RetrieveAPIView):
    """Просмотр деталей поставщика (GET)"""
    serializer_class = NetworkNodeSerializer
    queryset = NetworkNode.objects.all()
    permission_classes = [UserIsActive]


class NetworkNodeDeleteAPIView(generics.DestroyAPIView):
    """Удаление поставщика (DELETE)"""
    serializer_class = NetworkNodeSerializer
    queryset = NetworkNode.objects.all()
    permission_classes = [UserIsActive]

from rest_framework import generics, status
from rest_framework.response import Response

from users.models import Employee
from users.permissions import UserIsActive
from users.serializers import EmployeeSerializer


class EmployeeListView(generics.ListAPIView):
    """Представление информации списка пользователей"""
    serializer_class = EmployeeSerializer
    queryset = Employee.objects.all()
    permission_classes = [UserIsActive]


class EmployeeCreateView(generics.CreateAPIView):
    serializer_class = EmployeeSerializer

    def create(self, request, *args, **kwargs):
        """Переопределяем метод для сохранения хешированного пароля"""
        serializer = EmployeeSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)

        password = serializer.data["password"]
        user = Employee.objects.get(pk=serializer.data["id"])
        user.set_password(password)
        user.is_active = True
        user.save()

        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)


class EmployeeUpdateView(generics.UpdateAPIView):
    """Представление для обновления информации о пользователе"""
    serializer_class = EmployeeSerializer
    queryset = Employee.objects.all()
    permission_classes = [UserIsActive]


class EmployeeDetailView(generics.RetrieveAPIView):
    """Представление для получения информации о пользователе"""
    serializer_class = EmployeeSerializer
    queryset = Employee.objects.all()
    permission_classes = [UserIsActive]


class EmployeeDeleteView(generics.DestroyAPIView):
    """Представление для удаления информации о пользователе"""
    queryset = Employee.objects.all()
    permission_classes = [UserIsActive]

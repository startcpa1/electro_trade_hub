from django.urls import path
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from users.apps import UsersConfig
from users.views import EmployeeListView, EmployeeCreateView, EmployeeDetailView, \
    EmployeeUpdateView, EmployeeDeleteView

app_name = UsersConfig.name


urlpatterns = [
    # URL-пути для токена
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

    # URL-пути для сотрудника
    path('employee/', EmployeeListView.as_view(), name='employee-list'),
    path('employee/create/', EmployeeCreateView.as_view(), name='employee-create'),
    path('employee/<int:pk>/', EmployeeDetailView.as_view(), name='employee-detail'),
    path('employee/<int:pk>/update/', EmployeeUpdateView.as_view(), name='employee-update'),
    path('employee/<int:pk>/delete/', EmployeeDeleteView.as_view(), name='employee-delete'),

]

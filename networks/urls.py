from django.urls import path

from networks.apps import NetworksConfig
from networks.views import NetworkNodeListAPIView, NetworkNodeCreateAPIView, NetworkNodeDetailView, \
    NetworkNodeUpdateAPIView, NetworkNodeDeleteAPIView

# Имя приложения для идентификации URL-путей
app_name = NetworksConfig.name

urlpatterns = [
    # URL-пути для звеньев сети
    path('suppliers/', NetworkNodeListAPIView.as_view(), name='networks-supplier-list'),
    path('suppliers/create/', NetworkNodeCreateAPIView.as_view(), name='networks-suppliers-create'),
    path('suppliers/<int:pk>/', NetworkNodeDetailView.as_view(), name='networks-supplier-detail'),
    path('suppliers/<int:pk>/update/', NetworkNodeUpdateAPIView.as_view(), name='networks-supplier-update'),
    path('suppliers/<int:pk>/delete/', NetworkNodeDeleteAPIView.as_view(), name='networks-supplier-delete'),
]

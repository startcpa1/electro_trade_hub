from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from networks.apps import NetworksConfig
from networks.views import SupplierListAPIView, SupplierCreateAPIView, SupplierDetailView, SupplierUpdateAPIView, \
    SupplierDeleteAPIView

app_name = NetworksConfig.name

urlpatterns = [
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

    path('suppliers/', SupplierListAPIView.as_view(), name='supplier-list'),
    path('suppliers/create/', SupplierCreateAPIView.as_view(), name='suppliers-create'),
    path('suppliers/<int:pk>/', SupplierDetailView.as_view(), name='supplier-detail'),
    path('suppliers/<int:pk>/update/', SupplierUpdateAPIView.as_view(), name='supplier-update'),
    path('suppliers/<int:pk>/delete/', SupplierDeleteAPIView.as_view(), name='supplier-delete'),

]

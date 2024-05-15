from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from networks.apps import NetworksConfig
from networks.views import FactoryListAPIView, FactoryCreateAPIView, FactoryDetailView, FactoryUpdateAPIView, \
    FactoryDeleteAPIView, RetailListAPIView, RetailCreateAPIView, RetailDetailView, RetailUpdateAPIView, \
    RetailDeleteAPIView, EntrepreneurListAPIView, EntrepreneurCreateAPIView, EntrepreneurDetailView, \
    EntrepreneurUpdateAPIView, EntrepreneurDeleteAPIView

app_name = NetworksConfig.name

urlpatterns = [
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

    path('factory/suppliers/', FactoryListAPIView.as_view(), name='factory-supplier-list'),
    path('factory/suppliers/create/', FactoryCreateAPIView.as_view(), name='factory-suppliers-create'),
    path('factory/suppliers/<int:pk>/', FactoryDetailView.as_view(), name='factory-supplier-detail'),
    path('factory/suppliers/<int:pk>/update/', FactoryUpdateAPIView.as_view(), name='factory-supplier-update'),
    path('factory/suppliers/<int:pk>/delete/', FactoryDeleteAPIView.as_view(), name='factory-supplier-delete'),

    path('retail/suppliers/', RetailListAPIView.as_view(), name='retail-supplier-list'),
    path('retail/suppliers/create/', RetailCreateAPIView.as_view(), name='retail-suppliers-create'),
    path('retail/suppliers/<int:pk>/', RetailDetailView.as_view(), name='retail-supplier-detail'),
    path('retail/suppliers/<int:pk>/update/', RetailUpdateAPIView.as_view(), name='retail-supplier-update'),
    path('retail/suppliers/<int:pk>/delete/', RetailDeleteAPIView.as_view(), name='retail-supplier-delete'),

    path('ie/suppliers/', EntrepreneurListAPIView.as_view(), name='ie-supplier-list'),
    path('ie/suppliers/create/', EntrepreneurCreateAPIView.as_view(), name='ie-suppliers-create'),
    path('ie/suppliers/<int:pk>/', EntrepreneurDetailView.as_view(), name='ie-supplier-detail'),
    path('ie/suppliers/<int:pk>/update/', EntrepreneurUpdateAPIView.as_view(), name='ie-supplier-update'),
    path('ie/suppliers/<int:pk>/delete/', EntrepreneurDeleteAPIView.as_view(), name='ie-supplier-delete'),
]

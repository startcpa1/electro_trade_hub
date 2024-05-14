from rest_framework import serializers

from networks.models import Factory


class SupplierSerializer(serializers.ModelSerializer):
    """Базовый сериализатор для моделей"""

    class Meta:
        model = Factory
        fields = '__all__'


def get_supplier_serializer(model_class):
    class Meta:
        model = model_class

    return type(f"{model_class.__name__}Serializer", (SupplierSerializer,), {'Meta': Meta})

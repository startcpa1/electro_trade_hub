from rest_framework import serializers

from networks.models import Factory, RetailNetwork, IndividualEntrepreneur


class FactorySupplierSerializer(serializers.ModelSerializer):
    """Сериализатор для моделей фабрики"""

    class Meta:
        model = Factory
        fields = '__all__'
        read_only_fields = ['debt']
        filter_fields = ['country']


class RetailSupplierSerializer(serializers.ModelSerializer):
    """Сериализатор для модели """

    class Meta:
        model = RetailNetwork
        fields = '__all__'
        read_only_fields = ['debt']
        filter_fields = ['country']


class EntrepreneurSupplierSerializer(serializers.ModelSerializer):
    """Сериализатор для модели """

    class Meta:
        model = IndividualEntrepreneur
        fields = '__all__'
        read_only_fields = ['debt']
        filter_fields = ['country']

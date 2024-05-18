from rest_framework import serializers

from networks.models import NetworkNode


class NetworkNodeSerializer(serializers.ModelSerializer):
    """Сериализатор для сети электроники"""

    class Meta:
        model = NetworkNode
        fields = '__all__'
        read_only_fields = ['debt']
        filter_fields = ['country']

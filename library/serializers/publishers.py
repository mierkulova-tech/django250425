from rest_framework import serializers

from library.models import Publisher


class PublisherDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Publisher
        fields = "__all__"


class PublisherListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Publisher
        fields = [
            'id',
            'name',
            'country'
        ]


class PublisherCreateUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Publisher
        fields = "__all__"

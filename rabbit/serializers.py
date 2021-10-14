from rest_framework.serializers import ModelSerializer

from rabbit import models


class ProductSerializer(ModelSerializer):
    class Meta:
        model = models.Product
        fields = '__all__'

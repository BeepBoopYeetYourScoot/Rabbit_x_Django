from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from rest_framework import status

from rabbit import models, serializers
from rabbit.producer import send_log_message
from rabbit.filters import ProductFilterSet

from django_filters.rest_framework import DjangoFilterBackend


class ProductViewSet(ModelViewSet):
    # model = models.Product
    queryset = models.Product.objects.all()
    serializer_class = serializers.ProductSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = ProductFilterSet

    @action(detail=False, url_path='send-hello')
    def send_hello(self, request):
        send_log_message('Request from API!')
        return Response({'detail': 'Сообщение отправлено'}, status=status.HTTP_202_ACCEPTED)

    @action(detail=False, url_path='')
    def upload_excel(self, request):
        pass

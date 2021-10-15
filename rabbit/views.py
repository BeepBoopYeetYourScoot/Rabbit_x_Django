from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from rest_framework import status

from rabbit import models, serializers
from rabbit.producer import producer_send_message


class ProductViewSet(ModelViewSet):
    queryset = models.Product.objects.all()
    serializer_class = serializers.ProductSerializer

    @action(detail=False, url_path='send-hello')
    def send_hello(self, request):
        producer_send_message()
        return Response({'detail': 'Сообщение отправлено'}, status=status.HTTP_202_ACCEPTED)

    @action(detail=False, url_path='')
    def upload_excel(self, request):
        pass


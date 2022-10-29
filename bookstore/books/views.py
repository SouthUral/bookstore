from django.shortcuts import render
from rest_framework import viewsets
from .models import *
from .serializers import *
from rest_framework.decorators import action
from rest_framework.response import Response


# Create your views here.
class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer


class GenreViewSet(viewsets.ModelViewSet):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer


class AuthorViewSet(viewsets.ModelViewSet):
    queryset = Author.objects.all()
    serializer_class = GenreSerializer


class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

    @action(methods=["get"], detail=False)
    def get_on_client(self, request):
        client_param = request.query_params.get("client")
        queryset = Order.objects.filter(client__name_client=client_param)
        serializers = self.serializer_class(queryset, many=True)
        return Response({'order' :serializers.data})

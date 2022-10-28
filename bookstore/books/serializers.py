from rest_framework import serializers

from .models import Client, Author, Genre, Book, City, Order, Сontent_order, Order_step


class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = ("id", "name_client", "city", "email")


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = ("id", "name_author")


class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = "__all__"


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = "__all__"


class CitySerializer(serializers.ModelSerializer):
    class Meta:
        model = City
        fields = "__all__"


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = "__all__"


class Сontent_orderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Сontent_order
        fields = "__all__"


class Order_stepSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order_step
        fields = "__all__"
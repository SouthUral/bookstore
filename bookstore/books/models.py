
from django.db import models


# Create your models here.
class Author(models.Model):
    id = models.AutoField(primary_key=True)
    name_author = models.CharField(max_length=50, verbose_name='Имя автора')

    def __str__(self):
        return self.name_author

    class Meta:
        verbose_name = "Имя автора"
        verbose_name_plural = "Авторы"


class Genre(models.Model):
    id = models.AutoField(primary_key=True)
    name_genre = models.CharField(max_length=30, verbose_name="Жанр", unique=True)

    def __str__(self):
        return self.name_genre

    class Meta:
        verbose_name = "Жанр"
        verbose_name_plural = "Жанры"


class Book(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100, verbose_name="Название")
    author = models.ForeignKey(Author, related_name="book", on_delete=models.CASCADE, verbose_name="Автор")
    genre = models.ForeignKey(Genre, related_name="book", on_delete=models.SET_NULL, null=True, verbose_name="Жанр")
    price = models.FloatField(verbose_name="Цена", null=True, blank=False)
    amount = models.IntegerField(verbose_name="Количество", null=True, blank=False)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Книга"
        verbose_name_plural = "Книги"
        constrains = [
            models.UniqueConstraint(
                fields=["title", "author"], name="unique_book"
            )
        ]


class City(models.Model):
    id = models.AutoField(primary_key=True)
    name_city = models.CharField(max_length=30, verbose_name="Город", unique=True)
    days_delivery = models.IntegerField(verbose_name="Срок доставки", default=0)

    def __str__(self):
        return f"{self.name_city}: {self.days_delivery}"

    class Meta:
        verbose_name = "Город"
        verbose_name_plural = "Города"


class Client(models.Model):
    id = models.AutoField(primary_key=True)
    name_client = models.CharField(max_length=50, verbose_name="Имя клиента")
    city = models.ForeignKey(City, related_name="client", on_delete=models.SET_NULL, null=True)
    email = models.EmailField()

    def __str__(self):
        return self.name_client

    class Meta:
        verbose_name = "Клиент"
        verbose_name_plural = "Клиенты"


class Order(models.Model):
    id = models.AutoField(primary_key=True)
    description = models.CharField(max_length=100, verbose_name="Комментарии к заказу")
    client = models.ForeignKey(Client, related_name="order", on_delete=models.SET_NULL, null=True, verbose_name="Клиент")

    def __str__(self):
        return f"{self.client}: id_order {self.id}"

    class Meta:
        verbose_name = "Заказ"
        verbose_name_plural = "Заказы"


class Сontent_order(models.Model):
    id = models.AutoField(primary_key=True)
    order = models.ForeignKey(Order, related_name="content_order", on_delete=models.SET_NULL, null=True, verbose_name="Заказ")
    book = models.ForeignKey(Book, related_name="content_order", on_delete=models.SET_NULL, null=True, verbose_name="Книга")
    amount = models.IntegerField(verbose_name="Количество")


class Order_step(models.Model):
    steps = [
        ("buy", "Оплата"),
        ("packaging", "Упаковка"),
        ("transportation", "Транспортировка"),
        ("delivered", "Доставка"),
    ]

    id = models.AutoField(primary_key=True)
    order = models.ForeignKey(Order, related_name="order_step", verbose_name="Заказ", on_delete=models.CASCADE)
    step = models.CharField(choices=steps, max_length=30, default="buy", verbose_name="Этап")
    date_step_beg = models.DateField(verbose_name="Дата начала этапа", auto_now_add=True, null=True)
    date_step_end = models.DateField(verbose_name="Дата завершения этапа", blank=False, null=True)

    def __str__(self):
        return f"{self.step}: {self.date_step_beg}|{self.date_step_end}"

    class Meta:
        verbose_name = "Этап"
        verbose_name_plural = "Этапы"
        constrains = [
            models.UniqueConstraint(
                fields=["order", "step"], name="unique_step_order"
            )
        ]

# Generated by Django 4.1.2 on 2022-10-27 16:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Author",
            fields=[
                ("id", models.AutoField(primary_key=True, serialize=False)),
                (
                    "name_author",
                    models.CharField(max_length=50, verbose_name="Имя автора"),
                ),
            ],
            options={
                "verbose_name": "Имя автора",
                "verbose_name_plural": "Авторы",
            },
        ),
        migrations.CreateModel(
            name="Book",
            fields=[
                ("id", models.AutoField(primary_key=True, serialize=False)),
                ("title", models.CharField(max_length=100, verbose_name="Название")),
                ("price", models.FloatField(null=True, verbose_name="Цена")),
                ("amount", models.IntegerField(null=True, verbose_name="Количество")),
                (
                    "author",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="book",
                        to="books.author",
                        verbose_name="Автор",
                    ),
                ),
            ],
            options={
                "verbose_name": "Книга",
                "verbose_name_plural": "Книги",
            },
        ),
        migrations.CreateModel(
            name="City",
            fields=[
                ("id", models.AutoField(primary_key=True, serialize=False)),
                (
                    "name_city",
                    models.CharField(max_length=30, unique=True, verbose_name="Город"),
                ),
                (
                    "days_delivery",
                    models.IntegerField(default=0, verbose_name="Срок доставки"),
                ),
            ],
            options={
                "verbose_name": "Город",
                "verbose_name_plural": "Города",
            },
        ),
        migrations.CreateModel(
            name="Client",
            fields=[
                ("id", models.AutoField(primary_key=True, serialize=False)),
                (
                    "name_client",
                    models.CharField(max_length=50, verbose_name="Имя клиента"),
                ),
                ("email", models.EmailField(max_length=254)),
                (
                    "city",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="client",
                        to="books.city",
                    ),
                ),
            ],
            options={
                "verbose_name": "Клиент",
                "verbose_name_plural": "Клиенты",
            },
        ),
        migrations.CreateModel(
            name="Genre",
            fields=[
                ("id", models.AutoField(primary_key=True, serialize=False)),
                (
                    "name_genre",
                    models.CharField(max_length=30, unique=True, verbose_name="Жанр"),
                ),
            ],
            options={
                "verbose_name": "Жанр",
                "verbose_name_plural": "Жанры",
            },
        ),
        migrations.CreateModel(
            name="Order",
            fields=[
                ("id", models.AutoField(primary_key=True, serialize=False)),
                (
                    "description",
                    models.CharField(
                        max_length=100, verbose_name="Комментарии к заказу"
                    ),
                ),
                (
                    "client",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="order",
                        to="books.client",
                        verbose_name="Клиент",
                    ),
                ),
            ],
            options={
                "verbose_name": "Заказ",
                "verbose_name_plural": "Заказы",
            },
        ),
        migrations.CreateModel(
            name="Сontent_order",
            fields=[
                ("id", models.AutoField(primary_key=True, serialize=False)),
                ("amount", models.IntegerField(verbose_name="Количество")),
                (
                    "book",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="content_order",
                        to="books.book",
                        verbose_name="Книга",
                    ),
                ),
                (
                    "order",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="content_order",
                        to="books.order",
                        verbose_name="Заказ",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Order_step",
            fields=[
                ("id", models.AutoField(primary_key=True, serialize=False)),
                (
                    "step",
                    models.CharField(
                        choices=[
                            ("buy", "Оплата"),
                            ("packaging", "Упаковка"),
                            ("transportation", "Транспортировка"),
                            ("delivered", "Доставка"),
                        ],
                        default="buy",
                        max_length=30,
                        verbose_name="Этап",
                    ),
                ),
                (
                    "date_step_beg",
                    models.DateField(
                        auto_now_add=True, null=True, verbose_name="Дата начала этапа"
                    ),
                ),
                (
                    "date_step_end",
                    models.DateField(null=True, verbose_name="Дата завершения этапа"),
                ),
                (
                    "order",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="order_step",
                        to="books.order",
                        verbose_name="Заказ",
                    ),
                ),
            ],
            options={
                "verbose_name": "Этап",
                "verbose_name_plural": "Этапы",
            },
        ),
        migrations.AddField(
            model_name="book",
            name="genre",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="book",
                to="books.genre",
                verbose_name="Жанр",
            ),
        ),
    ]
# Generated by Django 4.1.2 on 2022-10-27 17:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("books", "0002_alter_author_options_alter_book_options_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="order",
            name="description",
            field=models.CharField(
                blank=True,
                max_length=100,
                null=True,
                verbose_name="Комментарии к заказу",
            ),
        ),
    ]

from django.contrib import admin
from .models import *


class Order_stepInline(admin.TabularInline):
    model = Order_step
    fk_name = "order"


class AuthorAdmin(admin.ModelAdmin):
    list_display = ('id', 'name_author')


class BooksAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'author', 'genre', 'price', 'amount')


class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'description', 'client')
    list_filter = ('client',)
    inlines = [
        Order_stepInline,
    ]


class Сontent_orderAdmin(admin.ModelAdmin):
    list_display = ('id', 'order', 'book', 'amount')
    list_filter = ('order',)


class Order_stepAdmin(admin.ModelAdmin):
    list_display = ('id', 'order', 'step', 'date_step_beg', 'date_step_end')
    list_filter = ('order', 'step')


# Register your models here.
admin.site.register(Author, AuthorAdmin)
admin.site.register(Genre)
admin.site.register(Book, BooksAdmin)
admin.site.register(City)
admin.site.register(Client)
admin.site.register(Order, OrderAdmin)
admin.site.register(Order_step, Order_stepAdmin)
admin.site.register(Сontent_order, Сontent_orderAdmin)

from django.db import models
from django.conf import settings


class Products(models.Model):
    name = models.CharField(max_length=40, unique=True, verbose_name="Название")
    slug = models.SlugField(max_length=60, unique=True, blank=True, null=True, verbose_name='URL')
    description = models.CharField(max_length=200, unique=True, null=True, verbose_name='Описание')
    img = models.ImageField(upload_to='products_images', blank=True, null=True, verbose_name='Изображение')
    price = models.DecimalField(default=0.00, max_digits=7, decimal_places=2, verbose_name='Цена')
    quantity = models.PositiveIntegerField(default=0, verbose_name='Количество')

    class Meta:
        db_table = 'Products'
        verbose_name = 'Продукты'
        verbose_name_plural = 'Продукт'
        ordering = ("id",)

    def __str__(self):
        return self.name

    def display_id(self):
        return f"{self.id:05}"


class NotesUser(models.Model):
    images = models.ImageField(upload_to='users_orders',
                               null=True, blank=True,
                               verbose_name='Изображения')
    created_date = models.DateTimeField(auto_now_add=True, verbose_name='Дата Создания')
    wish = models.TextField(null=True, max_length=200, blank=True, verbose_name='Пожелание')
    username = models.TextField(max_length=40, verbose_name='Имя Пользователя')
    first_name = models.TextField(max_length=30, null=True, blank=True, verbose_name='Имя')
    phone = models.TextField(max_length=18, verbose_name='Номер Телефона')

    class Meta:
        db_table = 'Orders'
        verbose_name = 'Заказы'
        verbose_name_plural = 'Заказ'
        ordering = ("-created_date",)

    def __str__(self):
        return self.username


class Questions(models.Model):
    first_name = models.TextField(max_length=30, null=True, blank=True, verbose_name="Имя")
    username = models.TextField(max_length=40, verbose_name='Имя Пользователя')
    phone = models.TextField(max_length=18, verbose_name='Номер Телефона')
    created_date = models.DateTimeField(auto_now_add=True, verbose_name='Дата Создания')
    question = models.TextField(null=True, max_length=200, blank=True, verbose_name='Вопрос')

    class Meta:
        db_table = 'Questions'
        verbose_name = 'Вопросы'
        verbose_name_plural = 'Вопрос'
        ordering = ("-created_date",)

    def __str__(self):
        return self.username

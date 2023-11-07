from django.db import models


class Category(models.Model):
    # verbose_name = 'товар'  # Настройка для наименования одного объекта
    # verbose_name_plural = 'товары'  # Настройка для наименования набора объектов
    name = models.CharField(max_length=150, verbose_name='товар')
    description = models.CharField(max_length=150, verbose_name='описание')

    class Meta:
        verbose_name = 'категория'
        verbose_name_plural = 'категории'
        ordering = ('description',)


class Product(models.Model):
    name = models.CharField(max_length=150, verbose_name='товар')
    description = models.CharField(max_length=150, verbose_name='описание')
    image = models.ImageField(upload_to='картинки', max_length=1000)
    category = models.CharField(max_length=150, verbose_name='категория')
    price = models.CharField(max_length=150, verbose_name='цена')
    date_creation = models.DateTimeField(auto_now_add=True)
    date_last_use = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'товар'
        verbose_name_plural = 'товары'
        ordering = ('name',)



    def __str__(self):
        # Строковое отображение объекта
        return f'{self.first_name} {self.last_name}'

pass

from django.db import models

NULLABLE = {'blank': True,
            'null': True,
            }


class Product(models.Model):
    """Создаем класс продукта"""

    title = models.CharField(max_length=30, verbose_name='название', **NULLABLE)
    model = models.CharField(max_length=30, verbose_name='модель', **NULLABLE)
    release_date = models.DateField(verbose_name='дата выхода продукта')

    def __str__(self):
        return f'{self.title} - {self.model}'

    class Meta:
        verbose_name = 'продукт'
        verbose_name_plural = 'продукты'

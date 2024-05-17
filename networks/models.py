from django.db import models
from django.db.models.signals import pre_save
from django.dispatch import receiver

from products.models import Product

NULLABLE = {'blank': True,
            'null': True,
            }


class NetworkNode(models.Model):
    """Создаем класс сети электроники"""
    LEVEL_CHOICES = (
        (0, 'Завод'),
        (1, 'Розничная сеть'),
        (2, 'Индивидуальный предприниматель'),
    )

    name = models.CharField(max_length=100, verbose_name='Название', **NULLABLE)
    email = models.EmailField(verbose_name='Email', **NULLABLE)
    country = models.CharField(max_length=100, verbose_name='Страна', **NULLABLE)
    city = models.CharField(max_length=100, verbose_name='Город', **NULLABLE)
    street = models.CharField(max_length=100, verbose_name='Улица', **NULLABLE)
    house_number = models.CharField(max_length=10, verbose_name='Номер дома', **NULLABLE)
    products = models.ManyToManyField(Product, related_name='network_nodes', verbose_name="Продукты")

    supplier = models.ForeignKey('self', on_delete=models.SET_NULL, **NULLABLE, verbose_name='Поставщик')
    debt = models.DecimalField(max_digits=10, decimal_places=2, default=0, verbose_name='Задолженность(Руб)')
    created_time = models.DateTimeField(auto_now_add=True, verbose_name='Время создания')
    level = models.IntegerField(choices=LEVEL_CHOICES, **NULLABLE,
                                verbose_name='Уровень')  # Добавляем поле для определения уровня иерархии

    def __str__(self):
        return f"{self.name}, {self.email}, {self.country}"

    class Meta:
        verbose_name = 'звено сети'
        verbose_name_plural = 'звенья сети'


@receiver(pre_save, sender=NetworkNode)
def set_network_node_level(sender, instance, **kwargs):
    if instance.supplier:
        instance.level = instance.supplier.level + 1
    else:
        # Если у объекта нет поставщика, он считается заводом (уровень 0)
        instance.level = 0

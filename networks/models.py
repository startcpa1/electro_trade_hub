from django.db import models

NULLABLE = {'blank': True,
            'null': True,
            }


class NetworkNode(models.Model):
    """Создаем класс сети электроники"""
    name = models.CharField(max_length=100, verbose_name='Название', **NULLABLE)
    email = models.EmailField(verbose_name='Email', **NULLABLE)
    country = models.CharField(max_length=100, verbose_name='Страна', **NULLABLE)
    city = models.CharField(max_length=100, verbose_name='Город', **NULLABLE)
    street = models.CharField(max_length=100, verbose_name='Улица', **NULLABLE)
    house_number = models.CharField(max_length=10, verbose_name='Номер дома', **NULLABLE)

    supplier = models.ForeignKey('self', on_delete=models.SET_NULL, **NULLABLE, verbose_name='Поставщик')
    debt = models.DecimalField(max_digits=10, decimal_places=2, default=0, verbose_name='Задолженность')
    created_time = models.DateTimeField(auto_now_add=True, verbose_name='Время создания')

    class Meta:
        abstract = True

    def __str__(self):
        return self.name


class Factory(NetworkNode):
    """Создаем класс завода"""

    class Meta:
        verbose_name = 'завод'
        verbose_name_plural = 'заводы'


class RetailNetwork(NetworkNode):
    """Создаем класс розничной сети"""

    class Meta:
        verbose_name = 'розничная сеть'
        verbose_name_plural = 'розничные сети'


class IndividualEntrepreneur(NetworkNode):
    """Создаем класс индивидуального предпринимателя"""

    class Meta:
        verbose_name = 'индивидуальный предприниматель'
        verbose_name_plural = 'индивидуальные предприниматели'

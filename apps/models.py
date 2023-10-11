from django.db import models


class Brand(models.Model):

    class Meta:
        verbose_name = 'Марка'
        verbose_name_plural = 'Марки'

    name = models.CharField(verbose_name = 'Имя марка', max_length=150, unique=True)

    def __str__(self):
        return f'{self.name}'


class Car(models.Model):

    class Meta:
        verbose_name = 'Автомобил'
        verbose_name_plural = 'Автомобили'

    model = models.CharField(max_length=150, verbose_name='Модель')
    brand = models.ForeignKey(Brand, verbose_name = 'Марка', on_delete=models.CASCADE, related_name='cars',)
    year = models.IntegerField(verbose_name='год выпуска')
    image = models.ImageField(upload_to='images/', verbose_name='обложка',)
    overview = models.CharField(max_length=1000, verbose_name='Краткое описание',)
    owner = models.ForeignKey('auth.User', on_delete=models.CASCADE, verbose_name='Владелец', null=True)
    price = models.IntegerField(verbose_name='Цена автомобиля')
    color = models.CharField(max_length=100, verbose_name='Цвет автомобиля')
    date = models.DateTimeField(auto_now_add=True, verbose_name='дата добавление')

    def __str__(self):
        return f'{self.brand.name} - {self.model}'

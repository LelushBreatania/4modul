from django.db import models


class Advertisement(models.Model):

    #Название тавара
    # CharField - короткое текстовое поле
    # 'Заголовок' - verbose_name - человекочитаемое название
    title = models.CharField('Заголовок',max_length=128)

    # Описание товара
    description = models.TextField('описание')

    # Цена
    # Числовое поле с фиксированой точкой
    price = models.DecimalField('цена', max_digits=10, decimal_places=2)

    # Уместен ли торг
    auction = models.BooleanField('торг', help_text='отметьте, если хотите торговаться')

    # Дата публикации
    created_at = models.DateTimeField(auto_now_add=True)

    # Дата изменения/обнавления + что изменилось
    updated_at = models.DateTimeField(auto_now=True)

    # Продавец

    # Фото объявления

    # Рейтинг

    # В продаже/не в продаже - актуальность

    

    

    



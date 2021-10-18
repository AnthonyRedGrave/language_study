from django.db import models

class Card(models.Model):
    class LanguageChoices(models.TextChoices):
        russian = "Russian", "Русский"
        english = "English", "Английский"
        french = "French", "Французский"

    sentence = models.CharField('Определение', max_length=100)
    translate = models.CharField('Перевод', max_length=100)
    image = models.ImageField('Картинка к карточке', null=True, blank=True, upload_to="cards/images/")
    collection = models.ForeignKey('Collection', blank=False, on_delete=models.CASCADE)
    language = models.CharField("Язык", choices=LanguageChoices.choices, max_length=50)

    def __str__(self):
        return f"Карточка {self.sentence} - {self.translate}"


    class Meta:
        verbose_name = 'Карточка'
        verbose_name_plural = 'Карточки'


class Collection(models.Model):
    title = models.CharField('Название коллекции', max_length=100)
    desc = models.TextField('Описание коллекции')


    class Meta:
        verbose_name = 'Коллекция'
        verbose_name_plural = 'Коллекции'
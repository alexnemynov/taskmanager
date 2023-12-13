from django.db import models

class Task(models.Model):
    title = models.CharField('Название', max_length=50)  # текст до 255 символов
    task = models.TextField('Опсиание')  # огрмоное кол-во текста планируется

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Задача'
        verbose_name_plural = 'Задачи'
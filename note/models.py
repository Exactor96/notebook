from django.db import models

# Create your models here.
class Note(models.Model):
    title = models.CharField(verbose_name='Заголовок', max_length=50)
    body = models.TextField(verbose_name='Текст')
    created = models.DateTimeField(verbose_name='Создан', auto_now_add=True)

    class Meta:
        verbose_name = 'Заметка'
        verbose_name_plural = 'Заметки'


    def __str__(self):
        return 'Заметка №{}: {}'.format(self.id, self.title)

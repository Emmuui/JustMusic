from django.db import models
from django.urls import reverse

class Author(models.Model):
    pseudonym = models.CharField('Псевдоним', max_length=20)
    portrait = models.ImageField('портрет', null=True, blank=True, upload_to='authors/')
    description= models.FileField('Описание', null=True, blank=True, upload_to='descriptions/')
    def __str__(self):
        return f'{self.pseudonym}'
    def get_absolute_url(self):
        return reverse('pr1:author_detail',
                       args=(self.id,))
    class Meta:
        ordering = ['pseudonym']

class Music(models.Model):
    title = models.CharField('название', max_length=30)
    year = models.IntegerField('год выпуска', null=True, blank=True)
    author = models.ForeignKey(Author, help_text='автор', on_delete=models.SET_NULL,
                               blank=True, null=True)
    rating = models.FloatField('рейтинг', default=5.0)
    poster = models.ImageField('постер', null=True, blank=True, upload_to='musics/')
    text = models.FileField('текст', null=True, blank=True, upload_to='texts/')

    def __str__(self):
        return self.title
    def get_absolute_url(self):
        return reverse('pr1:music_detail',
                       args=(self.id,))
    class Meta:
        ordering = ['title']



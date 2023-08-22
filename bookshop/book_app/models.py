from django.db import models
from django.urls import reverse
from pytils.translit import slugify


class Book(models.Model):
    title = models.CharField(max_length=70)
    author = models.CharField(max_length=100, null=True)
    rating = models.IntegerField()
    is_best_selling = models.BooleanField()
    slug = models.SlugField(default='', null=False, db_index=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Book, self).save(*args, **kwargs)

    def get_url(self):
        return reverse('book_detail', args=[self.slug])

    def __str__(self):
        return f'{self.title} - {self.rating}%'

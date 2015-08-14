from django.db import models


class Quote(models.Model):
    title = models.CharField(max_length=100)
    pub_date = models.DateField('date published')

    def __str__(self):
        return self.title


class Image(models.Model):
    url = models.CharField(max_length=100)
    quote = models.ForeignKey(Quote)

    def __str__(self):
        return self.url

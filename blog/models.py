# -*- coding: utf-8 -*-

from django.db import models


class Article(models.Model):
    class Meta():
        db_table = u'Статья'

    article_title = models.CharField(max_length=70)
    article_text = models.TextField()
    article_date = models.DateField(auto_now_add=True)
    article_likes = models.IntegerField(default=0)

    def __unicode__(self):
        return self.article_title

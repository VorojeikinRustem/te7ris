from django.db import models


class Section(models.Model):
    title = models.CharField(max_length=30)
    title_slug = models.SlugField()
    description = models.TextField()
    image = models.ImageField(upload_to="media/", default="default.jpg")

    def __unicode__(self):
        return self.title

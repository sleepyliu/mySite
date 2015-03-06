from django.db import models

# Create your models here.
class BlogsPost(models.Model):

    """docstring for BlogsPost: 
        define three parameters: title,body and timestamp"""

    title = models.CharField(max_length = 150)
    body = models.TextField()
    timestamp = models.DateTimeField('date published')

    class Meta:
        ordering = ['-timestamp']

    def __str__(self):              # __unicode__ on Python 2
        return self.title


class Favor(models.Model):
    article = models.ForeignKey(BlogsPost)
    like = models.IntegerField(default=0)

    def __str__(self):              # __unicode__ on Python 2
        return str(self.like)

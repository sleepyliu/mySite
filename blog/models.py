from django.db import models

# Create your models here.
class BlogsPost(models.Model):

    """docstring for BlogsPost: 
        define four fields: title,body,timestamp and votes"""

    title = models.CharField(max_length = 150)
    body = models.TextField()
    timestamp = models.DateTimeField('date published')
    votes = models.IntegerField(default=0)

    class Meta:
        ordering = ['-timestamp']

    def __str__(self):              # __unicode__ on Python 2
        return self.title


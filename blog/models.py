from django.db import models

# Create your models here.
class Tag(models.Model):
    """docstring for Tags"""
    tag_name = models.CharField(max_length=20)
    create_time = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return self.tag_name



class BlogsPost(models.Model):

    """docstring for BlogsPost"""

    title = models.CharField(max_length = 150)
    body = models.TextField()
    timestamp = models.DateTimeField('date published',auto_now_add=True)
    tags = models.ManyToManyField(Tag, blank=True,null=True)
    votes = models.IntegerField(default=0)

    class Meta:
        ordering = ['-timestamp']
 
    def __unicode__(self):              # __unicode__ on Python 2  __str__ on Python 3
        return self.title


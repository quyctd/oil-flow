from django.db import models
from taggit.managers import TaggableManager
from ckeditor.fields import RichTextField
from django.utils import timezone

# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length = 255)
    author = models.ForeignKey("auth.User", on_delete= models.CASCADE)
    extend_question = RichTextField()
    create_date = models.DateField(default = timezone.now)
    answer = RichTextField()
    refer_link = models.URLField()
    tags = TaggableManager()
    hits = models.IntegerField(default = 0)

    def __str__(self):
        return self.title

class Category(models.Model):
    course_name = models.CharField(max_length = 255)
    post_list = models.ManyToManyField(Post, blank = True,  related_name='blog_list')

    def __str__(self):
        return self.course_name

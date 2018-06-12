from django.db import models
from taggit.managers import TaggableManager
from ckeditor.fields import RichTextField
from django.utils import timezone
# Create your models here.

class Question(models.Model):
    title = models.CharField(max_length = 255)
    author = models.ForeignKey("auth.User", on_delete= models.CASCADE)
    main_question = RichTextField()
    create_date = models.DateField(default = timezone.now)
    refer_link = models.URLField()
    tags = TaggableManager()
    hits = models.IntegerField(default = 0)

    def __str__(self):
        return self.title

class Category(models.Model):
    name = models.CharField(max_length = 255)
    post_list = models.ManyToManyField(Question, blank = True,  related_name='categories_list')

    def __str__(self):
        return self.name

class Answer(models.Model):
    question = models.ForeignKey(Question, on_delete = models.CASCADE)
    answer = RichTextField()

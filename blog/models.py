from django.db import models
from taggit.managers import TaggableManager
from ckeditor.fields import RichTextField
from django.utils import timezone
from datetime import datetime
from django.template.defaultfilters import slugify

# Create your models here.

class Question(models.Model):
    title = models.CharField(max_length = 255, unique= True)
    author = models.ForeignKey("auth.User", on_delete= models.CASCADE)
    main_question = RichTextField()
    create_date = models.DateField(default = datetime.now)
    tags = TaggableManager()
    hits = models.IntegerField(default = 0)
    slug = models.SlugField(max_length=255, blank=True)

    def __str__(self):
        return self.title

    def save(self, *arg, **kwargs):
        self.slug = slugify(self.title)
        super(Question, self).save(*arg, **kwargs)

class Category(models.Model):
    name = models.CharField(max_length = 255)
    post_list = models.ManyToManyField(Question, blank = True,  related_name='categories_list')

    def __str__(self):
        return self.name

class Answer(models.Model):
    question = models.ForeignKey(Question, on_delete = models.CASCADE, related_name='ans')
    answer = RichTextField()
    refer_link = models.URLField()

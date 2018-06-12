from django.contrib import admin
from blog.models import Question, Category, Answer
# Register your models here.

class CategoryInline(admin.TabularInline):
    model = Category.post_list.through
    extra = 0

class AnswerInline(admin.StackedInline):
    model = Answer
    extra = 1

class QuestionAdmin(admin.ModelAdmin):
    inlines = [ AnswerInline,CategoryInline,]
    exclude = ("hits",)
    list_display = ("title", "author", "create_date","hits")
    search_fields = ("title","created_date", "hits")
    list_filter = ("title", "create_date")

admin.site.register(Question, QuestionAdmin)
admin.site.register(Category)
admin.site.register(Answer)

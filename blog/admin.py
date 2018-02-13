from django.contrib import admin
from blog.models import Post, Category
# Register your models here.

class CategoryInline(admin.TabularInline):
    model = Category.post_list.through
    extra = 0

class PostAdmin(admin.ModelAdmin):
    inlines = [CategoryInline]
    exclude = ("hits",)
    list_display = ("title", "author", "create_date","hits")
    search_fields = ("title","created_date", "hits")
    list_filter = ("title", "create_date")

admin.site.register(Post, PostAdmin)
admin.site.register(Category)

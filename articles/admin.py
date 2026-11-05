from django.contrib import admin
from .models import Article, Comment

# Register your models here.
class CommentAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Comment._meta.fields]
admin.site.register(Comment, CommentAdmin)

class CommentInline(admin.TabularInline):
    model = Comment
    extra = 0

class ArticleAdmin(admin.ModelAdmin):
    inlines = [CommentInline]
    list_display = ["title", "body","author",]
admin.site.register(Article, ArticleAdmin)
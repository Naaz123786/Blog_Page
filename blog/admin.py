from django.contrib import admin

from .models import Post, CommentSectionModel

# Register your models here.

class PostAdmin(admin.ModelAdmin):
    list_filter = ("first_name", "caption", "date")
    list_display =  ("title" , "date", "first_name")
    prepopulated_fields = {"slug" : ("title",)}


admin.site.register(Post, PostAdmin)
admin.site.register(CommentSectionModel)
from django.contrib import admin
from django.db import models
from .models import Article, NewMessage
from ckeditor.widgets import CKEditorWidget
from ckeditor_uploader.widgets import CKEditorUploadingWidget
from django.utils.translation import gettext_lazy as _

class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'pub_date', 'author')
    formfield_overrides = {
        models.TextField: {'widget': CKEditorWidget},
    }

admin.site.register(Article, ArticleAdmin)
admin.site.register(NewMessage)
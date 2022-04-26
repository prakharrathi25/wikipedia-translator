from django.contrib import admin
from .models import *

# Register your models here.
class AdminLanguage(admin.ModelAdmin):
    list_display = ['id','language_code', 'language_name']

class AdminProject(admin.ModelAdmin):
    list_display = ['id','article_title', 'target_language']

class AdminSentence(admin.ModelAdmin): 
    list_display = ['id','project_id', 'original_sentence', 'translated_sentence']

''' Model registration '''
admin.site.register(Language, AdminLanguage)
admin.site.register(Project, AdminProject)
admin.site.register(Sentence, AdminSentence)
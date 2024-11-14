"""

"""
from django.contrib import admin

from .models import Question, Choice


# class ChoiceInline(admin.StackedInline:
class ChoiceInline(admin.TabularInline):
    """
    ChoiceInline(admin.StackedInline):
    """
    model = Choice
    extra = 3


class QuestionAdmin(admin.ModelAdmin):
    """
    QuestionAdmin(admin.ModelAdmin):
    """
    list_display = ('question_text', 'pub_date', 'was_published_recently')
    list_filter = ['pub_date']

    search_fields = ['question']
    date_hierarchy = 'pub_date'

    fieldsets = [
        (None,               {'fields': ['question_text']}),
        ('Date information', {'fields': [
         'pub_date'], 'classes': ['collapse']}),
    ]
    inlines = [ChoiceInline]


admin.site.register(Question, QuestionAdmin)
admin.site.register(Choice)

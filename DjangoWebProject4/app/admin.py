from django.contrib import admin
from app.models import Choice, Poll

class ChoiceInLine(admin.TabularInline):
    model = Choice
    extra = 3

class PollAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['question']}),
        ('Date Information', {'fields': ['pub_date'], 'classes': ['collapse']}),
    ]
    inlines= [ChoiceInLine]
    list_display = ('question', 'pub_date')
    list_filter = ['pub_date']
    search_feilds = ['question']
    date_hierarchy = 'pub_date'

admin.site.register(Poll, PollAdmin)
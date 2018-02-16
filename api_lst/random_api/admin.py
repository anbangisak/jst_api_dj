from django.contrib import admin
from random_api.models import RandomApi

class RandomAdmin(admin.ModelAdmin):
	list_display = ('title', 'language', 'style')

admin.site.register(RandomApi, RandomAdmin)

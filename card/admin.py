from django.contrib import admin

# Register your models here.
from .models import Card, CardTags, Tags

admin.site.register(Card)
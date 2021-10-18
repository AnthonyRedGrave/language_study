from django.contrib import admin
from .models import Card, Collection


@admin.register(Card)
class CardAdmin(admin.ModelAdmin):
    list_display = ("sentence", "translate", "language", "collection")


admin.site.register(Collection)

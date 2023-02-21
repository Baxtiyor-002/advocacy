from django.contrib import admin
from .models import Initiative, Offer
# Register your models here.


class OfferInline(admin.TabularInline):
    model = Offer
    extra = 5


class InitiativeAdmin(admin.ModelAdmin):
    inlines = [OfferInline]


admin.site.register(Initiative, InitiativeAdmin)
admin.site.register(Offer)

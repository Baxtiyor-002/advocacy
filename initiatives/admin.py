from django.contrib import admin
from .models import Initiative, Offer, Comment
# Register your models here.


class OfferInline(admin.TabularInline):
    model = Offer
    extra = 5


class CommentInline(admin.TabularInline):
    model = Comment
    extra = 0

class InitiativeAdmin(admin.ModelAdmin):
    inlines = [OfferInline, CommentInline]


admin.site.register(Initiative, InitiativeAdmin)
admin.site.register(Offer)
admin.site.register(Comment)

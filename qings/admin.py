from django.contrib import admin
from .models import Poet, Quote, Video

# Register your models here.

class PoetAdmin(admin.ModelAdmin):
    readonly_fields = ()

class QuoteAdmin(admin.ModelAdmin):
    readonly_fields = ()

class VideoAdmin(admin.ModelAdmin):
    readonly_fields = ()


admin.site.register(Poet, PoetAdmin)
admin.site.register(Quote, QuoteAdmin)
admin.site.register(Video, VideoAdmin)

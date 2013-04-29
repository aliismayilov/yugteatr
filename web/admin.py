from django.contrib import admin
from web.models import *
from yugteatr import settings


class PageAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}

    class Media:
        js = (
            '//cdnjs.cloudflare.com/ajax/libs/ckeditor/4.0.1/ckeditor.js',
            settings.STATIC_URL + 'js/ckeditor_init.js'
        )


class ActorAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}


class PlayPhotoAdmin(admin.TabularInline):
    model = PlayPhoto


class PlayInformationAdmin(admin.StackedInline):
    model = PlayInformation
    extra = 2


class PlayAdmin(admin.ModelAdmin):
    inlines = [
        PlayInformationAdmin,
        PlayPhotoAdmin
    ]

    class Media:
        js = (
            '//cdnjs.cloudflare.com/ajax/libs/ckeditor/4.0.1/ckeditor.js',
            settings.STATIC_URL + 'js/ckeditor_init.js'
        )


admin.site.register(Page, PageAdmin)
admin.site.register(Language)
admin.site.register(Actor, ActorAdmin)
admin.site.register(Play, PlayAdmin)
admin.site.register(Performance)

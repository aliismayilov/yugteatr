from django.contrib import admin
from web.models import *
from yugteatr import settings


class PageAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}
    list_filter = ('language',)

    class Media:
        js = (
            '//cdnjs.cloudflare.com/ajax/libs/ckeditor/4.0.1/ckeditor.js',
            settings.STATIC_URL + 'js/ckeditor_init.js'
        )

class PersonInformationAdmin(admin.StackedInline):
    model = PersonInformation
    extra = 2


class PersonAdmin(admin.ModelAdmin):
    inlines = [
        PersonInformationAdmin,
    ]

    class Media:
        js = (
            '//cdnjs.cloudflare.com/ajax/libs/ckeditor/4.0.1/ckeditor.js',
            settings.STATIC_URL + 'js/ckeditor_init.js'
        )


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


class PerformanceAdmin(admin.ModelAdmin):
    def formfield_for_manytomany(self, db_field, request, **kwargs):
        if db_field.name == 'performers':
            kwargs['queryset'] = Person.objects.filter(staff_type=Person.PERFORMER)
        elif db_field.name == 'designers':
            kwargs['queryset'] = Person.objects.filter(staff_type=Person.DESIGNER)
        elif db_field.name == 'directors':
            kwargs['queryset'] = Person.objects.filter(staff_type=Person.DIRECTOR)

        return super(PerformanceAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs)


admin.site.register(Page, PageAdmin)
admin.site.register(Language)
admin.site.register(Person, PersonAdmin)
admin.site.register(Play, PlayAdmin)
admin.site.register(Performance, PerformanceAdmin)

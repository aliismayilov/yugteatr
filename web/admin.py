from django.contrib import admin
from web.models import *


class PageAdmin(admin.ModelAdmin):
	prepopulated_fields = {"slug": ("title",)}


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


admin.site.register(Page, PageAdmin)
admin.site.register(Language)
admin.site.register(Actor, ActorAdmin)
admin.site.register(Play, PlayAdmin)
admin.site.register(Performance)

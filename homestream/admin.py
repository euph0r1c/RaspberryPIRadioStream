from django.contrib import admin
from homestream.models import Stream, RadioChannel


class RadioChannelInline(admin.StackedInline):
    model = RadioChannel
    extra = 1


class StreamAdmin(admin.ModelAdmin):
    inlines = [RadioChannelInline]

admin.site.register(Stream, StreamAdmin)

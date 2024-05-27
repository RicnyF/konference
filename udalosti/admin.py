from django.contrib import admin

from udalosti.models import Speaker, Conference, Session

admin.site.register(Speaker)
admin.site.register(Conference)
admin.site.register(Session)
# Register your models here.

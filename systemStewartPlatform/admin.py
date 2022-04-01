from django.contrib import admin
from .models import system_stewart_platform, stewart_platform, law_for_platform


admin.site.register(system_stewart_platform)
admin.site.register(stewart_platform)
admin.site.register(law_for_platform)
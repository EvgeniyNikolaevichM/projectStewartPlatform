from django.contrib import admin
from .models import matrix, stewart_platform, law_for_platform, law_for_system,stewart_platform_system


admin.site.register(matrix)
admin.site.register(stewart_platform)
admin.site.register(law_for_platform)
admin.site.register(law_for_system)
admin.site.register(stewart_platform_system)
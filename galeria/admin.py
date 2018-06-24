from django.contrib import admin
from .models import *

from django.utils.safestring import mark_safe


admin.site.register(Usuario)
admin.site.register(Galeria)
admin.site.register(Foto)

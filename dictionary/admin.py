from django.contrib import admin

from .models import *

admin.site.register(Word)
admin.site.register(Extracted_Word)
admin.site.register(Extracted_frequencies)
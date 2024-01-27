from django.contrib import admin

# Registering the models.
from .models import *

admin.site.register(Profile)
admin.site.register(Members)
admin.site.register(Meeting)
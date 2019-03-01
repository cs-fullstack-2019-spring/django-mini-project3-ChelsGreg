from django.contrib import admin

# FOR MODEL INFO TO REGISTER TO ADMIN SITE
from .models import TimeModel

admin.site.register(TimeModel)
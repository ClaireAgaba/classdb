from django.contrib import admin
from .models import *

# Register your models here.

admin.site.register(Branch)
admin.site.register(Video)
admin.site.register(Rental)
admin.site.register(Member)
admin.site.register(Staff)
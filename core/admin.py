from django.contrib import admin
from .models import Diamond, Rectangle, Square, Triangle

# Register your models here.

admin.site.register(Rectangle)
admin.site.register(Square)
admin.site.register(Diamond)
admin.site.register(Triangle)

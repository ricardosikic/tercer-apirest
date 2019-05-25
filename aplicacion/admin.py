from django.contrib import admin
from .models import User
from .models import Caso

# Register your models here.

class UserAdmin(admin.ModelAdmin):
    list_display = ('name', 'last_name', 'age', 'reg_date')
    

class CasoAdmin(admin.ModelAdmin):
    list_display = ('title', 'document', 'upload_to')
    
    

admin.site.register(User, UserAdmin)
admin.site.register(Caso, CasoAdmin)
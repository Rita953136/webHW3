from django.contrib import admin
from .models import Member
from .models import Court

# Register your models here.
class MemberAdmin(admin.ModelAdmin):
  list_display = ("firstname", "lastname", "joined_date",)

class CourtsAdmin(admin.ModelAdmin):
  list_display = ("courtname", "courttype", "city",)

admin.site.register(Member, MemberAdmin)
admin.site.register(Court, CourtsAdmin)

# admin.site.register(Member)



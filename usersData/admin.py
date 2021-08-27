from usersData.models import OTPModule, info, socialAcc
from django.contrib import admin

# Register your models here.

admin.site.register(socialAcc)
admin.site.register(info)
admin.site.register(OTPModule)
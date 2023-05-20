from usersData.models import AccountSettings, OTPModule, ProfileHitsUser, ProfileReactions, ProfileVisits, info, locationData, registerData, socialAcc, verifiedAccounts
from django.contrib import admin

# Register your models here.

admin.site.register(socialAcc)
admin.site.register(info)
admin.site.register(OTPModule)
admin.site.register(ProfileVisits)
admin.site.register(ProfileHitsUser)
admin.site.register(ProfileReactions)
admin.site.register(verifiedAccounts)
admin.site.register(locationData)
admin.site.register(registerData)
admin.site.register(AccountSettings)

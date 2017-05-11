from django.contrib import admin
from.models import (
	UserProfile,
	JobExperience
	)





class UserProfileAdmin(admin.ModelAdmin):
	List_display = ('user', 'wechat_username', 'phone_number')

class JobExperienceAdmin(admin.ModelAdmin):
	List_display = ('user', 'start_date', 'start_date', 'title', 'company', 'description')

admin.site.register(UserProfile, UserProfileAdmin)
admin.site.register(JobExperience, JobExperienceAdmin)
# Register your models here.

  
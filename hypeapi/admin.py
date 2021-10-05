from django.contrib import admin
from .models import Cohort, Profile, Assignment, Meeting

admin.site.register(Cohort)
admin.site.register(Profile)
admin.site.register(Assignment)
admin.site.register(Meeting)

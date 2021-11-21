from django.contrib import admin
from .models import Announcement, Assignment, Cohort, Meeting, Profile

admin.site.register(Announcement)
admin.site.register(Assignment)
admin.site.register(Cohort)
admin.site.register(Meeting)
admin.site.register(Profile)

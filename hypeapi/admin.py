from django.contrib import admin
from .models import Assignment, Cohort, Meeting, Profile, Submission, Upload

admin.site.register(Assignment)
admin.site.register(Cohort)
admin.site.register(Meeting)
admin.site.register(Profile)
admin.site.register(Submission)
admin.site.register(Upload)

from django.contrib import admin
from .models import Assignment, Cohort, Meeting, Profile

admin.site.register(Assignment)
admin.site.register(Cohort)
admin.site.register(Meeting)
admin.site.register(Profile)

from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.mail import send_mail
from .cohort import Cohort
from .profile import Profile


class Announcement(models.Model):
    subject = models.CharField(max_length=200)
    text = models.TextField()
    cohort = models.ForeignKey(Cohort, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.subject


@receiver(post_save, sender=Announcement)
def send_email_notification(sender, instance, created, **kwargs):
    if created:
        user_list = Profile.objects.filter(cohorts__in=[instance.cohort])
        email_list = [profile.user.email for profile in user_list]
        send_mail(instance.subject, instance.text, 'mail@gethype.org', recipient_list=email_list, fail_silently=True)

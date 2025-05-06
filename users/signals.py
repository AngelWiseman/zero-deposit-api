from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth import get_user_model
from django.contrib.auth.models import Group

User = get_user_model()

@receiver(post_save, sender=User)
def add_user_to_default_group(sender, instance, created, **kwargs):
    if created:
        try:
            default_group, _ = Group.objects.get_or_create(name='property_editors')
            instance.groups.add(default_group)
        except Exception as e:
            print(f"Error adding user to default group: {e}")

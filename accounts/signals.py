from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver
from accounts.models import User, UserProfile

@receiver(post_save, sender=User)
def post_save_create_userprofile(sender, instance, created, **kwargs):
    
    if created:
        UserProfile.objects.create(user=instance)
        
    else:
        try:
            profile=UserProfile.objects.get(user=instance)
            profile.save()
            
        except:
            UserProfile.objects.create(user=instance)
            

@receiver(pre_save, sender=User)
def pre_save_profile_recevier(sender, instance, **kwargs):
    print(instance.username, " the user being saved from godzilla")
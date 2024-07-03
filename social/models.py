from django.db import models

# Create your models here.
class UserProfile(models.Model):
    
    user = models.OneToOneRel(User,on_delete=models.CASCADE)
    loc = models.CharField(max_length=20,blank=True)
    bio = models.TextField(max_length=300,blank=True)
    img = models.ImageField(upload_to='pics',default='avatar.jpg')
    
    def __str__(self):
        return self.user.username+'profile'
    
class UserPost(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    post = models.TextField(max_length=300,blank=False)
    data = models.DataTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.user.username+'post'

@receiver(post_save,sender=User)
def create_user_profile(sender,instance,created,**kwargs):
    if created:
        UserProfile.objects.create(user=instance)

@receiver(post_save,sender=User)
def save_user_profile(sender,instance,**kwargs):
    instance.userprofile.save()

from django.db import models
from taggit.managers import TaggableManager
from django.conf import settings

User=settings.AUTH_USER_MODEL

# Create your models here.
def user_directory_path(instance,filename):
    return f"user_{instance.user.id}/{filename}"

VISIBILITY = (
    ('private','Private'),
    ('unlisted','Unlisted'),
    ('members_only','Members Only'),
    ('public','Public'),
)

class Video(models.Model):
    video = models.FileField(upload_to=user_directory_path)
    image = models.ImageField(upload_to=user_directory_path, blank= True, null=True)
    title = models.CharField(max_length=100)
    description = models.TextField(null=True, blank=True)
    tags = TaggableManager()
    date = models.DateTimeField(auto_now_add=True)
    visibility = models.CharField(choices=VISIBILITY,max_length=100,default='public')
    user = models.ForeignKey(User,on_delete=models.CASCADE, null=True)
    views = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.title

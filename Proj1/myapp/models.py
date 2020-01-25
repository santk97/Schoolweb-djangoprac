from django.db import models


# Create your models here.
class User_model(models.Model):
    name = models.CharField(max_length=120,blank=False)
    email = models.EmailField(unique=True,blank=False)
    username = models.CharField(max_length=120,unique=True,blank=False)
    password = models.CharField(max_length=400,blank=False)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    is_active=models.BooleanField(default=False)

    def __str__(self):
        return self.username

import uuid
class session_token(models.Model):
        username = models.ForeignKey(User_model,on_delete=models.CASCADE)
        token = models.CharField(max_length=250)
        created_on = models.DateTimeField(auto_now_add=True)
        valid = models.BooleanField(default=True)

        def create_token(self):
            self.token = uuid.uuid4()

        def __str__(self):
            return self.username

class PostModel(models.Model):
	user = models.ForeignKey(User_model,on_delete=models.CASCADE)
	image = models.FileField(upload_to='user_images')
	image_url = models.CharField(max_length=255)
	caption = models.CharField(max_length=240)
	created_on = models.DateTimeField(auto_now_add=True)
	updated_on = models.DateTimeField(auto_now=True)
	has_liked = models.BooleanField(default=False)

	def __str__(self):
		return self.caption



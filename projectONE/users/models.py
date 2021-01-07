from django.db import models
from django.contrib.auth.models import User
from PIL import Image

"""
 Here the models being created are for the ability of the user to
 add a profile. 
 ---------------------------------------------------|
 Profile Picture Models Set up.                     |
 ___________________________________________________|
 1. Import User module from the 'django.contrib.auth.models directory.
 2. Create a class and name it Profile. Pass in a models.Model parameter
 3. set a user variable euqal to the type of model module know as 'models.OneToOneField(User, on_delete=models.CASCADE)'
 4. set an image variable to 'models.ImageField(default='default.jpg', upload_to='profile_pics')' as well.
 5. You must also return the user profile in a HTML rendered element. For this you must invoke the __str__ string.
 6. Also recall to register the model created in the admin.py file.
 7. For this to be fully operational you need to also install the Pillow framework. A library used for image processing.
 8. After all steps are completed you may makemigations
 

"""
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='--default.jpg', upload_to='profile_pics')


#The __str__ is a function that returns a string to be rendered in HTML.
#So in this case it is returning the user profile.
    def __str__(self):
        return f'{self.user.username} Profile'
    
    def save(self):
        super().save()

        img = Image.open(self.image.path)
        #The conditional statement below checks for the imgae size
        #And outputs the correct size.
        #This will need the 'Image' module from the pillow python library
        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.image.path)

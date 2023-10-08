from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser


# Create your models here.

# User Model Manager
class UserManager(BaseUserManager):
    def create_user(self, email, first_name, last_name, password=None, password2=None):
       
        if not email:
            raise ValueError("Users must have an email address")

        user = self.model(
            email=self.normalize_email(email),
            first_name = first_name,
            last_name = last_name,
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, first_name, last_name, password=None, password2=None):
        user = self.create_user(
            email,
            password=password,
            first_name=first_name, 
            last_name=last_name,
        )
        user.is_admin = True
        user.save(using=self._db)
        return user

# User Model
class User(AbstractBaseUser):

    first_name = models.CharField('first_name', max_length=60, blank=False)
    last_name = models.CharField('last_name', max_length=60, null=True, blank=True)
    email = models.EmailField('Email', max_length=255, null=False, blank=False, unique=True)
    create_at = models.DateTimeField('create_at', null=False, blank=False, auto_now_add=True)
    update_at = models.DateTimeField('update_at', null=True, blank=True, auto_now=True)
   
    
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["first_name", "last_name"]

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return self.is_admin

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True

    @property
    def is_staff(self):
        "Is the user a member of staff?"
        # Simplest possible answer: All admins are staff
        return self.is_admin

class Media(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    media = models.FileField('Media', upload_to='video', blank=True, null=True)
    
    

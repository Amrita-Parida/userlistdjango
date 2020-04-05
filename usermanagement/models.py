import uuid
from .utils import NAME_REGEX
from django.db import models
from django.conf import settings
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser


class AbstractTime(models.Model):
    created_at = models.DateTimeField("Created Date", auto_now_add=True)
    updated_at = models.DateTimeField("Updated Date", auto_now=True)

    class Meta:
        abstract = True


# Create your models here.
class MyUserManager(BaseUserManager):

    def create_user(self, email, password, user_name):
        """
        Creates and saves a User with the given email, user_name and password.
        """
        if not email:
            raise ValueError('Users must have an Email Address')

        user = self.model(
            email=self.normalize_email(email),
            user_name=user_name,
            is_active=False,
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password,user_name):
        """Create superuser"""
        user = self.model(email=email, user_name=user_name)
        user.set_password(password)
        user.is_superuser = True
        user.is_active = True
        user.is_staff = True
        user.save(using=self._db)
        return user


class MyUser(AbstractBaseUser, AbstractTime):
    """
    User Model in order to save user details
    """
    uuid = models.UUIDField(default=uuid.uuid4, editable=False)
    user_name = models.CharField(
        'Username', max_length=256, unique=True, null=True, blank=True,)
    email = models.EmailField(
        "Email Address", null=True, unique=True, blank=True,)
    is_superuser = models.BooleanField("Super User", default=False)
    is_online = models.BooleanField("Online", default=False)
    is_staff = models.BooleanField("Staff", default=False)
    is_active = models.BooleanField("Active", default=False)

    objects = MyUserManager()
    EMAIL_FIELD = 'email'
    USERNAME_FIELD = 'user_name'
    REQUIRED_FIELDS = ['email', ]


    def has_perm(self, perm, obj=None):
        return self.is_staff

    def has_module_perms(self, app_label):
        return self.is_superuser

    def get_short_name(self):
        return self.email

    class Meta:
        verbose_name_plural = "User Management"
        ordering = ('-id',)

class ActivityPeriod(models.Model):
    """Model to show the User Activity Period"""
    user = models.ForeignKey(MyUser,on_delete=models.CASCADE,related_name='user_activity')
    start_time = models.DateTimeField("Start Time")
    end_time = models.DateTimeField("End Time")

    def __str__(self):
        return str(self.user)

    class Meta:
        verbose_name_plural = "User Activity Period"
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

class StudentManager(BaseUserManager):
    def create_user(self, reg_number, full_name, institution_code, password=None):
        if not reg_number:
            raise ValueError("Registration number is required")
        user = self.model(
            reg_number=reg_number,
            full_name=full_name,
            institution_code=institution_code,
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, reg_number, full_name, institution_code, password):
        user = self.create_user(reg_number, full_name, institution_code, password)
        user.is_admin = True
        user.save(using=self._db)
        return user

class Student(AbstractBaseUser):
    reg_number = models.CharField(max_length=20, unique=True)
    full_name = models.CharField(max_length=100)
    institution_code = models.CharField(max_length=20)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)

    objects = StudentManager()

    USERNAME_FIELD = 'reg_number'
    REQUIRED_FIELDS = ['full_name', 'institution_code']

    def __str__(self):
        return self.reg_number

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True

    @property
    def is_staff(self):
        return self.is_admin
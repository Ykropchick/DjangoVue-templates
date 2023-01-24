from django.db import models
from django.contrib.auth.models import (
    BaseUserManager, AbstractBaseUser
)


class UserManager(BaseUserManager):
    def create_user(self, phone, username, password=None):
        """
        Creates and saves a User with the given phone and password.
        """
        if not phone or not username:
            raise ValueError('Users must have an phone ')

        user = self.model(
            phone=phone,
            username=username
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_staffuser(self, phone, username, password):
        """
        Creates and saves a staff user with the given phone and password.
        """
        user = self.create_user(
            username=username,
            phone=phone,
            password=password,
        )
        user.staff = True
        user.approved = True
        user.save(using=self._db)
        return user

    def create_superuser(self, phone, username, password):
        """
        Creates and saves a superuser with the given phone and password.
        """
        user = self.create_user(
            username=username,
            phone=phone,
            password=password,
        )
        user.staff = True
        user.admin = True
        user.approved = True
        user.save(using=self._db)
        return user

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'


def upload_to(instance, filename):
    return 'images/{filename}'.format(filename=filename)


class User(AbstractBaseUser):
    username = models.CharField(max_length=30, unique=True, verbose_name="Имя пользователя")
    time_registrate = models.DateField(auto_now_add=True, blank=True, null=True, verbose_name="Дата регистрации")
    phone = models.CharField(max_length=20, unique=True, verbose_name="телефон")
    avatar = models.ImageField(upload_to=upload_to, blank=True, null=True, verbose_name="Аватар")
    approved = models.BooleanField(default=False, verbose_name="верифицирован")
    banned = models.BooleanField(default=False, verbose_name="забанен")
    staff = models.BooleanField(default=False, verbose_name="сотрудник")  # a admin user; non super-user
    admin = models.BooleanField(default=False, verbose_name="админ")  # a superuser

    last_login = None



    # notice the absence of a "Password field", that is built in.

    USERNAME_FIELD = 'phone'
    REQUIRED_FIELDS = ['username']

    objects = UserManager()

    def get_full_name(self):
        # The user is identified by their phone
        return self.phone

    def get_short_name(self):
        # The user is identified by their phone
        return self.phone

    def __str__(self):
        return self.username

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return True

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True

    @property
    def is_staff(self):
        "Is the user a member of staff?"
        return self.staff

    @property
    def is_admin(self):
        "Is the user a admin member?"
        return self.admin
import jwt, uuid
from datetime import datetime, timedelta
from django.conf import settings
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.db import models
from django.utils.translation import gettext_lazy as _

from . import choices


class UserManager(BaseUserManager):
    def create_user(self, username, email, password=None):
        """
        Создает и возвращает пользователя с имэйлом, паролем и именем.
        """
        if username is None:
            raise TypeError('Users must have a username.')

        if email is None:
            raise TypeError('Users must have an email address.')

        user = self.model(username=username, email=self.normalize_email(email))
        user.set_password(password)
        user.save()

        return user

    def create_superuser(self, username, email, password):
        """
        Создает и возвращет пользователя с привилегиями суперадмина.
        """
        if password is None:
            raise TypeError('Superusers must have a password.')

        user = self.create_user(username, email, password)
        user.is_superuser = True
        user.is_staff = True
        user.save()

        return user


class User(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(db_index=True, max_length=255, unique=True)
    email = models.EmailField(db_index=True, unique=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    objects = UserManager()

    class Meta:
        ordering = ('-created_at',)
        verbose_name = _('Пользователь')
        verbose_name_plural = _('Пользователи')

    def __str__(self):
        return self.email

    @property
    def token(self):
        return self._generate_jwt_token()

    def get_full_name(self):
        return self.username

    def get_short_name(self):
        return self.username

    def _generate_jwt_token(self):
        """
        Генерирует веб-токен JSON, в котором хранится идентификатор этого
        пользователя, срок действия токена составляет 1 день от создания
        """
        dt = datetime.now() + timedelta(days=1)

        token = jwt.encode({
            'id': self.pk,
            'exp': int(dt.strftime('%s'))
        }, settings.SECRET_KEY, algorithm='HS256')

        # return token.decode('utf-8')
        return token


class Feedback(models.Model):
    id = models.AutoField(primary_key=True)
    user_id = models.ForeignKey(
        to=User,
        on_delete=models.CASCADE,
        related_name='user_feedbacks',
        verbose_name=_('Пользователь')
    )
    title = models.CharField(max_length=255)
    text = models.TextField()

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ("-created_at",)
        verbose_name = _('Отзыв')
        verbose_name_plural = _('Отзывы')

    def __str__(self):
        return f"{self.user_id} - {self.title}"


class Discount(models.Model):
    id = models.AutoField(primary_key=True)
    user_id = models.OneToOneField(
        to=User,
        on_delete=models.CASCADE,
        related_name='user_discounts',
        verbose_name=_('Пользователь')
    )
    tickets_bought = models.PositiveIntegerField(verbose_name=_('Количество купленных билетов'))
    discount_count = models.DecimalField(max_digits=8, decimal_places=2, default=0, verbose_name='Сумма бонусов')

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = _('Бонус')
        verbose_name_plural = _('Бонусы')

    def __str__(self):
        return f"{self.user_id} - {self.discount_count}"


class PurchaseHistory(models.Model):
    id = models.AutoField(primary_key=True)
    ticket_id = models.OneToOneField(
        to=User,
        on_delete=models.CASCADE,
        related_name='ticket_purchases',
        verbose_name=_('Пользователь')
    )
    pay_status = models.CharField(
        choices=choices.PayStatuses.choices,
        max_length=50,
        verbose_name=_('Статус покупки')
    )
    user_id = models.ForeignKey(
        to=User,
        on_delete=models.CASCADE,
        related_name='user_purchases',
        verbose_name=_('Пользователь')
    )
    price = models.DecimalField(max_digits=8, decimal_places=2, verbose_name=_('Сумма'))
    discount_used = models.DecimalField(max_digits=8, decimal_places=2, verbose_name=_('Сумма использованных бонусов'))
    discount_added = models.DecimalField(max_digits=8, decimal_places=2, verbose_name=_('Сумма дополненных бонусов'))

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ("-created_at",)
        verbose_name = _('История покупок')
        verbose_name_plural = _('Истории покупок')

    def __str__(self):
        return f"{self.ticket_id}, {self.user_id} - {self.pay_status}"


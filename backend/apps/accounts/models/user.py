from django.db import models
from django.core.mail import send_mail
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.base_user import AbstractBaseUser
from django.utils.translation import gettext_lazy as _

from .managers import CustomUserManager


class User(AbstractBaseUser, PermissionsMixin):
    """ Modelo de Usuário customizado onde o campo de login é o email. """
    email = models.EmailField(_('endereço de email'), unique=True)
    first_name = models.CharField(_('primeiro nome'), max_length=300, blank=True)
    last_name = models.CharField(_('sobrenome'), max_length=300, blank=True)
    date_joined = models.DateTimeField(_('data de cadastro'), auto_now_add=True)
    is_active = models.BooleanField(_('ativo'), default=True)
    is_staff = models.BooleanField(_('equipe'), default=False)

    objects = CustomUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name']

    class Meta:
        verbose_name = _('usuário')
        verbose_name_plural = _('usuários')
        db_table = 'accounts_user'

    def __str__(self):
        return self.get_full_name().upper() if self.get_full_name() else self.email

    def get_full_name(self):
        """ Retorna o nome completo. """
        full_name = '%s %s' % (self.first_name, self.last_name)
        return full_name.strip()

    def get_short_name(self):
        """ Retorna o primeiro nome (nome curto). """
        return self.first_name

    def email_user(self, subject, message, from_email=None, **kwargs):
        """ Envia um email para este Usuário. """
        send_mail(subject, message, from_email, [self.email], **kwargs)

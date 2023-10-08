from django.conf import settings
from django.core.mail import send_mail
from django.db import models
from django.http import BadHeaderError, HttpResponse
from django.urls import reverse
from django.utils.timezone import now



class Profile(models.Model):
    objects = models.Manager()
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    avatar = models.ImageField(default='no-image-available.jpg', blank=True)
    first_name = models.CharField(max_length=200, null=True, blank=True)
    last_name = models.CharField(max_length=200, null=True, blank=True)
    email = models.EmailField(max_length=200, null=True, blank=True, verbose_name='Email')
    username = models.CharField(max_length=200, null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    phone = models.CharField(max_length=100, verbose_name='Phone')
    slug = models.SlugField()

    def __str__(self):
        return self.username



class EmailVerification(models.Model):
    code = models.UUIDField(unique=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    expiration = models.DateTimeField()

    def __str__(self):
        return f"EmailVerification object for {self.user.email}"

    class Meta:
        verbose_name = "верификацию"
        verbose_name_plural = "Верификация по почте"



    def send_verification_email(self):
        link = reverse('email_verification', kwargs={'email': self.user.email, 'code': self.code})
        verification_link = f"{settings.DOMAIN_NAME}{link}"
        subject = f"Подтверждение учётной записи для {self.user.username}"
        message = f"для подтверждение учётной записи {self.user.email} перейдите по ссылке {verification_link}"
        try:
            send_mail(
                "Subject here",
                message,
                settings.EMAIL_HOST_USER,
                [self.user.email],
                fail_silently=False,
            )
        except BadHeaderError:
            return HttpResponse("Обнаружен неверный заголовок")

    def is_expired(self):
        return True if now() >= self.expiration else False

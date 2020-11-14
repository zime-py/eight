from django.contrib.auth.forms import (UserCreationForm as DjangoUserCreationForm)
from django.contrib.auth.forms import UsernameField
from . import models

class UserCreationForm(DjangoUserCreationForm):
    class Meta(DjangoUserCreationForm.Meta):
        model = models.User
        fields = ("email",)
        field_classes = {"email": UsernameField}
    def send_mail(self):
        logger.info("Sending signup email for email=%s",
        self.cleaned_data["email"],
        )
        message = "Welcome{}".format(self.cleaned_data["email"])
        send_mail(
            "Welcome to BookTime",
            message,
            "site@booktime.domain",
            [self.cleaned_data["email"]],
            fail_silently=True,
        )
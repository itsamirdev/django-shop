from django.contrib.auth.models import BaseUserManager


class UserManager(BaseUserManager):
    def create_user(self, phone_number, email, fullname, password):
        user = self.model(phone_number=phone_number, email=self.normalize_email(email), fullname=fullname)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, phone_number, email, fullname, password):
        user = self.create_user(phone_number, email, fullname, password)
        user.is_admin = True
        user.save(using=self._db)
        return True

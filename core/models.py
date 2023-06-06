from django.db import models

class Problem(models.Model):
    name = models.CharField(max_length=100, verbose_name='नाम')
    phone = models.CharField(max_length=20, verbose_name='फ़ोन')
    address = models.CharField(max_length=200, verbose_name='पता')
    gav = models.CharField(max_length=100, verbose_name='गांव')
    problem = models.TextField( verbose_name='समस्या')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_solved = models.BooleanField(default=False)
    is_spam = models.BooleanField(default=False)

    def __str__(self):
        return self.name

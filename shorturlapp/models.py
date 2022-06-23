from django.db import models
import os
import hashlib
import binascii


class ShortUrl(models.Model):
    id = models.AutoField(primary_key=True)
    created_at = models.DateTimeField(auto_now_add=True)
    original_url = models.URLField()
    shorted_url = models.URLField(unique=True, blank=True)
    shares = models.PositiveIntegerField(default=0)
    url_context = models.CharField(max_length=20, default='0', blank=True)  # храним ссылку, что получили из хэша

    class Meta:
        app_label = 'shorturlapp'
        ordering = ["-shares"]

    def __str__(self):
        return f'{self.shorted_url}'

    def increment_shares(self):
        self.shares += 1
        super(ShortUrl, self).save()

    def save(self, *args, **kwargs):
        url_hash = self.salt_and_hash(self.original_url)
        self.shorted_url = "".join(['http://127.0.0.1:8000/short/', url_hash])
        self.url_context = url_hash
        super(ShortUrl, self).save(*args, **kwargs)
        return self.shorted_url

    def salt_and_hash(self, original_url):
        salt = os.urandom(64)
        my_hash = hashlib.pbkdf2_hmac('sha256', original_url.encode('utf-8'), salt, 10000, 7)
        return str(binascii.hexlify(my_hash))[2:-1]

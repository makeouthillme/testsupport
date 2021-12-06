from django.db import models


class Post(models.Model):
    name = models.CharField(max_length=255)
    question = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    answer = models.TextField(help_text='For the support', blank=True,)
    resolved = 'Resolved'
    unresolved = 'Unresolved'
    freez = 'Frozen'
    wait = 'Waiting for an answer'
    STATUS_CHOICES = [
        (wait, 'Waiting for an answer'),
        (resolved, 'Resolved'),
        (unresolved, 'Unresolved'),
        (freez, 'Frozen'),
    ]
    status = models.CharField(max_length=30, choices=STATUS_CHOICES, default=wait)

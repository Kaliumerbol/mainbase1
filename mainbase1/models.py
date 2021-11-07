from django.db import models
from django.contrib.auth import  get_user_model

User = get_user_model()

class Mainbase1(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='mainbase1', null=True)
    reg_id = models.IntegerField(auto_created=True)
    register_at = models.DateTimeField(auto_now_add=True)
    pr_name = models.TextField()
    pr_zacaz = models.TextField()
    pr_proectir = models.TextField()
    finished_at = models.DateTimeField(null=True)
    is_finished = models.BooleanField(default=False)
    estimated_finish_time = models.DateTimeField()
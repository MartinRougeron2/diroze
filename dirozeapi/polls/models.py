from django.db import models
from auth.models import authUser

class Poll(models.Model):
    question = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(authUser, related_name='polls', on_delete=models.CASCADE)

    def __str__(self):
        return self.question
    
class Choice(models.Model):
    poll = models.ForeignKey(Poll, related_name='choices', on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=255)
    votes = models.IntegerField(default=0)
    voted_by = models.ManyToManyField(authUser, related_name='choices')

    def __str__(self):
        return self.choice_text
    

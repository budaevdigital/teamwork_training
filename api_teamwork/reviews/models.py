from django.db import models
from api_teamwork.users.models import CustomUser


class Score(models.Model):
    CHOICES = [(i, i) for i in range(11)]
    score_field = models.IntegerField(choices=CHOICES)
    voted_on = models.DateTimeField(auto_now=True)


class Reviews(models.Model):
    title = models.CharField(max_length=200)
    text = models.TextField()
    pub_date = models.DateTimeField(auto_now_add=True)
    upd_date = models.DateTimeField(auto_now=True)
    score = models.ForeignKey(Score, on_delete=models.CASCADE)
    author = models.ForeignKey(CustomUser, on_delete=models.CASCADE)

    class Meta:
        unique_together = ('author', 'score')


class Comment(models.Model):
    post = models.ForeignKey(Reviews,
                             related_name='comments',
                             on_delete=models.CASCADE)
    name = models.CharField(max_length=80)
    email = models.EmailField()
    body = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)

    class Meta:
        ordering = ('created',)

    def __str__(self):
        return 'Comment by {} on {}'.format(self.name, self.post)

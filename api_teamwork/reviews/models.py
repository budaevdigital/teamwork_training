from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from api_teamwork.settings import AUTH_USER_MODEL 


class Score(models.Model):
    score_field = models.IntegerField('Оценка',validators=(
            MinValueValidator(1),
            MaxValueValidator(10)),
        error_messages={'validators': 'Допустимая оценка от 1 до 10!'})
    voted_on = models.DateTimeField(auto_now=True)


class Reviews(models.Model):
    title = models.CharField(max_length=200)
    text = models.TextField()
    pub_date = models.DateTimeField(auto_now_add=True)
    upd_date = models.DateTimeField(auto_now=True)
    score = models.ForeignKey(Score, on_delete=models.CASCADE)
    author = models.ForeignKey(AUTH_USER_MODEL, on_delete=models.CASCADE)

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

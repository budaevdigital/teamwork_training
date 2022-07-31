from django.db import models


class Reviews(models.Model):
    title = models.CharField(max_length=200)
    text = models.TextField()
    pub_date = models.DateTimeField(auto_now_add=True)
    rating = models.IntegerField(default=0, null=True, blank=True)


class Score(models.Model):
    CHOICES = [(i, i) for i in range(11)]
    score_field = models.IntegerField(choices=CHOICES)
    review = models.ForeignKey(Reviews, on_delete=models.CASCADE)
    voted_on = models.DateTimeField(auto_now=True)

    class Meta:
        unique_together = ('review',)


class Comment(models.Model):
    post = models.ForeignKey(
                            Reviews,
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

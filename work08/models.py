from django.db import models


class memo(models.Model):
    memo_title = models.CharField(max_length=100)
    memo_content = models.TextField(blank=True)
    memo_image = models.ImageField(upload_to="memo_images/", blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.memo_title

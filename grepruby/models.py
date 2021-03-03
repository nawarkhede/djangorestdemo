from django.db import models

# Create your models here.


class Article(models.Model):
    created_on = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=30)
    description = models.CharField(max_length=100)
    publish_date = models.DateTimeField(null=True)
    author_name = models.CharField(max_length=30)

    def __str__(self):
        return f"{self.title}: {self.author_name}"

    class Meta:
        unique_together = ("title", "author_name")


class Tag(models.Model):
    article = models.ForeignKey(
        Article, on_delete=models.CASCADE, related_name="tags", null=True
    )
    name = models.CharField(max_length=10)

    def __str__(self):
        return f"{self.name}"

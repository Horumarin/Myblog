# models.py
from django.db import models
from django.utils import timezone
from markdownx.models import MarkdownxField
from markdownx.utils import markdown


class BlogPost(models.Model):
    CHOICES = [
        ("", "選択肢から選んでください"),
        ("Python", "Python"),
        ("Django", "Django"),
        ("FrontEnd", "FrontEnd"),
        ("GO", "GO"),
        ("その他", "その他"),
    ]
    choice = models.CharField(max_length=20, choices=CHOICES, default="")
    title = models.CharField(max_length=200)
    content = MarkdownxField()
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)  # 投稿者をユーザーに紐づけ

    def formatted_markdown(self):
        return markdown(
            self.content, extras=["fenced-code-blocks", "code-friendly", "tables"]
        )

    def __str__(self):
        return self.title

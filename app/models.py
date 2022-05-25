from django.db import models
import uuid
from django.utils.text import slugify
from tinymce import models as tinymce_models

class Article(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=400, blank=False, null=False)
    header_image_url = models.URLField(blank=False, null=False)
    published_date = models.DateField(auto_now_add=True, editable=False)
    draft = models.BooleanField(default=True)
    top_post = models.BooleanField(default=False)
    content = tinymce_models.HTMLField()
    slug = models.SlugField(unique=True, db_index=True, blank=True, max_length=255)

    def __str__(self):
        return self.title
    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Article, self).save(*args, **kwargs)    
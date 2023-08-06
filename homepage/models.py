from django.db import models

# Create your models here.

import uuid
from django.db import models
from imagekit.models import ProcessedImageField
from imagekit.processors import ResizeToFit

class Slide(models.Model):
    title = models.CharField(max_length=70)
    description = models.TextField(max_length=1024, null=True, blank=True)
    image = ProcessedImageField(upload_to='albums', processors=[ResizeToFit(1280)], format='JPEG', options={'quality': 100})
    created = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField(max_length=70, default=uuid.uuid4, editable=False)

    def __unicode__(self):
        return self.title
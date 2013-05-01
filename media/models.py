from django.db import models
from datetime import datetime

class Media(models.Model):

    file = models.FileField(upload_to="media")
    title = models.CharField(max_length=255, blank=True)
    date_added = models.DateTimeField(default=datetime.now(), blank=True, null=True)

    def __unicode__(self):
        return self.file.name

    @models.permalink
    def get_absolute_url(self):
        return ('upload-new')

    def save(self, *args, **kwargs):
        self.date_added = datetime.now()
        self.title = self.file.name
        super(Media, self).save(*args, **kwargs)

    def delete(self, *args, **kwargs):
        self.file.delete(False)
        super(Media, self).delete(*args, **kwargs)

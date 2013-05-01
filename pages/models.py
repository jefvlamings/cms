from django.db import models
from django.forms import ModelForm, DateInput, Textarea, TextInput, CheckboxInput
from datetime import datetime


# Create your models here.
class Page(models.Model):

    # Fields
    parent = models.ForeignKey('self', related_name='children', blank=True, null=True)
    path = models.CharField(max_length=255)
    title = models.CharField(max_length=255)
    text = models.TextField()
    date_added = models.DateTimeField(default=datetime.now(), blank=True, null=True)
    date_modified = models.DateTimeField(blank=True, null=True)
    published = models.BooleanField()
    deletable = models.BooleanField()
    order = models.IntegerField(blank=True, null=True)

    # Readable representation of the object
    def __unicode__(self):
        return self.title

    # The tree structure of a page
    def as_tree(self):
        children = list(self.children.all())
        branch = bool(children)
        yield branch, self
        for child in children:
            for next in child.as_tree():
                yield next
        yield branch, None

    # Overwrite the save method
    def save(self, *args, **kwargs):
        self.date_modified = datetime.now()
        super(Page, self).save(*args, **kwargs)


# Create Model Form
class PageForm(ModelForm):

    class Meta:
        model = Page
        fields = ('title', 'text', 'parent','date_modified', 'date_added')
        widgets = {
            'title': TextInput(attrs={'placeholder': 'Een nieuwe titel'}),
            'text': Textarea(attrs={'rows': 20, 'placeholder': 'Typ hier uw tekst in'}),
            'date_added': DateInput(attrs={'type': 'date'}),
            'date_modified': DateInput(attrs={'type': 'date'}),
        }
    def __init__(self, *args, **kwargs):
        super(PageForm, self).__init__(*args, **kwargs)
        self.fields['date_added'].widget.format = '%Y-%m-%d'
        self.fields['date_modified'].widget.format = '%Y-%m-%d'
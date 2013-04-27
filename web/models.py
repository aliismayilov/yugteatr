from django.db import models

class Language(models.Model):
    name = models.SlugField(max_length=10, unique=True)
    order = models.IntegerField(null=True, blank=True) # optional order field

    class Meta:
        ordering = ['order']

    def __unicode__(self):
        return self.title

    def get_absolute_url(self):
        return '/%s' % self.name

class Page(models.Model):
    title = models.CharField(max_length=50)
    slug = models.SlugField(max_length=50, unique=True)
    body = models.TextField()
    language = models.ForeignKey('Language')

    url = models.CharField(max_length=200, blank=True, null=True)
    order = models.IntegerField(null=True, blank=True) # optional order field

    # parent page
    parent = models.ForeignKey('self', null=True, blank=True)

    class Meta:
        ordering = ['order']

    def __unicode__(self):
        return self.title

    def get_absolute_url(self):
        if self.url:
            return self.url
        else:
            return '/%s/%s.html' % (self.language, self.slug)

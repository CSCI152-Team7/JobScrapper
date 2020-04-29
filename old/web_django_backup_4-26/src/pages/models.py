from django.db import models

# Create your models here.

class glassdoor(models.Model):
    key = models.DecimalField(max_digits=19, decimal_places=10)
    jobTitle = models.TextField()
    description = models.TextField()
    place = models.TextField()
    link = models.URLField()
    site = models.TextField()

    def __unicode__(self):
        return u'%s,%s, %s, %s, %s, %s' % (self.key,self.jobTitle, self.description, self.place,self.link, self.site)

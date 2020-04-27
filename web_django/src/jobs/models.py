from django.db import models

# Create your models here.
class jobsInfo(models.Model):
    JobTitle = models.TextField()
    organization = models.TextField()
    description = models.TextField()
    salary = models.TextField()
    place = models.TextField()
    link = models.URLField()
    site = models.TextField()

    #def __unicode__(self):
        #return u'%s,%s, %s, %s, %s, %s' % (self.key,self.jobTitle, self.description, self.place,self.link, self.site)
    def __str__(self):
        return self.JobTitle

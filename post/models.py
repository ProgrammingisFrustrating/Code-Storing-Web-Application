from django.db import models

# Create your models here.
class Language(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class CodeModel(models.Model):
    name = models.CharField(max_length=200)
    desc = models.TextField()
    lang = models.ForeignKey(Language, null=True, on_delete= models.SET_NULL)
    files = models.FileField(null=True, upload_to='media')
    status = models.BooleanField(default=False)

    def __str__(self):
        return self.name

    def delete(self,*args, **kwargs):
        self.files.delete()
        super().delete(*args, **kwargs)
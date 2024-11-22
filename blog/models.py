from django.db import models
from django.urls import reverse
from django.core.validators import MinLengthValidator

# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=80)

    first_name = models.CharField(max_length=80, null=True)
    last_name = models.CharField(max_length=80, null=True)
    e_mail_address = models.EmailField(null=True)

    excerpt = models.CharField(max_length=100)
    image = models.ImageField(upload_to="images", null=True)
    date = models.DateField(auto_now=True)

    slug = models.SlugField(unique=True,db_index=True)
    content = models.TextField(validators=[MinLengthValidator(10)])
    caption = models.CharField(max_length=20, null=True)

    views = models.IntegerField(null= True)
    like = models.IntegerField(null=True)
    comments = models.IntegerField(null=True)

    def get_absolute_url(self):
        return reverse("post-detail-page", args=[self.slug])
    
    def __str__(self):
        return self.title

class CommentSectionModel(models.Model):
    nome_utente = models.CharField(max_length=100)
    rating = models.IntegerField()
    commento = models.TextField()

    slug = models.SlugField(null=True)
    comment = models.ManyToManyField(Post)
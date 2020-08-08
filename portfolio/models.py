from django.db import models

# Create your models here.

class Profile(models.Model):
    """Profile - main table"""
    full_name = models.CharField(verbose_name='full name', max_length=200)
    profile_img = models.ImageField(verbose_name='profile image', upload_to = 'profile/main' )
    what_I_do = models.CharField(verbose_name='What I do', max_length=200)

    def __str__(self):
        return self.full_name

class About(models.Model):
    """Section About"""
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE, null=True)
    sentence = models.CharField(max_length=200)
    hidden = models.BooleanField(default=False)

    def __str__(self):
        return self.sentence


class Skill(models.Model):
    """Section About"""
    name = models.CharField(max_length=200, unique=True)
    
    def __str__(self):
        return self.name


class Expertise(models.Model):
    """Section About"""
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE, null=True)
    text = models.CharField(max_length=200)
    cv = models.FileField(upload_to='pdf/cv' )
    skills = models.ManyToManyField(Skill)
    slug = models.SlugField(unique=True)
    
    def __str__(self):
        return self.slug


class Achievement(models.Model):
    """Section About"""
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE, null=True)
    name = models.CharField(max_length=200)
    pdf = models.FileField(upload_to='pdf/achievements' )
    url = models.URLField(blank=True)
    slug = models.SlugField(unique=True, null=True)

    def __str__(self):
        return self.name


class Project(models.Model):
    """Section Projects"""
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE, null=True)
    title = models.CharField(max_length=20, default='comming soon ...')
    description = models.CharField(max_length=50, default='cooming soon ...')
    slug = models.SlugField(unique=True, null=True)
    url = models.URLField(null=True)
    image = models.ImageField(upload_to='projects_img')

    def __str__(self):
        return self.title


class Message(models.Model):
    """Section Contact"""
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE, null=True)
    name = models.CharField(max_length=100)
    subject = models.CharField(max_length=200)
    email = models.EmailField(max_length=200)
    
    def __str__(self):
        return self.name


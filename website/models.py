from django.db import models
from ckeditor.fields import RichTextField
from django.utils.text import slugify
#from sorl.thumbnail import ImageField
# Create your models here.

Rating_Choices = (
    # (1, 'Poor'),
    # (2, 'Average'),
    # (3, 'Good'),
    # (4, 'Very Good'),
    # (5, 'Excellent')
    (1, '1'),
    (2, '2'),
    (3, '3'),
    (4, '4'),
    (5, '5')
)


class ImageHome(models.Model):
    caption = models.CharField(max_length=255)
    rating = models.IntegerField(choices=Rating_Choices, default=1)
    imagehome = models.ImageField(
        null=True, blank=True, upload_to='imagehome/')

    class Meta:
        verbose_name_plural = 'Imágenes de Inicio'

    def __str__(self):
        return self.caption


class Category(models.Model):
    title = models.CharField(max_length=255)
    description = RichTextField(blank=True, null=True)
    HeaderImage = models.ImageField(
        null=True, blank=True, upload_to='category/')
    slug = models.SlugField(null=True, blank=True)

    class Meta:
        verbose_name_plural = 'Categorías'

    def __str__(self):
        return self.title

# Al Guardar, crear el URL basado en el titulo
    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Category, self).save(*args, **kwargs)


class Object(models.Model):
    Name = models.CharField(max_length=255)
    category = models.ForeignKey(Category, default=1, on_delete=models.CASCADE)
    description = RichTextField(blank=True, null=True)
    details = RichTextField(blank=True, null=True)
    image1 = models.ImageField(null=True, blank=True)
    image2 = models.ImageField(null=True, blank=True)
    image3 = models.ImageField(null=True, blank=True)
    image4 = models.ImageField(null=True, blank=True)
    image5 = models.ImageField(null=True, blank=True)

    class Meta:
        verbose_name_plural = 'Objetos'

    def __str__(self):
        return self.Name + '-' + str(self.category)

# TRIPS


class Trip(models.Model):
    name = models.CharField(max_length=255)
    description = RichTextField(blank=True, null=True)
    # Fecha y hora
    date_trip = models.DateField(null=True, blank=True)
#    image = ImageField(upload_to='trips/', null=True, blank=True)
    image = models.ImageField(null=True, blank=True, upload_to='trips/')

    class Meta:
        verbose_name_plural = 'Trips'

    def __str__(self):
        return self.name

# EQUIPMENT


class Equipment(models.Model):
    name = models.CharField(max_length=255)
    description = RichTextField(blank=True, null=True)
    image = models.ImageField(null=True, blank=True, upload_to='equipment/')

    class Meta:
        verbose_name_plural = 'Equipos'

    def __str__(self):
        return self.name

# PUBLISHED IMAGES


class Published(models.Model):
    name = models.CharField(max_length=255, verbose_name='Publicación')
    description = RichTextField(blank=True, null=True)
    link = models.CharField(max_length=255, blank=True, null=True)
    image = models.ImageField(null=True, blank=True, upload_to='published/')
 
    class Meta:
        verbose_name_plural = 'Publicaciones'

    def __str__(self):
        return self.name


class Links(models.Model):
    name = models.CharField(max_length=255)
    link = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        verbose_name_plural = 'Links'

    def __str__(self):
        return self.name

from django.db import models


class Genre(models.Model):
    """
    Modelo que representa un genero literario
    """
    name = models.CharField(max_length=200,help_text="INgrese el nombre del genero")

    def __str__(self):
        """cadena que representa una instancia del modelo
        """
        return self.name

from django.urls import reverse 

class Book(models.Model):

    title = models.CharField(max_length=200)
    author = models.ForeignKey('Author',on_delete=models.SET_NULL,null=True)
        # ForeignKey, ya que un libro tiene un solo autor, pero el mismo autor puede haber escrito muchos libros.
    # 'Author' es un string, en vez de un objeto, porque la clase Author aún no ha sido declarada.
    summary = models.TextField(max_length=1000,help_text="Ingrese una brve description del libro")
    isbn = models.CharField('ISBN',max_length=13,help_text='13 Caracteres <a href="https://www.isbn-international.org/content/what-isbn">ISBN number</a>')

    genre = models.ManyToManyField(Genre,help_text="Seleccione un genero para este libro")
    # ManyToManyField, porque un género puede contener muchos libros y un libro puede cubrir varios géneros.
    # La clase Genre ya ha sido definida, entonces podemos especificar el objeto arriba.
    
    def display_genre(self):
        """
        CReate a string for the Genre. this is required to display genere in admin
        """
        return ', '.join([genre.name for genre in self.genre.all()[:3] ])
    display_genre.short_description = 'Genre'
    def __str__(self):
        """
        Representacion del objeto book
        """
        return self.title
    
    def get_absolute_url(self):
        """
        Devuelve el URL a una instancia particular de Book
        """
        return reverse("book-detail", args=[str(self.id)])
    
import uuid # Requerida para las instancias de libros únicos


class BookInstance(models.Model):
    """
    Modelo que representa una copia específica de un libro (i.e. que puede ser prestado por la biblioteca).
    """
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, help_text="ID único para este libro particular en toda la biblioteca")
    book = models.ForeignKey('Book', on_delete=models.SET_NULL, null=True) 
    imprint = models.CharField(max_length=200)
    due_back = models.DateField(null=True, blank=True)

    LOAN_STATUS = (
        ('m', 'Maintenance'),
        ('o', 'On loan'),
        ('a', 'Available'),
        ('r', 'Reserved'),
    )

    status = models.CharField(max_length=1, choices=LOAN_STATUS, blank=True, default='m', help_text='Disponibilidad del libro')

    class Meta:
        ordering = ["due_back"]
        

    def __str__(self):
        """
        String para representar el Objeto del Modelo
        """
        return '%s (%s)' % (self.id,self.book.title)
class Author (models.Model):

    first_name= models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    date_of_birth = models.DateField(null=True,blank=True)
    date_of_death= models.DateField('Died',null=True,blank=True)
    

    def get_absolute_url(self): return reverse('author-detail',args=[str(self.id)])

    def __str__(self):
        return '%s, %s' % (self.last_name,self.first_name)


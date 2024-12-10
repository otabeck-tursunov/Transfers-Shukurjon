from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models


class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        abstract = True


class Country(BaseModel):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Categories'


class Club(BaseModel):
    name = models.CharField(max_length=255)
    logo = models.ImageField(upload_to='clubs/')
    president = models.CharField(max_length=255, blank=True, null=True)
    coach = models.CharField(max_length=255, blank=True, null=True)
    found_date = models.DateField(blank=True, null=True)
    max_import = models.FloatField(blank=True, null=True)
    max_export = models.FloatField(blank=True, null=True)

    country = models.ForeignKey(Country, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Player(BaseModel):
    name = models.CharField(max_length=255)
    age = models.PositiveSmallIntegerField()
    price = models.FloatField(blank=True, null=True, validators=[MinValueValidator(0)])
    position = models.CharField(max_length=255, blank=True, null=True)
    number = models.PositiveSmallIntegerField(blank=True, null=True)

    club = models.ForeignKey(Club, on_delete=models.CASCADE)
    country = models.ForeignKey(Country, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Season(BaseModel):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Transfer(BaseModel):
    player = models.ForeignKey(Player, on_delete=models.CASCADE)
    old_club = models.ForeignKey(Club, on_delete=models.CASCADE, related_name='old_club')
    new_club = models.ForeignKey(Club, on_delete=models.CASCADE, related_name='new_club')
    price = models.FloatField(blank=True, null=True, validators=[MinValueValidator(0)])
    tft_price = models.FloatField(blank=True, null=True, validators=[MinValueValidator(0)])
    season = models.ForeignKey(Season, on_delete=models.CASCADE)
    date = models.DateField()

    def __str__(self):
        return f'{self.player} {self.season}'

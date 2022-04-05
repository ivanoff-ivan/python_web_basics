from django.core.validators import MinLengthValidator, MinValueValidator
from django.db import models

from my_music.main_app.validators import validate_input


class Profile(models.Model):
    USERNAME_MIN_LENGTH = 2
    USERNAME_MAX_LENGTH = 15

    AGE_MIN_VALUE = 0

    username = models.CharField(
        max_length=USERNAME_MAX_LENGTH,
        validators=(
            MinLengthValidator(USERNAME_MIN_LENGTH),
            validate_input,
        ),
    )

    email = models.EmailField()

    age = models.IntegerField(
        null=True,
        blank=True,
        validators=(
            MinValueValidator(AGE_MIN_VALUE),
        ),

    )


class Album(models.Model):
    ALBUM_NAME_MAX_LENGTH = 30
    ARTIST_MAX_LENGTH = 30
    GENRE_MAX_LENGTH = 30

    POP_MUSIC = 'Pop Music'
    JAZZ_MUSIC = 'Jazz Music'
    RNB_MUSIC = 'R&B Music'
    ROCK_MUSIC = 'Rock Music'
    COUNTRY_MUSIC = 'Country Music'
    DANCE_MUSIC = 'Dance Music'
    HIP_HOP_MUSIC = 'Hip Hop Music'
    OTHER = 'Other'

    PRICE_MIN_VALUE = 0.0

    album_name = models.CharField(
        max_length=ALBUM_NAME_MAX_LENGTH,
        unique=True,
    )

    artist = models.CharField(
        max_length=ARTIST_MAX_LENGTH,
    )

    genre = models.CharField(
        max_length=GENRE_MAX_LENGTH,
        choices=(
            (POP_MUSIC, 'Pop Music'),
            (JAZZ_MUSIC, 'Jazz Music'),
            (RNB_MUSIC, 'R&B Music'),
            (ROCK_MUSIC, 'Rock Music'),
            (COUNTRY_MUSIC, 'Country Music'),
            (DANCE_MUSIC, 'Dance Music'),
            (HIP_HOP_MUSIC, 'Hip Hop Music'),
            (OTHER, 'Other'),
        ),
    )

    description = models.TextField(
        null=True,
        blank=True,
    )

    image_url = models.URLField()

    price = models.FloatField(
        validators=(
            MinValueValidator(PRICE_MIN_VALUE),
        )
    )

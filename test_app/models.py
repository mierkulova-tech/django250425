from django.db import models


class Book(models.Model):
    title = models.CharField(max_length=120)  # VARCHAR
    description = models.TextField()
    author = models.CharField(max_length=100)
    published_date = models.DateField()
    pages = models.PositiveSmallIntegerField(default=0)

    def __str__(self):
        return f"Book '{self.title}'  -- Author '{self.author}'"

    class Meta:
        db_table = "books"  # Название таблицы
        ordering = ["published_date",]  # Порядок сортировки при запросе данных из базы (по умолчанию сортировка по ID)
        verbose_name = "Book"  # изменение отображения названия модели в ед. числе для админ панели
        verbose_name_plural = "Books"  # изменение отображения названия модели во множественном числе для админ панели

        get_latest_by = "published_date"  # Определяет то, как будет отдаваться последний объект в базе. По умолчанию отдаётся последний по ID

        default_related_name = "books"  #  Помогает поставить related_name по умолчанию для всех связанных объектов (ForeignKey, OneToOneField, ManyToManyField)
        # unique_together = ["title", "published_date"]  # Помогает создавать ПАРЫ уникальности по двум и более колонкам

        indexes = [
            models.Index(
                fields=["title", "published_date"],
                name="idx_book_title_pub_date"
            )
        ]

        constraints = [
            models.UniqueConstraint(
                fields=["title", "published_date"],
                name="unq_title_pub_date"
            ),

            models.CheckConstraint(
                check=models.Q(pages__gte=0),
                name="book_pages_constraint"
            )
        ]



class Post(models.Model):
    title = models.CharField(max_length=120)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    image_url = models.URLField(max_length=250, null=True, blank=True)

    def __str__(self):
        return self.title

    class Meta:
        db_table = "posts"  # Название таблицы

class UserProfile(models.Model):
    nickname = models.CharField(max_length=70, unique=True)
    bio = models.TextField(null=True, blank=True)
    website = models.URLField(max_length=250, blank=True, null=True)
    age = models.PositiveSmallIntegerField()
    followers_count = models.PositiveBigIntegerField()
    posts_count = models.PositiveIntegerField()
    comments_count = models.PositiveIntegerField()
    engagement_rate = models.FloatField()

    def __str__(self):
        return self.nickname

    class Meta:
        db_table = "user_profile"  # Название таблицы

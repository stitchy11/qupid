from django.db import models

from django.urls import reverse

class Character(models.Model):
    DEGREE = (
        (5, '아주 많음'),
        (4, '많음'),
        (3, '보통'),
        (2, '적음'),
        (1, '아주 적음')
    )

    char_active = models.PositiveSmallIntegerField(verbose_name='활발함', choices=DEGREE)
    char_hair = models.PositiveSmallIntegerField(verbose_name='털날림', choices=DEGREE)
    char_barking = models.PositiveSmallIntegerField(verbose_name='짖음', choices=DEGREE)
    char_social = models.PositiveSmallIntegerField(verbose_name='사교성', choices=DEGREE)
    char_indep = models.PositiveSmallIntegerField(verbose_name='독립성', choices=DEGREE)
    char_lovely = models.PositiveSmallIntegerField(verbose_name='애교', choices=DEGREE)

    def __str__(self):
        return "활발({}),털날림({}),짖음({}),사교성({}),독립성({}),애교({})".format(*list(self.__dict__.values())[2:])


class Profile(models.Model):
    GENDERS = (
        ('F', '여자'),
        ('M', '남자'),
    )
    NEUTERED = (
        ('O', 'O'),
        ('X', 'X'),
    )

    character = models.ForeignKey(Character, on_delete=models.PROTECT)
    name = models.CharField(verbose_name='이름',max_length=200, db_index=True)
    gender = models.CharField(verbose_name='성별', max_length=20, choices=GENDERS)
    age = models.PositiveSmallIntegerField(verbose_name='나이', null=True)
    neutered = models.CharField(verbose_name='중성화여부', max_length=20, choices=NEUTERED)
    a_number = models.CharField(verbose_name='공고번호',max_length=20)
    shelter = models.CharField(verbose_name='유기견 보호소', max_length=200)
    # 이거 이렇게 해도 되는건지

    slug = models.SlugField(max_length=200, db_index=True, unique=True,allow_unicode=True)
    image = models.ImageField(upload_to='profiles/%Y/%m/%d', blank=True)

    available_adopt = models.BooleanField('입양 가능 여부', default=True)

    created = models.DateTimeField(auto_now_add=True)  # settings.USE_TZ = False
    updated = models.DateTimeField(auto_now=True)  # settings.USE_TZ = False


    class Meta:
        ordering = ['-created']
        index_together = [['id', 'slug']]

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('profiles:all_profiles', args=[self.id, self.slug])


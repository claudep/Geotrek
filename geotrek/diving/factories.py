import factory

from django.contrib.contenttypes.models import ContentType

from geotrek.authent.factories import StructureRelatedDefaultFactory
from geotrek.common.utils.testdata import get_dummy_uploaded_image

from . import models

from mapentity.factories import UserFactory

from django.contrib.auth.models import Permission


class PracticeFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = models.Practice

    name = "Practice"
    pictogram = get_dummy_uploaded_image()


class LevelFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = models.Level

    name = "Level"
    description = "<p>Description</p>"
    pictogram = get_dummy_uploaded_image('level.png')


class DiveWithLevelsFactory(StructureRelatedDefaultFactory):
    class Meta:
        model = models.Dive

    name = "Dive"
    practice = factory.SubFactory(PracticeFactory)
    geom = 'POINT(0 0)'
    published = True

    @factory.post_generation
    def levels(obj, create, extracted=None, **kwargs):
        if create:
            obj.levels.add(LevelFactory.create().pk)


class DiveFactory(StructureRelatedDefaultFactory):
    class Meta:
        model = models.Dive

    name = "Dive"
    practice = factory.SubFactory(PracticeFactory)
    geom = 'POINT(0 0)'
    published = True

    @factory.post_generation
    def sources(obj, create, extracted=None, **kwargs):
        if create:
            if extracted:
                for source in extracted:
                    obj.source.add(source)

    @factory.post_generation
    def portals(obj, create, extracted=None, **kwargs):
        if create:
            if extracted:
                for portal in extracted:
                    obj.portal.add(portal)


class DivingManagerFactory(UserFactory):
    is_staff = True

    @factory.post_generation
    def create_biodiv_manager(obj, create, extracted, **kwargs):
        content_type_dive = ContentType.objects.get_for_model(models.Dive)
        content_type_divelevel = ContentType.objects.get_for_model(models.Level)
        content_type_divedifficutly = ContentType.objects.get_for_model(models.Difficulty)
        for perm in Permission.objects.filter(content_type__in=[content_type_dive.pk, content_type_divelevel.pk,
                                                                content_type_divedifficutly.pk]):
            obj.user_permissions.add(perm)


class DifficultyFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = models.Difficulty

    name = "Difficulty"
    pictogram = get_dummy_uploaded_image('difficulty.png')

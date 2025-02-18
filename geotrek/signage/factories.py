import factory

from geotrek.common.utils.testdata import get_dummy_uploaded_image
from geotrek.core.factories import PointTopologyFactory
from geotrek.infrastructure.factories import InfrastructureConditionFactory

from . import models


class SignageTypeFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = models.SignageType

    label = "Signage type"
    pictogram = get_dummy_uploaded_image('signage_type.png')


class SignageTypeNoPictogramFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = models.SignageType

    label = "Signage type"


class BladeTypeFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = models.BladeType

    label = "Blade type"


class BladeColorFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = models.Color

    label = "Blade color"


class BladeDirectionFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = models.Direction

    label = "Blade direction"


class SealingFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = models.Sealing

    label = "Sealing"


class SignageFactory(PointTopologyFactory):
    class Meta:
        model = models.Signage

    name = "Signage"
    type = factory.SubFactory(SignageTypeFactory)
    condition = factory.SubFactory(InfrastructureConditionFactory)
    sealing = factory.SubFactory(SealingFactory)
    printed_elevation = 4807
    published = True


class SignageNoPictogramFactory(SignageFactory):
    class Meta:
        model = models.Signage

    type = factory.SubFactory(SignageTypeNoPictogramFactory)


class BladeFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = models.Blade

    number = 1
    type = factory.SubFactory(BladeTypeFactory)
    condition = factory.SubFactory(InfrastructureConditionFactory)
    direction = factory.SubFactory(BladeDirectionFactory)
    color = factory.SubFactory(BladeColorFactory)
    topology = factory.SubFactory(PointTopologyFactory)
    signage = factory.SubFactory(SignageFactory)

    @factory.post_generation
    def lines(obj, create, extracted=None, **kwargs):
        if create:
            LineFactory.create(blade=obj)


class LineFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = models.Line

    number = "1"
    text = "Text"
    distance = 42.5
    pictogram_name = "Pictogram name"
    time = "0:42:30"
    blade = factory.SubFactory(BladeFactory)

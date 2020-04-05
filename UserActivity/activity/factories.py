import factory
from . import models

factory.Faker._DEFAULT_LOCALE = 'en_US'

class UserFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = models.User

    ok = factory.Faker('ok')


class MemberFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = models.Member

    user = factory.Iterator(models.User.objects.all())
    id = factory.Faker('id')
    real_name = factory.Faker('real_name')
    tz = factory.Faker('tz')


class ActivityPeriodFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = models.ActivityPeriod

    member = factory.Iterator(models.Member.objects.all())
    start_time = factory.Faker('start_time')
    end_time = factory.Faker('end_time')

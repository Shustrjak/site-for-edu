import graphene
from graphene_django.types import DjangoObjectType
from graphene_django.filter import DjangoFilterConnectionField

from .models import Teacher, Course


class TeacherType(DjangoObjectType):

    class Meta:
        model = Teacher


class TeacherFilteredType(DjangoObjectType):

    class Meta:
        model = Teacher
        filter_fields = {
            'name': ['exact', 'icontains', 'istartswith'],
        }
        interfaces = (graphene.relay.Node, )


class CourseType(DjangoObjectType):

    class Meta:
        model = Course


class CourseMutation(graphene.Mutation):

    class Arguments:
        course_id = graphene.Int(required=True)
        new_name = graphene.String(required=True)

    result = graphene.Boolean()
    teacher = graphene.Field(TeacherType)

    def mutate(self, info, school_id, new_name):
        return {
            'result': True,
            'teacher': Teacher.objects.first()
        }


class Mutation:
    change_school_name = CourseMutation.Field()


class Query:
    all_teachers = graphene.List(TeacherType, limit=graphene.Int())
    filtered_teachers = DjangoFilterConnectionField(TeacherFilteredType)
    retrieve_teacher = graphene.Field(TeacherType, id=graphene.Int())

    def resolve_all_teachers(self, *args, **kwargs):
        if 'limit' in kwargs:
            return Teacher.objects.all()[:kwargs['limit']]
        return Teacher.objects.all()

    def resolve_retrieve_teacher(self, info, **kwargs):
        if 'id' in kwargs:
            return Teacher.objects.get(id=kwargs['id'])

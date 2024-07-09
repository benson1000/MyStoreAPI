from rest_framework import serializers
from .models import Product
from core.models import Company
from core.serializers import CompanySerializer


class CompanyRelatedField(serializers.RelatedField):

    def to_representation(self, value):
        serializer = CompanySerializer(value)
        return serializer.data

    def to_internal_value(self, data):
        return self.queryset.get(pk=data)


class ProductSerializer(serializers.ModelSerializer):
    company = CompanyRelatedField(many=False, queryset=Company.objects.all())

    class Meta:
        model = Product
        fields = ('id', 'name', 'description', 'price', 'image', 'company')
        extra_kwargs = {
            'company': {
               'required': True
            }
        }

from rest_framework import serializers
from .models import Company
from review.models import Review, CompanyEmploymentAuth
from users.models import EmploymentAuth
from users.serializers import EmploymentAuthSerializer
from django.db.models import Avg, Count

class CompanySerializer(serializers.ModelSerializer):
    ratings = serializers.SerializerMethodField()
    supported_employment_auths = serializers.SerializerMethodField()
    review_id = serializers.SerializerMethodField()
    review_count = serializers.SerializerMethodField()

    def get_review_count(self, obj):
        return Review.objects.filter(is_published=True, company__pk=obj.pk).count()

    def get_review_id(self, obj):
        if Review.objects.filter(user=self.context.get('user'), company__pk=obj.pk).count() == 0:
            return None
        return Review.objects.filter(user=self.context.get('user'), company__pk=obj.pk)[0].pk   

    def get_ratings(self, obj):
        ratings = []
        for i in range(1,6):
            rating = {}
            rating['id'] = i
            rating['count'] = Review.objects.filter(company=obj, overall_company_experience=i).aggregate(Count('overall_company_experience'))['overall_company_experience__count']
            ratings.append(rating)
        return ratings

    def get_supported_employment_auths(self, obj):
        auths = []
        for auth in EmploymentAuth.objects.all():
            a_ser = EmploymentAuthSerializer(instance=auth, many=False).data
            emp_auths = CompanyEmploymentAuth.objects.filter(review__company=obj, employment_auth=auth)
            a_ser['yes'] = emp_auths.filter(value=True).aggregate(Count('value'))['value__count']
            a_ser['no'] = emp_auths.filter(value=False).aggregate(Count('value'))['value__count']
            auths.append(a_ser)
        return auths    

    def create(self, validated_data):
        return Company.objects.create(**validated_data)
    class Meta:
        model = Company
        fields = ('__all__')
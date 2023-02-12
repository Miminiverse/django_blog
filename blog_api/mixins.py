

from rest_framework import serializers

class UserQuerySetMixin():
    user_fields = 'author'
    def get_queryset(self, *args, **kwargs):
        lookup_data = {}
        lookup_data[self.user_fields] = self.request.user
        qs = super().get_queryset(*args, **kwargs)
        return qs.filter(**lookup_data)
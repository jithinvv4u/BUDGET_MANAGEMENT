from utilities.functions import decode, encode
from rest_framework import serializers

class IdencodeField(serializers.CharField):

    serializer = None
    related_model = None

    def __init__(self, serializer=None, related_model=None, *args, **kwargs):
        self.serializers = serializer
        self.related_model = related_model
        super(IdencodeField, self).__init__(*args, **kwargs)

    def to_representation(self, value):
        if not value:
            return None
        if self.serializer:
            return self.serializer(value).data
        if isinstance(value, int):
            return encode(value)
        try:
            return encode(value.id)
        except:
            return None

    def to_internal_value(self, value):
        if self.related_model and isinstance(value, self.related_model):
            return value
        try:
            value = decode(value) or int(value)
        except:
            raise serializers.ValidationError('invalid id/pk format')
        related_model = self.related_model
        if not related_model:
            return value
        try:
            return related_model.objects.get(id=value)
        except:
            raise serializers.ValidationError(
                'invalid pk , object does not exist')


class ManyToManyIdencodeField(serializers.CharField):
    """Encoded id field."""

    serializer = None
    related_model = None

    def __init__(self, serializer=None, related_model=None, *args, **kwargs):
        """Initializing field object."""
        self.serializer = serializer
        self.related_model = related_model
        super(ManyToManyIdencodeField, self).__init__(*args, **kwargs)

    def to_representation(self, value):
        """
        Override the returning method.

        This function will check if the serializer is supplied
        in case of foreign key field. In case of foreign key, the
        value will be and object. If it is  normal id then it is
        going to be type int.
        """
        if not value:
            return []
        if self.serializer:
            data = []
            for pk in value.all():
                data.append(self.serializer(pk).data)
            return data
        data = []
        for item in value.all():
            if isinstance(item, int):
                data.append(encode(item))
            try:
                data.append(encode(item.id))
            except:
                return []
        return data

    def to_internal_value(self, value):
        """To convert value for saving."""
        data = []
        if value is None:
            values = []
        elif type(value) == str:
            values = [i.strip() for i in value.split(',')]
        elif type(value) == list:
            values = value
        else:
            raise serializers.ValidationError("Should be list of IDs")
        for pk in values:
            try:
                data.append(int(pk))
            except:
                data.append(decode(pk))
        related_model = self.related_model
        if not related_model:
            try:
                related_model = self.parent.Meta.model._meta.get_field(
                    self.source).related_model
            except:
                raise serializers.ValidationError(
                    f"Model '{self.parent.Meta.model.__name__}' "
                    f"has no foreign key relation with key '{self.source}'. "
                    f"'related_model' is required."
                )
        try:
            return related_model.objects.filter(id__in=data)
        except:
            raise serializers.ValidationError(
                'Invalid pk - object does not exist.')


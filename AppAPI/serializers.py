from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
from rest_framework import serializers, validators


class Signup_userSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ('Image', 'Fullname', 'EmailAddress', 'Phonenumber', 'password', 
                  'Address', 'Landmark', 'Label', 'Role', 'Identity', 'ID_Image', 'Document')

        extra_fields = {
            "password": {'write_only': True},
            "email": {
                'required': True,
                'allow_blank': False,
                'validators': [
                    validators.UniqueValidator(
                        get_user_model().objects.all(), "A user with that Email exists"
                    )
                ]
            }
        }
    
    def create(self, validated_data):
        image = validated_data.get('Image')
        fullname = validated_data.get('Fullname')
        email = validated_data.get('EmailAddress')
        phonenumber = validated_data.get('Phonenumber')
        password = validated_data.get('password')
        address = validated_data.get('Address')
        landmark = validated_data.get('Landmark')
        label = validated_data.get('Label')
        role = validated_data.get('Role')
        identity = validated_data.get('Imdentity')
        id_image = validated_data.get('ID_Image')
        document = validated_data.get('Document')

        user = get_user_model().objects.create(
            Image = image,
            Fullname = fullname,
            EmailAddress = email,
            Phonenumber = phonenumber,
            username = email,
            password = password,
            Address = address,
            Landmark = landmark,
            Label = label,
            Role = role,
            Identity = identity,
            ID_Image = id_image,
            Document = document

        )
        user.set_password(password)
        user.save()
        return user

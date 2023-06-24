# project/app/models/tortoise.py


from dataclasses import field
from tortoise import fields, models
from tortoise.contrib.pydantic import pydantic_model_creator  # new


class UserLicence(models.Model):
    licence_key = fields.UUIDField(auto_now_add=True,pk=True)
    #user_id = fields.ForeignKeyField('models.Users', related_name='licences')
    user_id = fields.IntField()
    created_at = fields.DatetimeField(auto_now_add=True)

    def __str__(self):
        return str(self.licence_key)


class Users(models.Model):
    user_id = fields.IntField(pk=True)
    user_email = fields.CharField(max_length=255, unique=True)
    user_password = fields.CharField(max_length=255)
    user_name = fields.TextField()
    user_pronoun = fields.TextField()


LicenceSchema = pydantic_model_creator(UserLicence)  # new
UserSchema = pydantic_model_creator(Users)

from ma import ma
from models.user import UserModel


class UserSchema(ma.ModelSchema):
    class Meta:
        model = UserModel
        load_only = ("password",)   #only for loading, not return the password to user inquire
        dump_only = ("id",)


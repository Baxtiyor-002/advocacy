from rest_framework.exceptions import AuthenticationFailed
from .. import serializer
from google.auth2 import id_token
from google.auth.transport import requests
from oauth import AuthUser


def check_google_auth(google_user: serializer.GoogleAuth):
    try:
        id_token.verify_oauth2_token(google_user['token'], requests.Request())
    except ValueError:
        raise AuthenticationFailed(code=403, detail='Bad token Google')

    user, _ = AuthUser.objects.get_or_create(email=google_user['email'])
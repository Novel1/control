# from datetime import datetime
#
# import jwt
# from app.user import schemas
#
#
# class TokenService:
#     def create_token(self, data: schemas.TokenData, expires_delta):
#         payload = {
#             'sub': str(data.sub),
#             'exp': datetime.utcnow() + expires_delta,
#         }
#
#
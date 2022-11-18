from rest_framework import serializers
from dj_rest_auth.registration.serializers import RegisterSerializer
from articles.serializers import ReviewSerializer
from movies.serializers import ScoreSerializer, MovieListSerializer
from .models import User

class CustomUserSerializer(RegisterSerializer):
    # 기본 설정 필드: username, password, email
    # 추가 설정 필드: profile_image

    # profile_image = serializers.ImageField(use_url=True)
    nickname = serializers.CharField(max_length=30)

    def get_cleaned_data(self):
        data = super().get_cleaned_data()
        data['nickname'] = self.validated_data.get('nickname', '')

        return data

# class UserSerializer(serializers.ModelSerializer):

#     class Meta:
#         model = User
#         fields =('username','nickname','last_name','first_name')


# class OtherUserSerializer(serializers.ModelSerializer):

#     class Meta:
#         model = User
#         fields = ('username','nickname',)

# class FollowingSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = 


class MyArticleSerializer(serializers.ModelSerializer):
    user_reviews = ReviewSerializer(many=True, read_only=True)
    #무비정보도 있어야함
    # user_movies 
    class Meta:
        model = User
        fields = ('username','nickname','last_name','first_name','user_reviews')
#나 말고 다른사용자가 
class OtherArticleSerializer(serializers.ModelSerializer):
    user_reviews = ReviewSerializer(many=True, read_only=True)

    class Meta:
        model = User
        fields = ('username','nickname','user_reviews')


# class UserGenreScoreSerializer(serializers.ModelSerializer):
#     user_genre = ScoreSerializer(many=True, read_only=True)
    
#     class Meta:
#         model = User
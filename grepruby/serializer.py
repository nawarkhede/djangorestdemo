from rest_framework import serializers

from .models import Article, Tag


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = "__all__"

    def create(self, validated_data):
        article = validated_data.pop("article")
        tag = Tag.objects.get_or_create(**validated_data)[0]
        tag.article = article
        tag.save(update_fields=["article"])
        return tag


class ArticleSerializer(serializers.ModelSerializer):
    tags = TagSerializer(many=True)

    class Meta:
        model = Article
        fields = (
            "id",
            "created_on",
            "title",
            "description",
            "publish_date",
            "author_name",
            "tags",
        )

    def create(self, validated_data):
        tag_validated_data = validated_data.pop("tags")
        article = Article.objects.create(**validated_data)
        tag_serializer = self.fields["tags"]
        for each in tag_validated_data:
            each["article"] = article
        tags = tag_serializer.create(tag_validated_data)
        return article

    def update(self, instance, validated_data):
        tag_validated_data = validated_data.pop("tags")
        for each in validated_data:
            setattr(instance, each, validated_data[each])
        instance.save()
        tag_serializer = self.fields["tags"]
        for each in tag_validated_data:
            each["article"] = instance
        for t in instance.tags.all():
            instance.tags.remove(t)
        instance.save()
        tags = tag_serializer.create(tag_validated_data)
        return instance

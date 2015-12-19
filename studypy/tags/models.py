from django.db import models


class Tag(models.Model):
    name = models.CharField('name', max_length=50, unique=True)

    def __str__(self):
        return self.name

    @property
    def number_of_resources(self):
        return self.resources.all().count()

    @classmethod
    def number_of_tags(cls):
        return cls.objects.count()

    @staticmethod
    def get_tags_grid(tags, tags_per_row):
        grid = []
        for i in range(0, len(tags) - 1, tags_per_row):
            grid.append(tags[i:i+tags_per_row])
        return grid

    @classmethod
    def get_tags_sorted_by_number_of_resources(cls):
        return sorted(cls.objects.all(),
                      key=lambda tag: tag.number_of_resources, reverse=True)
import csv
import os

from django.conf import settings
from django.core.management.base import BaseCommand
from django.shortcuts import get_object_or_404
from reviews.models import Category, Comment, Genre, Review, Title
from users.models import User


class Command(BaseCommand):
    help = 'Load yamdb data from .csv files'

    def load_raw(self, file_name, obj):
        self.stdout.write(f'    Loading {file_name}...', ending='')
        obj.objects.all().delete()
        with open(file_name) as f:
            lines = list(csv.reader(f, delimiter=','))
            fields = lines[0]
            for line in lines[1:]:
                values = line
                kwargs = dict(zip(fields, values))
                if 'category' in kwargs.keys():
                    kwargs['category'] = get_object_or_404(
                        Category,
                        id=kwargs['category']
                    )
                if 'author' in kwargs.keys():
                    kwargs['author'] = get_object_or_404(
                        User,
                        id=kwargs['author']
                    )
                obj.objects.get_or_create(**kwargs)
        self.stdout.write('Done')

    def load_genre_title(self, file_name):
        self.stdout.write(f'   Loading {file_name}...', ending='')
        with open(file_name) as f:
            lines = list(csv.reader(f, delimiter=','))
            fields = lines[0]
            for line in lines[1:]:
                values = line
                kwargs = dict(zip(fields, values))
                title = get_object_or_404(Title, id=kwargs['title_id'])
                genre = get_object_or_404(Genre, id=kwargs['genre_id'])
                title.genre.add(genre)
                title.save()
        self.stdout.write('Done')

    def handle(self, *args, **kwargs):

        full_path_loc = ''
        data_loc = 'data'
        for dir in settings.STATICFILES_DIRS:
            if os.path.isdir(dir + data_loc):
                full_path_loc = dir + data_loc
                break
        if full_path_loc == '':
            self.stdout.write(
                f'Directory \'{data_loc}\' with .csv files not found.'
            )
            return

        self.stdout.write(f'Loading .csv files from {full_path_loc}...')

        self.load_raw(full_path_loc + '/category.csv', Category)
        self.load_raw(full_path_loc + '/genre.csv', Genre)
        self.load_raw(full_path_loc + '/users.csv', User)
        self.load_raw(full_path_loc + '/titles.csv', Title)
        self.load_raw(full_path_loc + '/review.csv', Review)
        self.load_raw(full_path_loc + '/comments.csv', Comment)
        self.load_genre_title(full_path_loc + '/genre_title.csv')

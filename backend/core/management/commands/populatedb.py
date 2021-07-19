from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model
from blog.models import *


class Command(BaseCommand):
	def add_arguments(self, parser):
		parser.add_argument(
			"--target",
			nargs="?",
			dest="target",
		)

	@staticmethod
	def boolean_input(question, default=None):
		result = input("%s " % question)
		if not result and default is not None:
			return default
		while len(result) < 1 or result[0].lower() not in "yn":
			result = input("yかnで入力して下さい")
		return result[0].lower() == "y"

	def handle(self, *args, **options):
		alert_message = "これを実行するとデータベース内のデータが削除されます。宜しいですか？ (y/n)"
		if self.boolean_input(alert_message):
			target = str(options['target'])
			if target == 'all':
				self.reset_users()
				self.reset_posts()
			elif target == 'users':
				self.reset_users()
			elif target == 'posts':
				self.reset_posts()
			else:
				print('対象を指定して下さい。')

	def reset_users(self):
		User = get_user_model()
		User.objects.all().delete()
		user = User.objects.create(
                email="papurica@gmail.com",
				username="papurica",
            )
		user.set_password("papurica")
		user.is_staff = True
		user.is_superuser = True
		user.save()

	def reset_posts(self):
		Post.objects.all().delete()
		Category.objects.all().delete()
		Tag.objects.all().delete()

		for category in [
			{"name": "筋トレ", "slug": "work_out"},
			{"name": "栄養", "slug": "nutrition"},
			{"name": "美容", "slug": "beauty"},
			{"name": "ファッション", "slug": "fashion"},
		]:
			Category.objects.create(
				name=category["name"],
				slug=category["slug"]
			)
		
		for tag in [
			{"name": "腕トレ", "slug": "arm_training"},
			{"name": "脚トレ", "slug": "leg_training"},
			{"name": "肩トレ", "slug": "shoulder_training"},
			{"name": "胸トレ", "slug": "chest_training"},
			{"name": "背中トレ", "slug": "back_training"},
			{"name": "炭水化物", "slug": "carbo"},
			{"name": "脂質", "slug": "fat"},
			{"name": "タンパク質", "slug": "protein"},
		]:
			Tag.objects.create(
				name=tag["name"],
				slug=tag["slug"]
			)

		for post in [
			{"category": Category.objects.get(slug="work_out"),
			"tags": Tag.objects.filter(slug__contains="training"),
			"title": "筋トレをするメリットとは？", 
			"description": "筋トレで得られる具体的な効果やメリット",
			"image": "https://source.unsplash.com/random",
			"image_text": "work_out",
			"is_published": True,
			"is_featured": True
			},
			{"category": Category.objects.get(slug="work_out"),
			"tags": Tag.objects.filter(slug__contains="training"),
			"title": "BIG3の効果は？", 
			"description": "BIG3をすることで得られる筋肉への影響",
			"image": "https://source.unsplash.com/random",
			"image_text": "work_out",
			"is_published": True,
			"is_featured": True
			},
			{"category": Category.objects.get(slug="nutrition"),
			"tags": Tag.objects.exclude(slug__contains="training"),
			"title": "筋肉がつきやすくなる食事週間とは？", 
			"description": "筋トレの効果を最大限に引き出す食事メニュー",
			"image": "https://source.unsplash.com/random",
			"image_text": "nutrition",
			"is_published": True,
			"is_featured": True
			},
			{"category": Category.objects.get(slug="nutrition"),
			"tags": Tag.objects.exclude(slug__contains="training"),
			"title": "筋トレをする人におすすめのサプリメント", 
			"description": "筋トレ効果を最大限に引き出すサプリメント",
			"image": "https://source.unsplash.com/random",
			"image_text": "nutrition",
			"is_published": True,
			"is_featured": True
			},
		]:
			Post.objects.create(
				category=post["category"],
				title=post["title"],
				description=post["description"],
				image=post["image"],
				image_text=post["image_text"],
				is_published=post["is_published"],
				is_featured=post["is_featured"]
			)
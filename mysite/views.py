from django.shortcuts import render
import pyrebase
from . import pyrebase_config
import locale
locale.setlocale(locale.LC_ALL, '')

def index(request):
    db = pyrebase.initialize_app(pyrebase_config.config).database()
    social_stats = db.child("social_stats").get().val()

    my_dict = {
        "num_twitter": locale.format("%d", int(social_stats["num_twitter"]), grouping=True),
        "num_instagram": locale.format("%d", int(social_stats["num_instagram"]), grouping=True),
        "num_facebook": locale.format("%d", int(social_stats["num_facebook"]), grouping=True),
        "num_youtube": locale.format("%d", int(social_stats["num_youtube"]), grouping=True),
        "num_discord": locale.format("%d", int(social_stats["num_discord"]), grouping=True),
        "num_mastodon": locale.format("%d", int(social_stats["num_mastodon"]), grouping=True),
        "num_soundcloud": locale.format("%d", int(social_stats["num_soundcloud"]), grouping=True),
        "num_gab": locale.format("%d", int(social_stats["num_gab"]), grouping=True)
    }

    return render(request, "mysite/index.html", context=my_dict)
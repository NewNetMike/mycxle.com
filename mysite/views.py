from django.shortcuts import render
import pyrebase
from . import pyrebase_config
import locale
locale.setlocale(locale.LC_ALL, '')
from pprint import pprint

def index(request):
    db = pyrebase.initialize_app(pyrebase_config.config).database()
    social_stats = db.child("social_stats").get().val()
    portfolio = db.child("portfolio").get().val()
    print(len(portfolio))
    grouped_portfolio = [[]]
    counter = 0
    for i in range(len(portfolio)):
        portfolio[i]["id"] = str(i)
        grouped_portfolio[counter].append(portfolio[i])
        if (i+1) % 3 == 0:
            grouped_portfolio.append([])
            counter += 1

    my_dict = {
        "num_twitter": locale.format("%d", int(social_stats["num_twitter"]), grouping=True),
        "num_instagram": locale.format("%d", int(social_stats["num_instagram"]), grouping=True),
        "num_facebook": locale.format("%d", int(social_stats["num_facebook"]), grouping=True),
        "num_youtube": locale.format("%d", int(social_stats["num_youtube"]), grouping=True),
        "num_discord": locale.format("%d", int(social_stats["num_discord"]), grouping=True),
        "num_mastodon": locale.format("%d", int(social_stats["num_mastodon"]), grouping=True),
        "num_soundcloud": locale.format("%d", int(social_stats["num_soundcloud"]), grouping=True),
        "num_gab": locale.format("%d", int(social_stats["num_gab"]), grouping=True),
        "portfolio_items": grouped_portfolio
    }

    return render(request, "mysite/index.html", context=my_dict)
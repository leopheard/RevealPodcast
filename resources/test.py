from resources.lib import thisiscriminal

def test_get_playable_podcast_returns_content():

    soup = thisiscriminal.get_soup("https://thisiscriminal.com/wp-json/criminal/v1/episodes?posts=1000&page=1")

    podcasts = thisiscriminal.get_playable_podcast(soup)

    assert type(podcasts) == list

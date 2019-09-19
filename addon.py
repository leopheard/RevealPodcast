from xbmcswift2 import Plugin, xbmcgui
from resources.lib import mainaddon

plugin = Plugin()

# base url for fetching podcasts 
URL1 = "http://feeds.revealradio.org/revealpodcast"
URL2 = "https://www.revealnews.org/feed/"

media:thumbnail
url

@plugin.route('/')
def main_menu():
    items = [
   {
            'label': plugin.get_string(30001), 
            'path': plugin.url_for('episodes1'),
            'thumbnail': "https://www.revealnews.org/wp-content/uploads/2017/11/reveal-square-logo-black-on-transparent-150x150.png"},
        {
            'label': plugin.get_string(30000), 
            'path': plugin.url_for('episodes'),
            'thumbnail': "https://www.revealnews.org/wp-content/uploads/2017/11/reveal-square-logo-black-on-transparent-150x150.png"},
   {
            'label': plugin.get_string(30002), 
            'path': plugin.url_for('episodes2'),
            'thumbnail': "https://www.revealnews.org/wp-content/uploads/2017/11/reveal-square-logo-black-on-transparent-150x150.png"},
    ]
    return items

@plugin.route('/episodes/')
def all_episodes():
    soup1 = mainaddon.get_soup1(URL1)
    playable_podcast = mainaddon.get_playable_podcast(soup1)
    items = mainaddon.compile_playable_podcast(playable_podcast)
    return items

@plugin.route('/episodes1/')
def all_episodes1():
    soup1 = mainaddon.get_soup1(URL1)
    playable_podcast1 = mainaddon.get_playable_podcast1(soup1)
    items = mainaddon.compile_playable_podcast1(playable_podcast1)
    return items

@plugin.route('/episodes2/')
def all_episodes2():
    soup2 = mainaddon.get_soup2(URL2)
    playable_podcast2 = mainaddon.get_playable_podcast2(soup2)
    items = mainaddon.compile_playable_podcast2(playable_podcast2)
    return items

if __name__ == '__main__':
    plugin.run()

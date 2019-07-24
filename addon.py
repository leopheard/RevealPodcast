from xbmcswift2 import Plugin, xbmcgui
from resources.lib import mainaddon

plugin = Plugin()

# base url for fetching podcasts 
URL = "http://feeds.revealradio.org/revealpodcast"

@plugin.route('/')
def main_menu():
    """
    main menu 
    """
    items = [
   {
            'label': plugin.get_string(30001), 
            'path': plugin.url_for('all_episodes1'),
            'thumbnail': "/home/osmc/.kodi/addons/plugin.audio.NPRpodcasts/resources/media/reveal300px.png"},
        {
            'label': plugin.get_string(30000), 
            'path': plugin.url_for('all_episodes'),
            'thumbnail': "/home/osmc/.kodi/addons/plugin.audio.NPRpodcasts/resources/media/reveal300px.png"},
    ]

    return items


@plugin.route('/all_episodes/')
def all_episodes():
    """
    contains playable podcasts listed as just-in
    """
    soup = mainaddon.get_soup(URL)
    
    playable_podcast = mainaddon.get_playable_podcast(soup)
    
    items = mainaddon.compile_playable_podcast(playable_podcast)

    return items


@plugin.route('/all_episodes1/')
def all_episodes1():
    """
    contains playable podcasts listed as just-in
    """
    soup = mainaddon.get_soup(URL)
    
    playable_podcast1 = mainaddon.get_playable_podcast1(soup)
    
    items = mainaddon.compile_playable_podcast1(playable_podcast1)

    return items


if __name__ == '__main__':
    plugin.run()

# coding=utf-8

"""
Module to display movie object, attributes and instances
main Python script to run
"""

import media
import fresh_tomatoes


# Movie Objects
I_am_legend = media.MovieTrailer(
    "I am legend",
    '''I_am_legend is a movie where a single man will
    smith finds solution to cure the zombies.''',
    "https://upload.wikimedia.org/wikipedia/en/d/df/I_am_legend_teaser.jpg",  # noqa
    "https://www.youtube.com/watch?v=ewpYq9rgg3w")

Winters_tale = media.MovieTrailer(
    "Winters tale",
    '''Polixenes, King of Bohemia, has been on a 
    nine-month visit to the court of his childhood 
    friend Leontes, King of Sicilia, and his wife,
    Queen Hermione. Groundlessly, Leontes becomes 
    convinced that his heavily pregnant wife has 
    been having an affair with Polixenes.''',
    "http://www.hans-zimmer.com/~hybrid/zimmer/WINTERSTALE.jpg",  # noqa
    "https://www.youtube.com/watch?v=DBSj1MKwx6A")

Alaipayuthae = media.MovieTrailer(
    "Alaipayuthae",
    '''Alaipayuthae is a dramatic and comedy movie 
    in which the romance and marriage life of two 
    peoples are show like a tale.''',
    "http://3.bp.blogspot.com/_WIFlbAzMDaQ/TJaDzGk-tLI/AAAAAAAAAyQ/u4T5NGVcrwg/w1200-h630-p-k-no-nu/Alaipayuthey_9.jpg",  # noqa
    "https://www.youtube.com/watch?v=BRFdGc3ku-k")

Men_in_black_3 = media.MovieTrailer(
    "Men in black 3",
    '''Men in black 3 is a action movie in which 
    ajent J and K has been protecting the Earth 
    from alien scum for many years. there arrived 
    a new animal called boris, they way they find 
    the animal is exciting.''',
    "https://www.dvdplanetstore.pk/wp-content/uploads/2014/08/Men-in-Black-3-2012dvdplanetstorepk.jpg",  # noqa
    "https://www.youtube.com/watch?v=aoyV49FfjOU")

Pele_Birth_of_legend = media.MovieTrailer(
    "Pele Birth of legend",
    '''Pele Birth of legend Under guidance from 
    manager Vicente Feola (Vincent D'Onofrio), young 
    Pelé (Kevin de Paula) utilizes his street soccer 
    skills to lead Brazil to the World Cup in 1958.''',
    "https://vidamine.com/media/com_hwdmediashare/files/22/34/9e/95a45631b7368aad585040ece859e65f.jpg",  # noqa
    "https://www.youtube.com/watch?v=pwBXs2B2ZbI")

King_arthur_legend_of_sword = media.MovieTrailer(
    "King arthur legend of sword",
    '''King arthur legend of sword After the murder 
    of his father, young Arthur's power-hungry uncle 
    Vortigern seizes control of the crown. When fate 
    leads him to pull the Excalibur sword from stone, 
    Arthur embraces his true destiny to become a 
    legendary fighter and leader.''',
    "https://cdn.flickeringmyth.com/wp-content/uploads/2017/04/king-arthur-charlie-hunnam-poster.jpg",  # noqa
    "https://www.youtube.com/watch?v=4luDtkC3Oy0")

# Creating list for movie objects
movies = [I_am_legend, Winters_tale, Alaipayuthae, Men_in_black_3, Pele_Birth_of_legend, King_arthur_legend_of_sword]  # noqa
fresh_tomatoes.open_movies_page(movies)

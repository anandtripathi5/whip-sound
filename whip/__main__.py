import itertools
import sys
import time
from random import randint
from threading import Thread

import click
import pkg_resources
from playsound import playsound


@click.command()
@click.argument('sound', required=False)
def main(sound):
    """Whip Application uses the numeric option for different whip sounds. Please pass the option from 1-5 \n
    whip          'play the default sound' \n
    whip 1        'play the 1st sound' \n
    whip random   'play random sound'
    """
    done = False
    if sound == 'random':
        sound = randint(1, 5)
    file = pkg_resources.resource_filename(__name__, f"static/{sound or 1}.mp3")
    play_thread = Thread(target=lambda: playsound(file))
    play_thread.start()
    for c in itertools.cycle(['|', '/', '-', '\\']):
        if done:
            break
        sys.stdout.write('\rPlaying ' + c)
        sys.stdout.flush()
        time.sleep(0.1)
        is_alive = play_thread.is_alive()
        if not is_alive:
            done = True
    sys.stdout.write('\rDone!')


if __name__ == '__main__':
    args = sys.argv
    if "--help" in args or len(args) == 1:
        print("Welcome to Whip Sound Application")
    main()

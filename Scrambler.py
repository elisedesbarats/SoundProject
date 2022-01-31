import pydub
import simpleaudio
import random
from pydub import AudioSegment


def cutMP3(songName, exportName, delay, length, fade_time):
    ## This one takes import and export filenames as an arguments
    ## as well as an onset delay in seconds
    ## the length of the cut clip you want in seconds
    ## and the fade in/fade out time (recommended is 2 seconds).

    # Example usage:
    # cutMP3('mysong.mp3', 'mysong_cut.mp3', 0, 60, 2)

    length = length * 1000
    fade_time = fade_time * 1000

    song = AudioSegment.from_mp3("%s" % songName)
    song = song[delay:delay + length]

    song = song.fade_out(fade_time)
    if delay != 0:
        song = song.fade_in(fade_time)

    exportPath = "%s" % exportName
    song.export(exportPath, format="mp3")


def scrambleMP3(songName, exportName, fragSize, crossfade_size, output_length, fade_time):
    ## This function makes a scrambled copy of a track.
    ## fragSize argument specifies the length of a fragment.
    ## reccomended fragSize is 0.5.
    ## crossfade_size is the length of the crossfade between fragments
    ## reccomended crossfade is 0.1 seconds.
    ## output_length is the desired length of the scrambled output in seconds.
    ## fade_time is same as in cutMP3(). Recommended is 2 seconds.

    # Example usage:
    # scrambleMP3('mysong.mp3', 'mysong_scrambled.mp3', 0.5, 0.1, 60, 2)

    fragSize = fragSize * 1000
    crossfade_size = crossfade_size * 1000
    output_length = output_length * 1000
    fade_time = fade_time * 1000

    song = AudioSegment.from_mp3("%s" % songName)

    clipList = list()
    fragNum = int(len(song) / fragSize)

    for i in range(fragNum):
        fraction = song[(i * fragSize):(i * fragSize + fragSize)]
        clipList.append(fraction)

    random.shuffle(clipList)
    scrambledSong = song[:crossfade_size]

    length = False
    while length == False:
        scrambledSong = scrambledSong.append(random.choice(clipList), crossfade=100)
        if len(scrambledSong) >= output_length:
            length = True

    scrambledSong = scrambledSong.fade_in(fade_time).fade_out(fade_time)

    exportPath = "%s" % exportName
    scrambledSong.export(exportPath, format="mp3")

    ##########
    ## Put your commands here and run the script.
    ## Examples:
    ## cutMP3('pref1.mp3', 'pref1_cut.mp3', 0, 60, 2)
    ## scrambleMP3('pref1_cut.mp3', 'pref1_scrambled.mp3', 0.5, 0.1, 60, 2)

    ##########

cutMP3('/Users/elise/PycharmProjects/SoundProject/audio/test.mp3',
       '/Users/elise/PycharmProjects/SoundProject/audio/test_cut.mp3', 0, 180, 2 )

scrambleMP3('/Users/elise/PycharmProjects/SoundProject/audio/test_cut.mp3',
             '/Users/elise/PycharmProjects/SoundProject/audio/test_scrambled.mp3',0.3, 180, 2)


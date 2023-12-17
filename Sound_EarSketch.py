# description: 
# this track created using the library and tool https://earsketch.gatech.edu/
# to the saved track were added an additional effect in another software.

from earsketch import *

setTempo(100)
PIANO_2 = YG_GOSPEL_PIANO_1
START_END = -60 


def line1():
    Piano_start = YG_ALT_POP_PIANO_3
    track_start = 1
    efect_mid = -15
    fitMedia(Piano_start, track_start, 1, 45) 
    setEffect(track_start, VOLUME, GAIN, START_END, 1, 0, 5)
    setEffect(track_start, VOLUME, GAIN, 0, 5, efect_mid, 10)
    setEffect(track_start, VOLUME, GAIN, efect_mid, 10, efect_mid, 30)
    setEffect(track_start, VOLUME, GAIN, efect_mid, 30, 0, 38)
    setEffect(track_start, VOLUME, GAIN, 0, 38, START_END, 45)


def line2():
    CLAP = YG_GOSPEL_CLAP_4
    track_clap_1 = 2
    fitMedia(CLAP, track_clap_1, 1, 45)
    setEffect(track_clap_1, VOLUME, GAIN, START_END, 1, 0, 5)
    setEffect(track_clap_1, VOLUME, GAIN, 0, 5, 0, 40)
    setEffect(track_clap_1, VOLUME, GAIN, 0, 40, START_END, 45)


def line3():
    SZUM_2 = YG_FUNK_SHAKER_4
    track_clap_2 = 3
    fitMedia(SZUM_2, track_clap_2, 5, 45)
    setEffect(track_clap_2, VOLUME, GAIN, START_END, 5, -10, 10)
    setEffect(track_clap_2, VOLUME, GAIN, -10, 10, -10, 40)
    setEffect(track_clap_2, VOLUME, GAIN, -10, 40, START_END, 45)


def line4():
    MUZ_6 = YG_ALT_POP_BASS_1
    track_muz = 4
    fitMedia(MUZ_6, track_muz, 5, 45)
    setEffect(track_muz, VOLUME, GAIN, START_END, 5, 10, 10)
    setEffect(track_muz, VOLUME, GAIN, 10, 10, 0, 40)
    setEffect(track_muz, VOLUME, GAIN, 0, 40, START_END, 45)


def line5():
    CLAP_2 = OS_LOWTOM04
    track_clap_2 = 5
    fitMedia(CLAP_2, track_clap_2, 1, 45) #1
    setEffect(track_clap_2, VOLUME, GAIN, START_END, 10, 5, 15)
    setEffect(track_clap_2, VOLUME, GAIN, 5, 15, 5, 35)
    setEffect(track_clap_2, VOLUME, GAIN, 5, 35, START_END, 45)


def line6():
    CLAP_2 = YG_FUNK_SNARE_8
    track_clap_3 = 6
    fitMedia(CLAP_2, track_clap_3, 1, 45)
    setEffect(track_clap_3, VOLUME, GAIN, START_END, 20, 0, 25)
    setEffect(track_clap_3, VOLUME, GAIN, 0, 25, 0, 40)
    setEffect(track_clap_3, VOLUME, GAIN, 0, 40, START_END, 45)


def all_lines():
    line1()
    line2()
    line3()
    line4()
    line5()
    line6()


if __name__ == "__main__":
    all_lines()
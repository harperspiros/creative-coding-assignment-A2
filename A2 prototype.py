from earsketch import *

init()
setTempo(112)
# =====================================

# SOUND SELECTION

kick = OS_KICK02
snare = OS_SNARE03
hat = OS_CLOSEDHAT03
openhat = OS_OPENHAT03

# DRUM PATTERNS - 16 STEPS

kickPattern = "0---0--0-0---0--"
snarePattern = "----0-------0---"
hatPattern = "0-0-0-0-0-0-0-0-"
openPattern = "--------0-------"

# =====================================
# MAIN MUSIC
# =====================================

# INTRO 

fitMedia(RD_POP_PADCHORD_2, 1, 1, 73)
fitMedia(HOUSE_ROADS_PIANO_007, 2, 1, 73)

# VERSE MINOR CHORDS

fitMedia(YG_RNB_PIANO_4, 3, 9, 73)
fitMedia(HIPHOP_BASSSUB_001, 4, 9, 73)

# CHORUS VOLUME

fitMedia(HOUSE_DEEP_SINELEAD_001, 5, 25, 73)

# EXTRA RHYTHM

fitMedia(YG_RNB_TAMBOURINE_1, 6, 17, 73)
fitMedia(YG_FUNK_HIHAT_2, 7, 25, 73)

# =====================================
# PROGRAMMED DRUMS
# =====================================

for bar in range(5, 73):

    # Main kick and snare
    makeBeat(kick, 8, bar, kickPattern)
    makeBeat(snare, 9, bar, snarePattern)

    # Hi-hats throughout the song
    if bar >= 9:
        makeBeat(hat, 10, bar, hatPattern)

    # Open hat in choruses
    if bar >= 25 and bar < 37:
        makeBeat(openhat, 11, bar, openPattern)

    if bar >= 49:
        makeBeat(openhat, 11, bar, openPattern)

# =====================================
# SONG DYNAMICS
# =====================================

# INTRO
setEffect(1, VOLUME, GAIN, -12)
setEffect(2, VOLUME, GAIN, -10)

# VERSE 
setEffect(3, VOLUME, GAIN, -5)
setEffect(4, VOLUME, GAIN, -4)

# CHORUS
setEffect(5, VOLUME, GAIN, -3)
setEffect(6, VOLUME, GAIN, -4)
setEffect(7, VOLUME, GAIN, -5)

# FINAL MIX FADE OUT
setEffect(8, VOLUME, GAIN, -3)
setEffect(9, VOLUME, GAIN, -4)
setEffect(10, VOLUME, GAIN, -7)
setEffect(11, VOLUME, GAIN, -8)

finish()
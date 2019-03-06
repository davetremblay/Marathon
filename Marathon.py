#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Feb 23 08:03:51 2019

Marathon is a program to automatically create microrhythm between two rhythmic
patterns in MIDI.

Maraton offers a range of preset patterns and a text command option to create
custom patterns.

@author: DaveTremblay
"""

import presets


def main():
    preset_options = """
Choose preset

1: Swing (q q / q. e)
2: Half-Swing (h q q / h q. e)
3: West African Triplet (e e e / e s s)
4: Gnawa Triplet (e e e / e s e)
5: Brazilian 16ths (s s s s / e s s e)
6: Braff's Quintuplet (s s s s s / e s s e s)
7: Viennese Waltz (q q q / e. s-q q)
99: Text Command
"""
    print(preset_options)
    preset = input("Enter number: ")
    comm1 = ""
    comm2 = ""
    morph1 = ""
    morph2 = ""
    repeats = ""

    morph_examples_1 = """
Examples
0: 1:1 Straight Quarter Notes
29: ~4:3 Septuplet Feel
40: 3:2 Quintuplet Feel
50: 5:3 Eighth Feel
66.7: 2:1 Triplet Feel
85.7: ~5:2 Septuplet Feel
100: 3:1 Hard Swing
"""

    morph_examples_2 = """
Examples
0: 1:1:1 Straight Triplet Notes
50: Halfway Morph
100: 2:1:1 16ths Gallop
"""

    morph_examples_3 = """
Examples
0: 1:1:1 Straight Triplet Notes
50: Halfway Morph
100: 2:1:2 Quintuplet Feel
"""

    morph_examples_4 = """
Examples
0: 1:1:1:1 Straight 16th Notes
50: Halfway Morph
100: 2:1:1:2 Sixtuplet Feel
"""

    morph_examples_5 = """
Examples
0: 1:1:1:1:1 Straight Quintuplets
50: Halfway Morph
100: 2:1:1:2:1 Septuplet Feel
"""

    morph_examples_6 = """
Examples
0: 1:1:1 Straight Quarter Notes
50: Halfway Morph
65: Recommended Morph
100: 3:5:4 16ths Feel
"""

    if preset == "1":
        print(morph_examples_1)
        morph1 = input("Enter starting morph value (0-100): ")
        morph2 = input("Enter ending morph value (0-100): ")
        repeats = input("How many repetitions do you want?: ")
        presets.swing(morph1, morph2, repeats)

    elif preset == "2":
        print(morph_examples_1)
        morph1 = input("Enter starting morph value (0-100): ")
        morph2 = input("Enter ending morph value (0-100): ")
        repeats = input("How many repetitions do you want?: ")
        presets.half_swing(morph1, morph2, repeats)

    elif preset == "3":
        print(morph_examples_2)
        morph1 = input("Enter starting morph value (0-100): ")
        morph2 = input("Enter ending morph value (0-100): ")
        repeats = input("How many repetitions do you want?: ")
        presets.west_african_triplet(morph1, morph2, repeats)

    elif preset == "4":
        print(morph_examples_3)
        morph1 = input("Enter starting morph value (0-100): ")
        morph2 = input("Enter ending morph value (0-100): ")
        repeats = input("How many repetitions do you want?: ")
        presets.gwana_triplet(morph1, morph2, repeats)

    elif preset == "5":
        print(morph_examples_4)
        morph1 = input("Enter starting morph value (0-100): ")
        morph2 = input("Enter ending morph value (0-100): ")
        repeats = input("How many repetitions do you want?: ")
        presets.brazilian_sixteens(morph1, morph2, repeats)

    elif preset == "6":
        print(morph_examples_5)
        morph1 = input("Enter starting morph value (0-100): ")
        morph2 = input("Enter ending morph value (0-100): ")
        repeats = input("How many repetitions do you want?: ")
        presets.braffs_quintuplets(morph1, morph2, repeats)

    elif preset == "7":
        print(morph_examples_6)
        morph1 = input("Enter starting morph value (0-100): ")
        morph2 = input("Enter ending morph value (0-100): ")
        repeats = input("How many repetitions do you want?: ")
        presets.vienesse_waltz(morph1, morph2, repeats)

    elif preset == "99":
        text_notation = """
Separate each note by a space, tied notes with a dash

Notes
w: whole note
h: half note
q: quarter note
e: eighth note
s: sixteenth note
t: thirty-second note

Dots (after the note)
.: dotted
..: double dotted
...: triple dotted

Tuplets (after note and dots)
x/y: where x-tuplet notes are to be played in y non-tuplet notes

Rest (at the end)
r
"""
        print(text_notation)
        comm1 = input("Enter text command (track 1): ")
        comm2 = input("Enter text command (track 2): ")
        morph1 = input("Enter starting morph value (0-100): ")
        morph2 = input("Enter ending morph value (0-100): ")
        repeats = input("How many repetitions do you want?: ")
        presets.text_command(morph1, morph2, repeats, comm1, comm2)


# Execute the main program if this file is not being imported as a module
if __name__ == "__main__":
    main()

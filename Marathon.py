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

import os
try:
    import jinja2
except ImportError:
    import pip
    pip.main(['install','jinja2'])
import presets

def main():
    preset_options = """
Marathon: Microrhythm Generation Software

Choose preset

1: Swing (2(q) / q. e)
2: West African Triplet (3(q) / e 2(s))
3: Gnawa Triplet (3(e) / e s e)
4: Brazilian 16ths (4(s) / e 2(s) e)
5: Braff's Quintuplet (5(s) / e 2(s) e s)
6: Viennese Waltz (3(q) / e. s-q q)
0: Text Command
"""
    print(preset_options)
    preset = input("Enter number: ")
    while str(preset) not in "0 1 2 3 4 5 6":
        print(preset_options)
        print("Invalid preset. Try again.")
        preset = input("Enter number: ")
    comm1 = ""
    comm2 = ""
    morph1 = ""
    morph2 = ""
    pattern_tick = ""
    repeats = ""

    morph_examples_2 = """
Examples
0:   1:1:1 Straight Triplet Notes
50:  Halfway Morph
100: 2:1:1 Sixteenths Gallop
"""

    morph_examples_3 = """
Examples
0:   1:1:1 Straight Triplet Notes
50:  Halfway Morph
100: 2:1:2 Quintuplet Feel
"""

    morph_examples_4 = """
Examples
0:   1:1:1:1 Straight Sixteenth Notes
50:  Halfway Morph
100: 2:1:1:2 Sixtuplet Feel
"""

    morph_examples_5 = """
Examples
0:   1:1:1:1:1 Straight Quintuplets
50:  Halfway Morph
100: 2:1:1:2:1 Septuplet Feel
"""

    morph_examples_6 = """
Examples
0:   1:1:1 Straight Quarter Notes
50:  Halfway Morph
65:  Recommended Morph
100: 3:5:4 Sixteenths Feel
"""

    if preset == "1":

        swing_options = """
    Choose preset

    Base-4 Swing (up to 3:1):
    1: Half-Bar Swing (2(q) / q. e)
    2: Full-Bar Swing (h 2(q) / h q. e)

    Base-16 Swing (up to 15:1):
    3: Half-Bar Swing (2(q) / q... t)
    4: Full-Bar Swing (h 2(q) / h q... t)
    """
        print(swing_options)
        swing_preset = input("Enter number: ")
        while str(swing_preset) not in "1 2 3 4":
            print(swing_options)
            print("Invalid preset. Try again.")
            swing_preset = input("Enter number: ")
        comm1 = ""
        comm2 = ""
        morph1 = ""
        morph2 = ""
        repeats = ""

        swing_examples_1 = """
    Examples
    0:    1:1 Straight Quarter Notes
    28.6: 4:3 Septuplet Feel
    40:   3:2 Quintuplet Feel
    50:   5:3 Sixteenths Feel
    66.7: 2:1 Triplet Feel
    85.7: 5:2 Septuplet Feel
    100:  3:1 Eighths Feel
    """

        swing_examples_2 = """
    Examples
    0:     1:1 Straight Quarter Notes
    16.3:  4:3 Septuplet Feel
    22.9:  3:2 Quintuplet Feel
    28.6:  5:3 Sixteenths Feel
    38.1:  2:1 Triplet Feel
    49:    5:2 Septuplet Feel
    57.1:  3:1 Eighths Feel
    68.6:  4:1 Quintuplet Feel
    76.2:  5:1 Sextuplet Feel
    81.6:  6:1 Septuplet Feel
    85.7:  7:1 Sixteenths Feel
    88.9:  8:1 Nonuplet Feel
    91.4:  9:1 Quintuplet Feel
    93.5: 10:1 Undecuplet Feel
    95.2: 11:1 Sextuplet Feel
    96.7: 12:1 Tridecuplet Feel
    98:   13:1 Septuplet Feel
    99:   14:1 Quindecuplet Feel
    100:  15:1 Thirty-Seconds Feel

   """
        if swing_preset == "1" or swing_preset == "2":
            print(swing_examples_1)
            ok = 0
            while ok == 0:
                try:
                    morph1_in = input("Enter starting morph value (0-100): ")
                    morph1 = float(morph1_in)
                    if morph1 >= 0 and morph1 <= 100:
                        ok += 1
                    else:
                        print("Invalid value. Must be between 0 and 100.")
                except ValueError:
                    print(swing_examples_1)
                    print("Invalid value. Try again.")
            ok = 0
            while ok == 0:
                try:
                    morph2_in = input("Enter ending morph value (0-100): ")
                    morph2 = float(morph2_in)
                    if morph2 >= 0 and morph2 <= 100:
                        ok += 1
                    else:
                        print("Invalid value. Must be between 0 and 100.")
                except ValueError:
                    print(swing_examples_1)
                    print("Invalid value. Try again.")
            ok = 0
            while ok == 0:
                try:
                    repeats_in = input("How many repetitions do you want?: ")
                    repeats = float(repeats_in)
                    if repeats > 0:
                        ok += 1
                    else:
                        print("Invalid value. Must be greater than 0.")
                except ValueError:
                    print("Invalid value. Try again.")

            if swing_preset == "1":
                presets.swing(morph1, morph2, repeats)
            elif swing_preset == "2":
                presets.half_swing(morph1, morph2, repeats)

        if swing_preset == "3" or swing_preset == "4":
            print(swing_examples_2)
            ok = 0
            while ok == 0:
                try:
                    morph1_in = input("Enter starting morph value (0-100): ")
                    morph1 = float(morph1_in)
                    if morph1 >= 0 and morph1 <= 100:
                        ok += 1
                    else:
                        print("Invalid value. Must be between 0 and 100.")
                except ValueError:
                    print(swing_examples_2)
                    print("Invalid value. Try again.")
            ok = 0
            while ok == 0:
                try:
                    morph2_in = input("Enter ending morph value (0-100): ")
                    morph2 = float(morph2_in)
                    if morph2 >= 0 and morph2 <= 100:
                        ok += 1
                    else:
                        print("Invalid value. Must be between 0 and 100.")
                except ValueError:
                    print(swing_examples_2)
                    print("Invalid value. Try again.")
            ok = 0
            while ok == 0:
                try:
                    repeats_in = input("How many repetitions do you want?: ")
                    repeats = float(repeats_in)
                    if repeats > 0:
                        ok += 1
                    else:
                        print("Invalid value. Must be greater than 0.")
                except ValueError:
                    print("Invalid value. Try again.")
            if swing_preset == "3":
                presets.hard_swing(morph1, morph2, repeats)
            elif swing_preset == "4":
                presets.half_hard_swing(morph1, morph2, repeats)

    elif preset == "2":
        print(morph_examples_2)
        ok = 0
        while ok == 0:
            try:
                morph1_in = input("Enter starting morph value (0-100): ")
                morph1 = float(morph1_in)
                if morph1 >= 0 and morph1 <= 100:
                    ok += 1
                else:
                    print("Invalid value. Must be between 0 and 100.")
            except ValueError:
                print(morph_examples_2)
                print("Invalid value. Try again.")
        ok = 0
        while ok == 0:
            try:
                morph2_in = input("Enter ending morph value (0-100): ")
                morph2 = float(morph2_in)
                if morph2 >= 0 and morph2 <= 100:
                    ok += 1
                else:
                    print("Invalid value. Must be between 0 and 100.")
            except ValueError:
                print(morph_examples_2)
                print("Invalid value. Try again.")
        ok = 0
        while ok == 0:
            try:
                repeats_in = input("How many repetitions do you want?: ")
                repeats = float(repeats_in)
                if repeats > 0:
                    ok += 1
                else:
                    print("Invalid value. Must be greater than 0.")
            except ValueError:
                print("Invalid value. Try again.")
        presets.west_african_triplet(morph1, morph2, repeats)

    elif preset == "3":
        print(morph_examples_3)
        ok = 0
        while ok == 0:
            try:
                morph1_in = input("Enter starting morph value (0-100): ")
                morph1 = float(morph1_in)
                if morph1 >= 0 and morph1 <= 100:
                    ok += 1
                else:
                    print("Invalid value. Must be between 0 and 100.")
            except ValueError:
                print(morph_examples_3)
                print("Invalid value. Try again.")
        ok = 0
        while ok == 0:
            try:
                morph2_in = input("Enter ending morph value (0-100): ")
                morph2 = float(morph2_in)
                if morph2 >= 0 and morph2 <= 100:
                    ok += 1
                else:
                    print("Invalid value. Must be between 0 and 100.")
            except ValueError:
                print(morph_examples_3)
                print("Invalid value. Try again.")
        ok = 0
        while ok == 0:
            try:
                repeats_in = input("How many repetitions do you want?: ")
                repeats = float(repeats_in)
                if repeats > 0:
                    ok += 1
                else:
                    print("Invalid value. Must be greater than 0.")
            except ValueError:
                print("Invalid value. Try again.")
        presets.gwana_triplet(morph1, morph2, repeats)

    elif preset == "4":
        print(morph_examples_4)
        ok = 0
        while ok == 0:
            try:
                morph1_in = input("Enter starting morph value (0-100): ")
                morph1 = float(morph1_in)
                if morph1 >= 0 and morph1 <= 100:
                    ok += 1
                else:
                    print("Invalid value. Must be between 0 and 100.")
            except ValueError:
                print(morph_examples_4)
                print("Invalid value. Try again.")
        ok = 0
        while ok == 0:
            try:
                morph2_in = input("Enter ending morph value (0-100): ")
                morph2 = float(morph2_in)
                if morph2 >= 0 and morph2 <= 100:
                    ok += 1
                else:
                    print("Invalid value. Must be between 0 and 100.")
            except ValueError:
                print(morph_examples_4)
                print("Invalid value. Try again.")
        ok = 0
        while ok == 0:
            try:
                repeats_in = input("How many repetitions do you want?: ")
                repeats = float(repeats_in)
                if repeats > 0:
                    ok += 1
                else:
                    print("Invalid value. Must be greater than 0.")
            except ValueError:
                print("Invalid value. Try again.")
        presets.brazilian_sixteens(morph1, morph2, repeats)

    elif preset == "5":
        print(morph_examples_5)
        ok = 0
        while ok == 0:
            try:
                morph1_in = input("Enter starting morph value (0-100): ")
                morph1 = float(morph1_in)
                if morph1 >= 0 and morph1 <= 100:
                    ok += 1
                else:
                    print("Invalid value. Must be between 0 and 100.")
            except ValueError:
                print(morph_examples_5)
                print("Invalid value. Try again.")
        ok = 0
        while ok == 0:
            try:
                morph2_in = input("Enter ending morph value (0-100): ")
                morph2 = float(morph2_in)
                if morph2 >= 0 and morph2 <= 100:
                    ok += 1
                else:
                    print("Invalid value. Must be between 0 and 100.")
            except ValueError:
                print(morph_examples_5)
                print("Invalid value. Try again.")
        ok = 0
        while ok == 0:
            try:
                repeats_in = input("How many repetitions do you want?: ")
                repeats = float(repeats_in)
                if repeats > 0:
                    ok += 1
                else:
                    print("Invalid value. Must be greater than 0.")
            except ValueError:
                print("Invalid value. Try again.")
        presets.braffs_quintuplets(morph1, morph2, repeats)

    elif preset == "6":
        print(morph_examples_6)
        ok = 0
        while ok == 0:
            try:
                morph1_in = input("Enter starting morph value (0-100): ")
                morph1 = float(morph1_in)
                if morph1 >= 0 and morph1 <= 100:
                    ok += 1
                else:
                    print("Invalid value. Must be between 0 and 100.")
            except ValueError:
                print(morph_examples_6)
                print("Invalid value. Try again.")
        ok = 0
        while ok == 0:
            try:
                morph2_in = input("Enter ending morph value (0-100): ")
                morph2 = float(morph2_in)
                if morph2 >= 0 and morph2 <= 100:
                    ok += 1
                else:
                    print("Invalid value. Must be between 0 and 100.")
            except ValueError:
                print(morph_examples_6)
                print("Invalid value. Try again.")
        ok = 0
        while ok == 0:
            try:
                repeats_in = input("How many repetitions do you want?: ")
                repeats = float(repeats_in)
                if repeats > 0:
                    ok += 1
                else:
                    print("Invalid value. Must be greater than 0.")
            except ValueError:
                print("Invalid value. Try again.")
        presets.vienesse_waltz(morph1, morph2, repeats)

    elif preset == "0":
        text_notation = """
Notes
w: whole note
h: half note
q: quarter note
e: eighth note
s: sixteenth note
t: thirty-second note

Dots (after the note)
.:   dotted
..:  double dotted
...: triple dotted (and so on)

Tuplets (after note and dots)
x/y: where x-tuplet notes are to be played in y non-tuplet notes

Rest (at the end)
r

Single Note Repetition
x(note): where x is an integer and "note" is the repeated note

Separate each note by a space, tied notes with a dash
"""
        print(text_notation)
        comm1 = input("Enter text command (track 1): ")
        comm2 = input("Enter text command (track 2): ")
        ok = 0
        while ok == 0:
            try:
                morph1_in = input("Enter starting morph value (0-100): ")
                morph1 = float(morph1_in)
                if morph1 >= 0 and morph1 <= 100:
                    ok += 1
                else:
                    print("Invalid value. Must be between 0 and 100.")
            except ValueError:
                print("Invalid value. Try again.")
        ok = 0
        while ok == 0:
            try:
                morph2_in = input("Enter ending morph value (0-100): ")
                morph2 = float(morph2_in)
                if morph2 >= 0 and morph2 <= 100:
                    ok += 1
                else:
                    print("Invalid value. Must be between 0 and 100.")
            except ValueError:
                print("Invalid value. Try again.")
        ok = 0
        while ok == 0:
            try:
                pattern_tick_in = input("""
w: whole note =        3840 ticks
h: half note =         1920 ticks
q: quarter note =       960 ticks
e: eighth note =        480 ticks
s: sixteenth note =     240 ticks
t: thirty-second note = 120 ticks

Enter the total tick value of the pattern: """)
                pattern_tick = int(pattern_tick_in)
                if pattern_tick > 0:
                    ok += 1
                else:
                    print("Invalid value. Must be greater than 0.")
            except ValueError:
                print("Invalid value. Try again.")
        ok = 0
        while ok == 0:
            try:
                repeats_in = input("How many repetitions do you want?: ")
                repeats = float(repeats_in)
                if repeats > 0:
                    ok += 1
                else:
                    print("Invalid value. Must be greater than 0.")
            except ValueError:
                print("Invalid value. Try again.")
        presets.text_command(morph1, morph2, repeats, comm1, comm2, pattern_tick)


# Execute the main program if this file is not being imported as a module
while __name__ == "__main__":
    main()

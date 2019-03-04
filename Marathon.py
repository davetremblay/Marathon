#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import midi

"""
Created on Sat Feb 23 08:03:51 2019

Marathon is a program to automatically create microrhythm between two rhythmic 
patterns in MIDI.

Maraton offers a range of preset patterns and a text command option to create
custom patterns.

@author: DaveTremblay
"""


def main():
    preset = input("Choose preset \n\n1: Swing (q q / q. e)\n2: Half-Swing (h q q / h q. e)\n3: West African Triplet (e e e / e s s)\n4: Gnawa Triplet (e e e / e s e)\n5: Brazilian 16ths (s s s s / e s s e)\n6: Braff's Quintuplet (s s s s s / e s s e s)\n7: Viennese Waltz (q q q / e. s-q q)\n99: Text Command\n\nEnter number: ")
    comm1 = ""
    comm2 = ""
    morph1 = ""
    morph2 = ""
    repeats = ""

    if str(preset) == "1":
        morph1 = input("Enter starting morph value (0-100)\n\nExamples\n0: 1:1 Straight Quarter Notes\n29: ~4:3 Septuplet Feel\n40: 3:2 Quintuplet Feel\n50: 5:3 Eighth Feel\n66.7: 2:1 Triplet Feel \n85.7: ~5:2 Septuplet Feel\n100: 3:1 Hard Swing\n\nEnter starting morph value (0-100): ")
        morph2 = input("Enter ending morph value (0-100)\n\nExamples\n0: 1:1 Straight Quarter Notes\n29: ~4:3 Septuplet Feel\n40: 3:2 Quintuplet Feel\n50: 5:3 Eighth Feel\n66.7: 2:1 Triplet Feel \n85.7: ~5:2 Septuplet Feel\n100: 3:1 Hard Swing\n\nEnter ending morph value (0-100): ")
        repeats = input("How many repetitions do you want?: ")
        Marathon(preset, comm1, comm2, morph1, morph2, repeats)

    elif str(preset) == "2":
        morph1 = input("Enter starting morph value (0-100)\n\nExamples\n0: 1:1 Straight Quarter Notes\n29: ~4:3 Septuplet Feel\n40: 3:2 Quintuplet Feel\n50: 5:3 Eighth Feel\n66.7: 2:1 Triplet Feel \n85.7: ~5:2 Septuplet Feel\n100: 3:1 Hard Swing\n\nEnter starting morph value (0-100): ")
        morph2 = input("Enter ending morph value (0-100)\n\nExamples\n0: 1:1 Straight Quarter Notes\n29: ~4:3 Septuplet Feel\n40: 3:2 Quintuplet Feel\n50: 5:3 Eighth Feel\n66.7: 2:1 Triplet Feel \n85.7: ~5:2 Septuplet Feel\n100: 3:1 Hard Swing\n\nEnter ending morph value (0-100): ")
        repeats = input("How many repetitions do you want?: ")
        Marathon(preset, comm1, comm2, morph1, morph2, repeats)

    elif str(preset) == "3":
        morph1 = input("Enter starting morph value (0-100)\n\nExamples\n0: 1:1:1 Straight Triplet Notes\n50: Halfway Morph\n100: 2:1:1 16ths Gallop\n\nEnter starting morph value (0-100): ")
        morph2 = input(
            "Enter ending morph value (0-100)\n\nExamples\n0: 1:1:1 Straight Triplet Notes\n50: Halfway Morph\n100: 2:1:1 16ths Gallop\n\nEnter ending morph value (0-100): ")
        repeats = input("How many repetitions do you want?: ")
        Marathon(preset, comm1, comm2, morph1, morph2, repeats)

    elif str(preset) == "4":
        morph1 = input("Enter starting morph value (0-100)\n\nExamples\n0: 1:1:1 Straight Triplet Notes\n50: Halfway Morph\n100: 2:1:2 Quintuplet Feel\n\nEnter starting morph value (0-100): ")
        morph2 = input("Enter ending morph value (0-100)\n\nExamples\n0: 1:1:1 Straight Triplet Notes\n50: Halfway Morph\n100: 2:1:2 Quintuplet Feel\n\nEnter ending morph value (0-100): ")
        repeats = input("How many repetitions do you want?: ")
        Marathon(preset, comm1, comm2, morph1, morph2, repeats)

    elif str(preset) == "5":
        morph1 = input("Enter starting morph value (0-100)\n\nExamples\n0: 1:1:1:1 Straight 16th Notes\n50: Halfway Morph\n100: 2:1:1:2 Sixtuplet Feel\n\nEnter starting morph value (0-100): ")
        morph2 = input("Enter ending morph value (0-100)\n\nExamples\n0: 1:1:1:1 Straight 16th Notes\n50: Halfway Morph\n100: 2:1:1:2 Sixtuplet Feel\n\nEnter ending morph value (0-100): ")
        repeats = input("How many repetitions do you want?: ")
        Marathon(preset, comm1, comm2, morph1, morph2, repeats)

    elif str(preset) == "6":
        morph1 = input("Enter starting morph value (0-100)\n\nExamples\n0: 1:1:1:1:1 Straight Quintuplets\n50: Halfway Morph\n100: 2:1:1:2:1 Septuplet Feel\n\nEnter starting morph value (0-100): ")
        morph2 = input("Enter ending morph value (0-100)\n\nExamples\n0: 1:1:1:1:1 Straight Quintuplets\n50: Halfway Morph\n100: 2:1:1:2:1 Septuplet Feel\n\nEnter ending morph value (0-100): ")
        repeats = input("How many repetitions do you want?: ")
        Marathon(preset, comm1, comm2, morph1, morph2, repeats)

    elif str(preset) == "7":
        morph1 = input("Enter starting morph value (0-100)\n\nExamples\n0: 1:1:1 Straight Quarter Notes\n50: Halfway Morph\n65: Recommended Morph\n100: 3:5:4 16ths Feel\n\nEnter starting morph value (0-100): ")
        morph2 = input("Enter ending morph value (0-100)\n\nExamples\n0: 1:1:1 Straight Quarter Notes\n50: Halfway Morph\n65: Recommended Morph\n100: 3:5:4 16ths Feel\n\nEnter ending morph value (0-100): ")
        repeats = input("How many repetitions do you want?: ")
        Marathon(preset, comm1, comm2, morph1, morph2, repeats)

    elif str(preset) == "99":
        comm1 = input("Enter text notation for track 1\n\nSeparate each note by a space, tied notes with a dash\n\nNotes\nw: whole note\nh: half note\nq: quarter note\ne: eighth note\ns: sixteenth note\nt: thirty-second note\n\nDots (after the note)\n.: dotted\n..: double dotted\n...: triple dotted\n\nTuplets (after note and dots)\nx/y: where x-tuplet notes are to be played in y non-tuplet notes\n\nRest (at the end)\nr\n\nEnter text command (track 1): ")
        comm2 = input("Enter text notation for track 2\n\nSeparate each note by a space, tied notes with a dash\n\nNotes\nw: whole note\nh: half note\nq: quarter note\ne: eighth note\ns: sixteenth note\nt: thirty-second note\n\nDots (after the note)\n.: dotted\n..: double dotted\n...: triple dotted\n\nTuplets (after note and dots)\nx/y: where x-tuplet notes are to be played in y non-tuplet notes\n\nRest (at the end)\nr\n\nEnter text command (track 2): ")
        if len(str(comm1).split(" ")) != len(str(comm2).split(" ")):
            print("Error: The number of notes in the two tracks is different.")
            raise SystemExit
        morph1 = input("Enter starting morph value (0-100): ")
        morph2 = input("Enter ending morph value (0-100): ")
        repeats = input("How many repetitions do you want?: ")
        Marathon(preset, comm1, comm2, morph1, morph2, repeats)


# Execute the main program if this file is not being imported as a module
if __name__ == "__main__":
    main()

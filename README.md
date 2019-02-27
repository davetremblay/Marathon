# Marathon

Marathon is a program to automatically create a 50% microrhythm between two
rhythmic patterns in MIDI.

For more information about microrhythms, follow the link https://wp.me/p3mIfa-off

Marathon takes a MIDI file by the name "marathon_in.mid" located in the same
folder as itself containing two MIDI tracks of same length and number of notes.
Marathon then creates the file "marathon_out.mid" by calculating the average
duration of each note pair in the two tracks and copying the channel, velocity,
and pitch pattern of the first track.

As of February 26, 2019, Marathon can also generate microrhythms for you,
without having to feed it a MIDI file. You can select from 6 different
rhythmic classes (like Swing Feel, Gnawa Triplet, or Brazilian 16ths), and
apply a morph value of your desire to create a microrhythm. For this feature  the program will output a file by the name "marathon_out.mid" that contains
the rhythmic pattern placed by default on C4 (note 60).

## Installation

You need to install [python-midi](python-midi). Then, just type 

```console
$ python Marathon.py`
```

in a terminal, and enjoy the program.

## Example Usage

### Creating a 3:2 Quintuplet Feel Swing

Starting the program:
```console
$ python Marathon.py
```

The program will ask you for a preset:
```console
Choose preset

1: Custom File
2: Swing
3: Half-Swing
4: West African Triplet
5: Gnawa Triplet
6: Brazilian 16ths
7: Braff's Quintuplet
8: Viennese Waltz

Enter number:
3
```

Then for a morph value:
```console
Enter morph value (0-100)

Examples
0: 1:1 Straight Quarter Notes
29: ~4:3 Septuplet Feel
40: 3:2 Quintuplet Feel
50: 5:3 Eighth Feel
66.7: 2:1 Triplet Feel
85.7: ~5:2 Septuplet Feel
100: 3:1 Hard Swing

Enter number:
40
```

And finally how many repetitions you need:
```console
How many repetitions do you want?:
32
```

You will then find the file `marathon_out.mid` in the same directory, which you can freely import in a digital audio workstation (DAW) and do as you wish.

## Known issues
* Does not work properly with chords and multiple voices on one track.
* May behave unexpectedly with time signatures or tempo changes and other more complex actions.

## Suggestions
* Create simple MIDI files with a DAW to feed the program.
* Create monophonic tracks. If you want multiphonic results, I suggest you create a MIDI file for each voice. Remember to write the same number of notes in each track if you want similar results. You can then manually recombine the different output files into one track on a DAW.
* Tempo or time signature change, note bends, and other more complex actions are to be avoided for better results. You can apply those changes manually on the output track.

## Author
Dave Tremblay

# Marathon

Marathon is a program to automatically create a microrhythm between two rhythmic patterns in MIDI.

For more information about microrhythms, follow the link https://wp.me/p3mIfa-off

Maraton offers a range of preset patterns and a text command option to create
custom patterns.

As of February 26, 2019, Marathon can also generate microrhythms for you,
without having to feed it a MIDI file. You can select from 6 different
rhythmic classes (like Swing Feel, Gnawa Triplet, or Brazilian 16ths), and
apply a morph value of your desire to create a microrhythm. For this feature  the program will output a file by the name "marathon_out.mid" that contains
the rhythmic pattern placed by default on C4 (note 60).

As of February 27, 2019, Marathon can also generate custom microrhythms. You can select preset "99" and write your two rhythm tracks using text commands. Marathon accepts note length (from whole to thirty-second notes), dots (up to 3), and tuplet feel (Marathon is very flexible regarding tuplets, as they don't need to be whole to be accepted). The syntax is "z(ndx/yr)":
* z is the number of note repetitions (optional)
  * z is a great way to quickly write out multiple repeated notes
* n is the note value (mandatory)
* d is the place for dots (optional)
* x/y is the tuplet space (it must be two integers separated by "/") (optional)
  * Tuplets also allow you to write smaller or greater note subdivisions, for example a quarter note can be written out as "q", but also "h2/1" or "e1/2". This can be useful for writing very short or very long notes.
* r denotes rest notes (optional)
* Each note must be separated by a space or dash ("-") for tied notes

As of March 3, Marathon doesn't support MIDI input anymore due to problems with reading them and the redundancy with Text Command. It also now supports progressive morphing. You can write two morph values and the program will create a MIDI file that progressively moves from the former to the latter. Moreover, there has been work put into diminishing the offset between the notes and the grid.

As of March 6, Marathon Text Command supports shorthand notation for repeated notes. For example, you can now write 16(e) to make the program play 16 eighth notes instead of writing 16 separate "e". You can also write multiple tied notes like 4(e-s.), which will give "e-s." four times, but not one note with multiple ties like *e-4(s.)*.

You can then choose a morph value and a number of repetitions, and then the program will export the completed MIDI track as "marathon_out.mid".

As of May 4, Marathon supports morph values outside of the 0-100 range.

## Installation
You need to install [python-midi](https://github.com/vishnubob/python-midi) before running Marathon.py.

## Example Usage

### Creating a 3:2 Quintuplet Feel Swing
Starting the program:

```console
$ python Marathon.py
```

The program will ask you for a preset:

```console
Choose preset

1: Swing (2(q) / q. e)
2: West African Triplet (3(q) / e 2(s))
3: Gnawa Triplet (3(e) / e s e)
4: Brazilian 16ths (4(s) / e 2(s) e)
5: Braff's Quintuplet (5(s) / e 2(s) e s)
6: Viennese Waltz (3(q) / e. s-q q)
0: Text Command

Enter number:
1
```

If you choose Swing, there are more preset options. You can choose between a narrow (base-8) and broad (base-16) range of swing ratios.

```console
Choose preset

Base-4 Swing (up to 3:1):
1: Half-Bar Swing (2(q) / q. e)
2: Full-Bar Swing (h 2(q) / h q. e)

Base-16 Swing (up to 15:1):
3: Half-Bar Swing (2(q) / q... t)
4: Full-Bar Swing (h 2(q) / h q... t)

Enter number:
1
```

Then for starting and ending morph values:

```console
Enter starting morph value (%)

Examples
0:    1:1 Straight Quarter Notes
29:   4:3 Septuplet Feel
40:   3:2 Quintuplet Feel
50:   5:3 Eighth Feel
66.7: 2:1 Triplet Feel
85.7: 5:2 Septuplet Feel
100:  3:1 Eighth Feel

Enter starting morph value (%):
40

Enter ending morph value (%)

Examples
0:    1:1 Straight Quarter Notes
29:   4:3 Septuplet Feel
40:   3:2 Quintuplet Feel
50:   5:3 Eighth Feel
66.7: 2:1 Triplet Feel
85.7: 5:2 Septuplet Feel
100:  3:1 Eighth Feel

Enter ending morph value (%):
60
```

And finally how many repetitions you need:

```console
How many repetitions do you want?:
32
```

You will then find the file `marathon_out.mid` in the same directory, which you can freely import in a digital audio workstation (DAW) and do as you wish.


## Using Text Command
Select preset "0" for Text Command and you will see the vocabulary:

```console
Enter text notation for track 1

Separate each note by a space

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
...: triple dotted

Tuplets (after note and dots)
x/y: where x-tuplet notes are to be played in y non-tuplet notes

Rest (at the end)
r

Enter text command (track 1):
```

Valid example:

```console
(track 1): 1(q) q-s... q-e-s-t q
(track 2): q. e w.3/4 t11/10-s...5/3
```

Invalid example:
```console
(track 1): 3(qq) q--e q.... q2//3
(track 2): d.-2(e) ..e 3/4w t11/t s,5/3
```

Then Marathon will ask for a morph value and a number of repetitions.

## Author
Dave Tremblay

# Marathon
Marathon is a program to automatically create a 50% microrhythm between two
rhythmic patterns in MIDI.

For more information about microrhythms, follow the link https://wp.me/p3mIfa-off

Maraton takes a MIDI file by the name "marathon_in.mid" located in the same
folder as itself containing two MIDI tracks of same length and number of notes.
Marathon then creates the file "marathon_out.mid" by calculating the average
duration of each note pair in the two tracks and copying the channel, velocity,
and pitch pattern of the first track.

Known issues:

    —Does not work properly with chords and multiple voices on one track.
    —May behave unexpectedly with time signatures or tempo changes and other
        more complex actions.

Suggestions:

    —Create simple MIDI files with a DAW to feed the program.
    —Create monophonic tracks. If you want multiphonic results, I suggest you
        create a MIDI file for each voice. Remember to write the same number of
        notes in each track if you want similar results. You can then manually
        recombine the different output files into one track on a DAW.
    —Tempo or time signature change, note bends, and other more complex actions
        are to be avoided for better results. You can apply those changes
        manually on the output track.

Dave Tremblay

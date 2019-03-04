"""asjdlajslkdaslj"""

import midi


def swing(morph, repeats):
    """TODO: Docstring for Swing.

    Args:
        morph: TODO
        repeats: TODO

    Returns: TODO

    """
    file_out = "marathon_out.mid"

    # straight
    notes1 = [0, 960, 0, 960]

    # phrased
    notes2 = [0, 1440, 0, 480]

    fm = 1
    rm = 960

    pat = midi.Pattern(format=int(fm), resolution=int(rm))
    tra = midi.Track()
    pat.append(tra)

    # pattern weight (must add up to 1.0)
    w1 = 1-float(morph)/100
    w2 = float(morph)/100

    # rounding correction
    rc = 0

    for n in range(int(repeats)):
        e = 0
        for event in notes2:
            tick1 = int(notes1[e])
            tick2 = int(notes2[e])

            # rounding correction
            rc += (w1 * tick1) + (w2 * tick2) - float(int(w1 * tick1) + (w2 * tick2))

            if rc % 1 < -0.5:
                tickm = int((w1 * tick1) + (w2 * tick2)) + int(rc) - 1
                rc = 0
            elif rc % 1 >= 0.5:
                tickm = int((w1 * tick1) + (w2 * tick2)) + int(rc) + 1
                rc = 0
            else:
                tickm = int((w1 * tick1) + (w2 * tick2)) + int(rc)
                rc = 0

            noteon = midi.NoteOnEvent(tick=0, channel=0, data=[60, 70])
            tra.append(noteon)
            noteoff = midi.NoteOffEvent(tick=tickm, channel=0, data=[60, 0])
            tra.append(noteoff)

            e += 1

        else:
            e += 1

    trackend = midi.EndOfTrackEvent(tick=1)
    tra.append(trackend)
    midi.write_midifile(file_out, pat)


def half_swing(morph, repeats):
    """TODO: Docstring for HalfSwing.

    Args:
        morph: TODO
        repeats: TODO

    Returns: TODO

    """

    file_out = "marathon_out.mid"

    # straight
    notes1 = [0, 1920, 0, 960, 0, 960]
    # phrased
    notes2 = [0, 1920, 0, 1440, 0, 480]

    fm = 1
    rm = 960

    pat = midi.Pattern(format=int(fm), resolution=int(rm))
    tra = midi.Track()
    pat.append(tra)

    # pattern weight (must add up to 1.0)
    w1 = 1-float(morph)/100
    w2 = float(morph)/100

    # rounding correction
    rc = 0

    for n in range(int(repeats)):
        e = 0
        for event in notes2:
            tick1 = int(notes1[e])
            tick2 = int(notes2[e])

            # rounding correction
            rc += (w1 * tick1) + (w2 * tick2) - float(int(w1 * tick1) + (w2 * tick2))

            if rc % 1 < -0.5:
                tickm = int((w1 * tick1) + (w2 * tick2)) + int(rc) - 1
                rc = 0
            elif rc % 1 >= 0.5:
                tickm = int((w1 * tick1) + (w2 * tick2)) + int(rc) + 1
                rc = 0
            else:
                tickm = int((w1 * tick1) + (w2 * tick2)) + int(rc)
                rc = 0

            noteon = midi.NoteOnEvent(tick=0, channel=0, data=[60, 70])
            tra.append(noteon)
            noteoff = midi.NoteOffEvent(tick=tickm, channel=0, data=[60, 0])
            tra.append(noteoff)

            e += 1

        else:
            e += 1

    trackend = midi.EndOfTrackEvent(tick=1)
    tra.append(trackend)
    midi.write_midifile(file_out, pat)


def west_african_triplet(morph, repeats):
    """TODO: Docstring for WestAfricanTriplet.

    Args:
        morph: TODO
        repeats: TODO

    Returns: TODO

    """

    file_out = "marathon_out.mid"

    # straight
    notes1 = [0, 480, 0, 480, 0, 480]
    # phrased
    notes2 = [0, 720, 0, 360, 0, 360]

    fm = 1
    rm = 960

    pat = midi.Pattern(format=int(fm), resolution=int(rm))
    tra = midi.Track()
    pat.append(tra)

    # pattern weight (must add up to 1.0)
    w1 = 1-float(morph)/100
    w2 = float(morph)/100

    # rounding correction
    rc = 0

    for n in range(int(repeats)):
        e = 0
        for event in notes2:
            tick1 = int(notes1[e])
            tick2 = int(notes2[e])

            # rounding correction
            rc += (w1 * tick1) + (w2 * tick2) - float(int(w1 * tick1) + (w2 * tick2))

            if rc % 1 < -0.5:
                tickm = int((w1 * tick1) + (w2 * tick2)) + int(rc) - 1
                rc = 0
            elif rc % 1 >= 0.5:
                tickm = int((w1 * tick1) + (w2 * tick2)) + int(rc) + 1
                rc = 0
            else:
                tickm = int((w1 * tick1) + (w2 * tick2)) + int(rc)
                rc = 0

            noteon = midi.NoteOnEvent(tick=0, channel=0, data=[60, 70])
            tra.append(noteon)
            noteoff = midi.NoteOffEvent(tick=tickm, channel=0, data=[60, 0])
            tra.append(noteoff)

            e += 1

        else:
            e += 1

    trackend = midi.EndOfTrackEvent(tick=1)
    tra.append(trackend)
    midi.write_midifile(file_out, pat)


def gwana_triplet(morph, repeats):
    """TODO: Docstring for GwanaTriplet.

    Args:
        morph: TODO
        repeats: TODO

    Returns: TODO

    """

    file_out = "marathon_out.mid"

    # straight
    notes1 = [0, 480, 0, 480, 0, 480]
    # phrased
    notes2 = [0, 576, 0, 288, 0, 576]

    fm = 1
    rm = 960

    pat = midi.Pattern(format=int(fm), resolution=int(rm))
    tra = midi.Track()
    pat.append(tra)

    # pattern weight (must add up to 1.0)
    w1 = 1-float(morph)/100
    w2 = float(morph)/100

    # rounding correction
    rc = 0

    for n in range(int(repeats)):
        e = 0
        for event in notes2:
            tick1 = int(notes1[e])
            tick2 = int(notes2[e])

            # rounding correction
            rc += (w1 * tick1) + (w2 * tick2) - float(int(w1 * tick1) + (w2 * tick2))

            if rc % 1 < -0.5:
                tickm = int((w1 * tick1) + (w2 * tick2)) + int(rc) - 1
                rc = 0
            elif rc % 1 >= 0.5:
                tickm = int((w1 * tick1) + (w2 * tick2)) + int(rc) + 1
                rc = 0
            else:
                tickm = int((w1 * tick1) + (w2 * tick2)) + int(rc)
                rc = 0

            noteon = midi.NoteOnEvent(tick=0, channel=0, data=[60, 70])
            tra.append(noteon)
            noteoff = midi.NoteOffEvent(tick=tickm, channel=0, data=[60, 0])
            tra.append(noteoff)

            e += 1

        else:
            e += 1

    trackend = midi.EndOfTrackEvent(tick=1)
    tra.append(trackend)
    midi.write_midifile(file_out, pat)


def brazilian_sixteens(morph, repeats):
    """TODO: Docstring for BrazilianSixteens.

    Args:
        morph: TODO
        repeats: TODO

    Returns: TODO

    """

    file_out = "marathon_out.mid"

    # straight
    notes1 = [0, 240, 0, 240, 0, 240, 0, 240]
    # phrased
    notes2 = [0, 320, 0, 160, 0, 160, 0, 320]

    fm = 1
    rm = 960

    pat = midi.Pattern(format=int(fm), resolution=int(rm))
    tra = midi.Track()
    pat.append(tra)

    # pattern weight (must add up to 1.0)
    w1 = 1-float(morph)/100
    w2 = float(morph)/100

    # rounding correction
    rc = 0

    for n in range(int(repeats)):
        e = 0
        for event in notes2:
            tick1 = int(notes1[e])
            tick2 = int(notes2[e])

            # rounding correction
            rc += (w1 * tick1) + (w2 * tick2) - float(int(w1 * tick1) + (w2 * tick2))

            if rc % 1 < -0.5:
                tickm = int((w1 * tick1) + (w2 * tick2)) + int(rc) - 1
                rc = 0
            elif rc % 1 >= 0.5:
                tickm = int((w1 * tick1) + (w2 * tick2)) + int(rc) + 1
                rc = 0
            else:
                tickm = int((w1 * tick1) + (w2 * tick2)) + int(rc)
                rc = 0

            noteon = midi.NoteOnEvent(tick=0, channel=0, data=[60, 70])
            tra.append(noteon)
            noteoff = midi.NoteOffEvent(tick=tickm, channel=0, data=[60, 0])
            tra.append(noteoff)

            e += 1

        else:
            e += 1

    trackend = midi.EndOfTrackEvent(tick=1)
    tra.append(trackend)
    midi.write_midifile(file_out, pat)


def braffs_quintuplets(morph, repeats):
    """TODO: Docstring for BraffsQuintuplets.

    Args:
        morph: TODO
        repeats: TODO

    Returns: TODO

    """

    file_out = "marathon_out.mid"

    # straight
    notes1 = [0, 192, 0, 192, 0, 192, 0, 192, 0, 192]
    # phrased
    notes2 = [0, 274, 0, 137, 0, 137, 0, 275, 0, 137]

    fm = 1
    rm = 960

    pat = midi.Pattern(format=int(fm), resolution=int(rm))
    tra = midi.Track()
    pat.append(tra)

    # pattern weight (must add up to 1.0)
    w1 = 1-float(morph)/100
    w2 = float(morph)/100

    # rounding correction
    rc = 0

    for n in range(int(repeats)):
        e = 0
        for event in notes2:
            tick1 = int(notes1[e])
            tick2 = int(notes2[e])

            # rounding correction
            rc += (w1 * tick1) + (w2 * tick2) - float(int(w1 * tick1) + (w2 * tick2))

            if rc % 1 < -0.5:
                tickm = int((w1 * tick1) + (w2 * tick2)) + int(rc) - 1
                rc = 0
            elif rc % 1 >= 0.5:
                tickm = int((w1 * tick1) + (w2 * tick2)) + int(rc) + 1
                rc = 0
            else:
                tickm = int((w1 * tick1) + (w2 * tick2)) + int(rc)
                rc = 0

            noteon = midi.NoteOnEvent(tick=0, channel=0, data=[60, 70])
            tra.append(noteon)
            noteoff = midi.NoteOffEvent(tick=tickm, channel=0, data=[60, 0])
            tra.append(noteoff)

            e += 1

        else:
            e += 1

    trackend = midi.EndOfTrackEvent(tick=1)
    tra.append(trackend)
    midi.write_midifile(file_out, pat)


def vienesse_waltz(morph, repeats):
    """TODO: Docstring for VienesseWaltz.

    Args:
        morph: TODO
        repeats: TODO

    Returns: TODO

    """

    file_out = "marathon_out.mid"

    # straight
    notes1 = [0, 960, 0, 960, 0, 960]
    # phrased
    notes2 = [0, 720, 0, 1200, 0, 960]

    fm = 1
    rm = 960

    pat = midi.Pattern(format=int(fm), resolution=int(rm))
    tra = midi.Track()
    pat.append(tra)

    # pattern weight (must add up to 1.0)
    w1 = 1-float(morph)/100
    w2 = float(morph)/100

    # rounding correction
    rc = 0

    for n in range(int(repeats)):
        e = 0
        for event in notes2:
            tick1 = int(notes1[e])
            tick2 = int(notes2[e])

            # rounding correction
            rc += (w1 * tick1) + (w2 * tick2) - float(int(w1 * tick1) + (w2 * tick2))

            if rc % 1 < -0.5:
                tickm = int((w1 * tick1) + (w2 * tick2)) + int(rc) - 1
                rc = 0
            elif rc % 1 >= 0.5:
                tickm = int((w1 * tick1) + (w2 * tick2)) + int(rc) + 1
                rc = 0
            else:
                tickm = int((w1 * tick1) + (w2 * tick2)) + int(rc)
                rc = 0

            noteon = midi.NoteOnEvent(tick=0, channel=0, data=[60, 70])
            tra.append(noteon)
            noteoff = midi.NoteOffEvent(tick=tickm, channel=0, data=[60, 0])
            tra.append(noteoff)

            e += 1

        else:
            e += 1

    trackend = midi.EndOfTrackEvent(tick=1)
    tra.append(trackend)
    midi.write_midifile(file_out, pat)


def text_command(morph, repeats, comm1, comm2):
    """TODO: Docstring for textCommand.

    :arg1: TODO
    :returns: TODO

    """

    file_out = "marathon_out.mid"

    note_length = {
        "w": 3840,
        "h": 1920,
        "q": 960,
        "e": 480,
        "s": 240,
        "t": 120
    }

    note_list1 = str(comm1).replace("-", " ").split(" ")
    note_list2 = str(comm2).replace("-", " ").split(" ")

    notes1 = []
    notes2 = []

    # notes
    for note in note_list1:
        notes1.append(int(0))
        notes1.append(int(note_length[str(note)[0]]))
    for note in note_list2:
        notes2.append(int(0))
        notes2.append(int(note_length[str(note)[0]]))

    # dots
    pos = 1
    for note in note_list1:
        if len(str(note)) == 2:
            if str(note)[1] == ".":
                notes1[pos*2-1] += int(notes1[pos*2-1]/2)
        if len(str(note)) == 3:
            if str(note)[2] == ".":
                notes1[pos*2-1] += int(notes1[pos*2-1]/2)
                notes1[pos*2-1] += int(notes1[pos*2-1]/6)
        if len(str(note)) == 4:
            if str(note)[3] == ".":
                notes1[pos*2-1] += int(notes1[pos*2-1]/2)
                notes1[pos*2-1] += int(notes1[pos*2-1]/6)
                notes1[pos*2-1] += int(notes1[pos*2-1]/14)
        pos += 1
    pos = 1
    for note in note_list2:
        if len(str(note)) == 2:
            if str(note)[1] == ".":
                notes2[pos*2-1] += int(notes2[pos*2-1]/2)
        if len(str(note)) == 3:
            if str(note)[2] == ".":
                notes2[pos*2-1] += int(notes2[pos*2-1]/2)
                notes2[pos*2-1] += int(notes2[pos*2-1]/6)
        if len(str(note)) == 4:
            if str(note)[3] == ".":
                notes2[pos*2-1] += int(notes2[pos*2-1]/2)
                notes2[pos*2-1] += int(notes2[pos*2-1]/6)
                notes2[pos*2-1] += int(notes2[pos*2-1]/14)
        pos += 1

    # tuplets
    pos = 1
    for note in note_list1:
        if "/" in str(note):
            tuplet_start = str(note).count(".")+1
            nom = int(str(note)[tuplet_start:len(note)].split("/")[0])
            denom = int(str(note)[tuplet_start:len(note)].split("/")[1])
            notes1[pos*2-1] = int(notes1[pos*2-1]*(denom/nom))
        pos += 1
    pos = 1
    for note in note_list2:
        if "/" in str(note):
            tuplet_start = str(note).count(".")+1
            nom = int(str(note)[tuplet_start:len(note)].split("/")[0])
            denom = int(str(note)[tuplet_start:len(note)].split("/")[1])
            notes2[pos*2-1] = int(notes2[pos*2-1]*(denom/nom))
        pos += 1

    notes1_f = []
    notes2_f = []

    # tying notes
    pos = 1
    for note in str(comm1).split(" "):
        notes1_f.append(0)
        ties = 0
        if "-" in str(note):
            ties += int(str(note).count("-"))
        tied_value = notes1[pos*2-1]
        for n in range(ties):
            tied_value += int(notes1[pos*2+1])
            pos += 1
        notes1_f.append(tied_value)
        pos += 1
    pos = 0
    for note in str(comm2).split(" "):
        notes2_f.append(0)
        ties = 0
        if "-" in str(note):
            ties += int(str(note).count("-"))
        tied_value = notes2[pos*2-1]
        for n in range(ties):
            tied_value += int(notes2[pos*2+1])
            pos += 1
        notes2_f.append(tied_value)
        pos += 1

    # length equalization
    T1 = 0
    for note in notes1_f:
        T1 += int(note)
    T2 = 0
    for note in notes2_f:
        T2 += int(note)
    ratio = T1/T2
    pos = 0
    for note in notes2_f:
        notes2_f[pos] = int(note*ratio)
        pos += 1

    fm = 1
    rm = 960

    pat = midi.Pattern(format=int(fm), resolution=int(rm))
    tra = midi.Track()
    pat.append(tra)

    # pattern weight (must add up to 1.0)
    w1 = 1-float(morph)/100
    w2 = float(morph)/100

    # rounding correction
    rc = 0

    for n in range(int(repeats)):
        e = 0
        for event in notes2:
            tick1 = int(notes1_f[e])
            tick2 = int(notes2_f[e])

            # rounding correction
            rc += (w1 * tick1) + (w2 * tick2) - float(int(w1 * tick1) + (w2 * tick2))

            if rc % 1 < -0.5:
                tickm = int((w1 * tick1) + (w2 * tick2)) + int(rc) - 1
                rc = 0
            elif rc % 1 >= 0.5:
                tickm = int((w1 * tick1) + (w2 * tick2)) + int(rc) + 1
                rc = 0
            else:
                tickm = int((w1 * tick1) + (w2 * tick2)) + int(rc)
                rc = 0

            noteon = midi.NoteOnEvent(tick=0, channel=0, data=[60, 70])
            tra.append(noteon)
            noteoff = midi.NoteOffEvent(tick=tickm, channel=0, data=[60, 0])
            tra.append(noteoff)

            e += 1

        else:
            e += 1

    trackend = midi.EndOfTrackEvent(tick=1)
    tra.append(trackend)
    midi.write_midifile(file_out, pat)


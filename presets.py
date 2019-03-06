# -*- coding: utf-8 -*-

"""Presets for marathon."""

import midi


def swing(morph1, morph2, repeats):
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

    # length equalization
    T1 = 0
    for note in notes1:
        T1 += int(note)
    T2 = 0
    for note in notes2:
        T2 += int(note)
    ratio = T1/T2
    pos = 0
    for note in notes2:
        notes2[pos] = int(note*ratio)
        pos += 1

    totaltick = T1 * int(repeats)

    # rounding correction
    rc = 0

    ws = float(morph1)
    we = float(morph2)
    currenttick = 0

    notes_f = []

    for n in range(int(repeats)):
        e = 0
        for event in notes2:
            tick1 = int(notes1[e])
            tick2 = int(notes2[e])

            progress = currenttick / totaltick

            if ws != we:
                w1 = (1 - progress) * (we/100) + progress * (ws/100)
                w2 = progress * (we/100) + (1 - progress) * (ws/100)
            else:
                w1 = 1-float(float(morph1)/100)
                w2 = float(float(morph1)/100)

            # rounding correction
            rc += (w1 * tick1) + (w2 * tick2) - float(int((w1 * tick1) + (w2 * tick2)))
            if rc % 1 >= 0.5:
                tickm = int((w1 * tick1) + (w2 * tick2)) + int(rc) + 1
                rc = 0
            else:
                tickm = int((w1 * tick1) + (w2 * tick2)) + int(rc)
                rc = 0

            notes_f.append(int(tickm))
            currenttick += tickm

            e += 1

    Tm = 0

    for note in notes_f:
        Tm += int(note)

    cf = (T1*int(repeats))/Tm

    for note in notes_f:
        note = int(note*cf)

    delta_t = Tm - T1*int(repeats)

    if delta_t > 0:
        i = 1
        for n in range(abs(delta_t)):
            if i >= len(notes_f):
                i = 1
            notes_f[i] -= 1
            i += 2
    if delta_t < 0:
        i = 1
        for n in range(abs(delta_t)):
            if i >= len(notes_f):
                i = 1
            notes_f[i] += 1
            i += 1

    f = 0

    for note in notes_f:
        tickm = int(note)
        noteon = midi.NoteOnEvent(tick=0, channel=0, data=[60, 70])
        tra.append(noteon)
        noteoff = midi.NoteOffEvent(tick=tickm, channel=0, data=[60, 0])
        tra.append(noteoff)
        f += tickm

    trackend = midi.EndOfTrackEvent(tick=1)
    tra.append(trackend)
    midi.write_midifile(file_out, pat)


def half_swing(morph1, morph2, repeats):
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

    # length equalization
    T1 = 0
    for note in notes1:
        T1 += int(note)
    T2 = 0
    for note in notes2:
        T2 += int(note)
    ratio = T1/T2
    pos = 0
    for note in notes2:
        notes2[pos] = int(note*ratio)
        pos += 1

    totaltick = T1 * int(repeats)

    # rounding correction
    rc = 0

    ws = float(morph1)
    we = float(morph2)
    currenttick = 0

    notes_f = []

    for n in range(int(repeats)):
        e = 0
        for event in notes2:
            tick1 = int(notes1[e])
            tick2 = int(notes2[e])

            progress = currenttick / totaltick

            if ws != we:
                w1 = (1 - progress) * (we/100) + progress * (ws/100)
                w2 = progress * (we/100) + (1 - progress) * (ws/100)
            else:
                w1 = 1-float(float(morph1)/100)
                w2 = float(float(morph1)/100)

            # rounding correction
            rc += (w1 * tick1) + (w2 * tick2) - float(int((w1 * tick1) + (w2 * tick2)))

            if rc % 1 >= 0.5:
                tickm = int((w1 * tick1) + (w2 * tick2)) + int(rc) + 1
                rc = 0
            else:
                tickm = int((w1 * tick1) + (w2 * tick2)) + int(rc)
                rc = 0

            notes_f.append(int(tickm))
            currenttick += tickm

            e += 1

    Tm = 0

    for note in notes_f:
        Tm += int(note)

    cf = (T1*int(repeats))/Tm

    for note in notes_f:
        note = int(note*cf)
    
    Tm = 0
    
    for note in notes_f:
        Tm += int(note)

    delta_t = Tm - T1*int(repeats)

    if delta_t > 0:
        i = 1
        for n in range(abs(delta_t)):
            if i >= len(notes_f):
                i = 1
            notes_f[i] -= 1
            i += 2
    if delta_t < 0:
        i = 1
        for n in range(abs(delta_t)):
            if i >= len(notes_f):
                i = 1
            notes_f[i] += 1
            i += 1
            
    Tm = 0
    
    for note in notes_f:
        Tm += int(note)

    f = 0

    for note in notes_f:
        tickm = int(note)
        noteon = midi.NoteOnEvent(tick=0, channel=0, data=[60, 70])
        tra.append(noteon)
        noteoff = midi.NoteOffEvent(tick=tickm, channel=0, data=[60, 0])
        tra.append(noteoff)
        f += tickm

    trackend = midi.EndOfTrackEvent(tick=1)
    tra.append(trackend)
    midi.write_midifile(file_out, pat)


def west_african_triplet(morph1, morph2, repeats):
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

    # length equalization
    T1 = 0
    for note in notes1:
        T1 += int(note)
    T2 = 0
    for note in notes2:
        T2 += int(note)
    ratio = T1/T2
    pos = 0
    for note in notes2:
        notes2[pos] = int(note*ratio)
        pos += 1

    totaltick = T1 * int(repeats)

    # rounding correction
    rc = 0

    ws = float(morph1)
    we = float(morph2)
    currenttick = 0

    notes_f = []

    for n in range(int(repeats)):
        e = 0
        for event in notes2:
            tick1 = int(notes1[e])
            tick2 = int(notes2[e])

            progress = currenttick / totaltick

            if ws != we:
                w1 = (1 - progress) * (we/100) + progress * (ws/100)
                w2 = progress * (we/100) + (1 - progress) * (ws/100)
            else:
                w1 = 1-float(float(morph1)/100)
                w2 = float(float(morph1)/100)

            # rounding correction
            rc += (w1 * tick1) + (w2 * tick2) - float(int((w1 * tick1) + (w2 * tick2)))

            if rc % 1 >= 0.5:
                tickm = int((w1 * tick1) + (w2 * tick2)) + int(rc) + 1
                rc = 0
            else:
                tickm = int((w1 * tick1) + (w2 * tick2)) + int(rc)
                rc = 0

            notes_f.append(int(tickm))
            currenttick += tickm

            e += 1

    Tm = 0

    for note in notes_f:
        Tm += int(note)

    cf = (T1*int(repeats))/Tm

    for note in notes_f:
        note = int(note*cf)

    delta_t = Tm - T1*int(repeats)

    if delta_t > 0:
        i = 1
        for n in range(abs(delta_t)):
            if i >= len(notes_f):
                i = 1
            notes_f[i] -= 1
            i += 2
    if delta_t < 0:
        i = 1
        for n in range(abs(delta_t)):
            if i >= len(notes_f):
                i = 1
            notes_f[i] += 1
            i += 1

    Tm = 0
    for note in notes_f:
        Tm += int(note)
    f = 0

    for note in notes_f:
        tickm = int(note)
        noteon = midi.NoteOnEvent(tick=0, channel=0, data=[60, 70])
        tra.append(noteon)
        noteoff = midi.NoteOffEvent(tick=tickm, channel=0, data=[60, 0])
        tra.append(noteoff)
        f += tickm

    trackend = midi.EndOfTrackEvent(tick=1)
    tra.append(trackend)
    midi.write_midifile(file_out, pat)


def gwana_triplet(morph1, morph2, repeats):
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

    # length equalization
    T1 = 0
    for note in notes1:
        T1 += int(note)
    T2 = 0
    for note in notes2:
        T2 += int(note)
    ratio = T1/T2
    pos = 0
    for note in notes2:
        notes2[pos] = int(note*ratio)
        pos += 1

    totaltick = T1 * int(repeats)

    # rounding correction
    rc = 0

    ws = float(morph1)
    we = float(morph2)
    currenttick = 0

    notes_f = []

    for n in range(int(repeats)):
        e = 0
        for event in notes2:
            tick1 = int(notes1[e])
            tick2 = int(notes2[e])

            progress = currenttick / totaltick

            if ws != we:
                w1 = (1 - progress) * (we/100) + progress * (ws/100)
                w2 = progress * (we/100) + (1 - progress) * (ws/100)
            else:
                w1 = 1-float(float(morph1)/100)
                w2 = float(float(morph1)/100)

            # rounding correction
            rc += (w1 * tick1) + (w2 * tick2) - float(int((w1 * tick1) + (w2 * tick2)))

            if rc % 1 >= 0.5:
                tickm = int((w1 * tick1) + (w2 * tick2)) + int(rc) + 1
                rc = 0
            else:
                tickm = int((w1 * tick1) + (w2 * tick2)) + int(rc)
                rc = 0

            notes_f.append(int(tickm))
            currenttick += tickm

            e += 1

    Tm = 0

    for note in notes_f:
        Tm += int(note)

    cf = (T1*int(repeats))/Tm

    for note in notes_f:
        note = int(note*cf)

    delta_t = Tm - T1*int(repeats)

    if delta_t > 0:
        i = 1
        for n in range(abs(delta_t)):
            if i >= len(notes_f):
                i = 1
            notes_f[i] -= 1
            i += 2
    if delta_t < 0:
        i = 1
        for n in range(abs(delta_t)):
            if i >= len(notes_f):
                i = 1
            notes_f[i] += 1
            i += 1

    Tm = 0
    for note in notes_f:
        Tm += int(note)
    f = 0

    for note in notes_f:
        tickm = int(note)
        noteon = midi.NoteOnEvent(tick=0, channel=0, data=[60, 70])
        tra.append(noteon)
        noteoff = midi.NoteOffEvent(tick=tickm, channel=0, data=[60, 0])
        tra.append(noteoff)
        f += tickm

    trackend = midi.EndOfTrackEvent(tick=1)
    tra.append(trackend)
    midi.write_midifile(file_out, pat)


def brazilian_sixteens(morph1, morph2, repeats):
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

    # length equalization
    T1 = 0
    for note in notes1:
        T1 += int(note)
    T2 = 0
    for note in notes2:
        T2 += int(note)
    ratio = T1/T2
    pos = 0
    for note in notes2:
        notes2[pos] = int(note*ratio)
        pos += 1

    totaltick = T1 * int(repeats)

    # rounding correction
    rc = 0

    ws = float(morph1)
    we = float(morph2)
    currenttick = 0

    notes_f = []

    for n in range(int(repeats)):
        e = 0
        for event in notes2:
            tick1 = int(notes1[e])
            tick2 = int(notes2[e])

            progress = currenttick / totaltick

            if ws != we:
                w1 = (1 - progress) * (we/100) + progress * (ws/100)
                w2 = progress * (we/100) + (1 - progress) * (ws/100)
            else:
                w1 = 1-float(float(morph1)/100)
                w2 = float(float(morph1)/100)

            # rounding correction
            rc += (w1 * tick1) + (w2 * tick2) - float(int((w1 * tick1) + (w2 * tick2)))

            if rc % 1 >= 0.5:
                tickm = int((w1 * tick1) + (w2 * tick2)) + int(rc) + 1
                rc = 0
            else:
                tickm = int((w1 * tick1) + (w2 * tick2)) + int(rc)
                rc = 0

            notes_f.append(int(tickm))
            currenttick += tickm

            e += 1

    Tm = 0

    for note in notes_f:
        Tm += int(note)

    cf = (T1*int(repeats))/Tm

    for note in notes_f:
        note = int(note*cf)

    delta_t = Tm - T1*int(repeats)

    if delta_t > 0:
        i = 1
        for n in range(abs(delta_t)):
            if i >= len(notes_f):
                i = 1
            notes_f[i] -= 1
            i += 2
    if delta_t < 0:
        i = 1
        for n in range(abs(delta_t)):
            if i >= len(notes_f):
                i = 1
            notes_f[i] += 1
            i += 1

    Tm = 0
    for note in notes_f:
        Tm += int(note)
    f = 0

    for note in notes_f:
        tickm = int(note)
        noteon = midi.NoteOnEvent(tick=0, channel=0, data=[60, 70])
        tra.append(noteon)
        noteoff = midi.NoteOffEvent(tick=tickm, channel=0, data=[60, 0])
        tra.append(noteoff)
        f += tickm

    trackend = midi.EndOfTrackEvent(tick=1)
    tra.append(trackend)
    midi.write_midifile(file_out, pat)


def braffs_quintuplets(morph1, morph2, repeats):
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

    # length equalization
    T1 = 0
    for note in notes1:
        T1 += int(note)
    T2 = 0
    for note in notes2:
        T2 += int(note)
    ratio = T1/T2
    pos = 0
    for note in notes2:
        notes2[pos] = int(note*ratio)
        pos += 1

    totaltick = T1 * int(repeats)

    # rounding correction
    rc = 0

    ws = float(morph1)
    we = float(morph2)
    currenttick = 0

    notes_f = []

    for n in range(int(repeats)):
        e = 0
        for event in notes2:
            tick1 = int(notes1[e])
            tick2 = int(notes2[e])

            progress = currenttick / totaltick

            if ws != we:
                w1 = (1 - progress) * (we/100) + progress * (ws/100)
                w2 = progress * (we/100) + (1 - progress) * (ws/100)
            else:
                w1 = 1-float(float(morph1)/100)
                w2 = float(float(morph1)/100)

            # rounding correction
            rc += (w1 * tick1) + (w2 * tick2) - float(int((w1 * tick1) + (w2 * tick2)))

            if rc % 1 >= 0.5:
                tickm = int((w1 * tick1) + (w2 * tick2)) + int(rc) + 1
                rc = 0
            else:
                tickm = int((w1 * tick1) + (w2 * tick2)) + int(rc)
                rc = 0

            notes_f.append(int(tickm))
            currenttick += tickm

            e += 1

    Tm = 0

    for note in notes_f:
        Tm += int(note)

    cf = (T1*int(repeats))/Tm

    for note in notes_f:
        note = int(note*cf)

    delta_t = Tm - T1*int(repeats)

    if delta_t > 0:
        i = 1
        for n in range(abs(delta_t)):
            if i >= len(notes_f):
                i = 1
            notes_f[i] -= 1
            i += 2
    if delta_t < 0:
        i = 1
        for n in range(abs(delta_t)):
            if i >= len(notes_f):
                i = 1
            notes_f[i] += 1
            i += 1

    Tm = 0
    for note in notes_f:
        Tm += int(note)
    f = 0

    for note in notes_f:
        tickm = int(note)
        noteon = midi.NoteOnEvent(tick=0, channel=0, data=[60, 70])
        tra.append(noteon)
        noteoff = midi.NoteOffEvent(tick=tickm, channel=0, data=[60, 0])
        tra.append(noteoff)
        f += tickm

    trackend = midi.EndOfTrackEvent(tick=1)
    tra.append(trackend)
    midi.write_midifile(file_out, pat)


def vienesse_waltz(morph1, morph2, repeats):
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

    # length equalization
    T1 = 0
    for note in notes1:
        T1 += int(note)
    T2 = 0
    for note in notes2:
        T2 += int(note)
    ratio = T1/T2
    pos = 0
    for note in notes2:
        notes2[pos] = int(note*ratio)
        pos += 1

    totaltick = T1 * int(repeats)

    # rounding correction
    rc = 0

    ws = float(morph1)
    we = float(morph2)
    currenttick = 0

    notes_f = []

    for n in range(int(repeats)):
        e = 0
        for event in notes2:
            tick1 = int(notes1[e])
            tick2 = int(notes2[e])

            progress = currenttick / totaltick

            if ws != we:
                w1 = (1 - progress) * (we/100) + progress * (ws/100)
                w2 = progress * (we/100) + (1 - progress) * (ws/100)
            else:
                w1 = 1-float(float(morph1)/100)
                w2 = float(float(morph1)/100)

            # rounding correction
            rc += (w1 * tick1) + (w2 * tick2) - float(int((w1 * tick1) + (w2 * tick2)))

            if rc % 1 >= 0.5:
                tickm = int((w1 * tick1) + (w2 * tick2)) + int(rc) + 1
                rc = 0
            else:
                tickm = int((w1 * tick1) + (w2 * tick2)) + int(rc)
                rc = 0

            notes_f.append(int(tickm))
            currenttick += tickm

            e += 1

    Tm = 0

    for note in notes_f:
        Tm += int(note)

    cf = (T1*int(repeats))/Tm

    for note in notes_f:
        note = int(note*cf)

    delta_t = Tm - T1*int(repeats)

    if delta_t > 0:
        i = 1
        for n in range(abs(delta_t)):
            if i >= len(notes_f):
                i = 1
            notes_f[i] -= 1
            i += 2
    if delta_t < 0:
        i = 1
        for n in range(abs(delta_t)):
            if i >= len(notes_f):
                i = 1
            notes_f[i] += 1
            i += 1

    Tm = 0
    for note in notes_f:
        Tm += int(note)
    f = 0

    for note in notes_f:
        tickm = int(note)
        noteon = midi.NoteOnEvent(tick=0, channel=0, data=[60, 70])
        tra.append(noteon)
        noteoff = midi.NoteOffEvent(tick=tickm, channel=0, data=[60, 0])
        tra.append(noteoff)
        f += tickm

    trackend = midi.EndOfTrackEvent(tick=1)
    tra.append(trackend)
    midi.write_midifile(file_out, pat)


def text_command(morph1, morph2, repeats, comm1, comm2):
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
    
    new_comm1 = str(comm1).split(" ")
    new_comm2 = str(comm2).split(" ")
    
    comm1 = ""
    comm2 = ""
        
    for comm in new_comm1:
        if "(" in str(comm):
            num = int(comm.split("(")[0])
            note = comm.split("(")[1].split(")")[0]
            for n in range(num):
                if comm1 == "":
                    comm1 += str(note)
                else:
                    comm1 += " "+str(note)
        else:
            if comm1 == "":
                comm1 += str(comm)
            else:
                comm1 += " "+str(comm)
            
    for comm in new_comm2:
        if "(" in str(comm):
            num = int(comm.split("(")[0])
            note = comm.split("(")[1].split(")")[0]
            for n in range(num):
                if comm2 == "":
                    comm2 += str(note)
                else:
                    comm2 += " "+str(note)
        else:
            if comm2 == "":
                comm2 += str(comm)
            else:
                comm2 += " "+str(comm)
            
    if len(comm1.split(" ")) != len(comm2.split(" ")):
        print("Error: The two commands must be of similar length\n\nTrack 1: "+str(comm1)+"\n\nTrack 2: "+str(comm2))
        raise SystemExit

    note_list1 = []
    note_list2 = []
    
    for note in comm1.split(" "):
        note_list1.append(str(note))
    for note in comm2.split(" "):
        note_list2.append(str(note))

    notes1 = []
    notes2 = []
    
    #notes
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
            tuplet_start = 0
            for char in str(note).split("/")[0]:
                if char.isalpha() == True or char == ".":
                    tuplet_start += 1
                else:
                    break
            nom = int(str(note)[tuplet_start:len(note)].split("/")[0])
            tuplet_end = 0
            for char in str(note).split("/")[1]:
                if char.isalpha() == False and char != "-":
                    tuplet_end += 1
                else:
                    break
            denom = int(str(note).split("/")[1][0:tuplet_end])
            notes1[pos*2-1] = int(notes1[pos*2-1]*(denom/nom))
        pos += 1
    pos = 1
    for note in note_list2:
        if "/" in str(note):
            tuplet_start = 0
            for char in str(note).split("/")[0]:
                if char.isalpha() == True or char == ".":
                    tuplet_start += 1
                else:
                    break
            nom = int(str(note)[tuplet_start:len(note)].split("/")[0])
            tuplet_end = 0
            for char in str(note).split("/")[1]:
                if char.isalpha() == False and char != "-":
                    tuplet_end += 1
                else:
                    break
            denom = int(str(note).split("/")[1][0:tuplet_end])
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
        posi = 0
        for n in range(ties-1):
            tied_value += int(notes1[posi*2+1])
            posi += 1
        notes1_f.append(tied_value)
        pos += 1
    pos = 1
    for note in str(comm2).split(" "):
        notes2_f.append(0)
        ties = 0
        if "-" in str(note):
            ties += int(str(note).count("-"))
        tied_value = notes2[pos*2-1]
        posi = 0
        for n in range(ties-1):
            tied_value += int(notes2[posi*2+1])
            posi += 1
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

    totaltick = T1 * int(repeats)

    fm = 1
    rm = 960

    pat = midi.Pattern(format=int(fm), resolution=int(rm))
    tra = midi.Track()
    pat.append(tra)

    # rounding correction
    rc = 0

    ws = float(morph1)
    we = float(morph2)
    currenttick = 0

    notes_f = []

    for n in range(int(repeats)):
        e = 0
        for event in notes2_f:
            tick1 = int(notes1_f[e])
            tick2 = int(notes2_f[e])

            progress = currenttick / totaltick
            if ws != we:
                w1 = (1 - progress) * (we/100) + progress * (ws/100)
                w2 = progress * (we/100) + (1 - progress) * (ws/100)
            else:
                w1 = 1-float(float(morph1)/100)
                w2 = float(float(morph1)/100)

            # rounding correction
            rc += (w1 * tick1) + (w2 * tick2) - float(int((w1 * tick1) + (w2 * tick2)))

            if rc % 1 >= 0.5:
                tickm = int((w1 * tick1) + (w2 * tick2)) + int(rc) + 1
                rc = 0
            else:
                tickm = int((w1 * tick1) + (w2 * tick2)) + int(rc)
                rc = 0

            notes_f.append(int(tickm))

            currenttick += tickm

            e += 1

    Tm = 0

    for note in notes_f:
        Tm += int(note)

    cf = (T1*int(repeats))/Tm

    for note in notes_f:
        note = int(note*cf)

    delta_t = Tm - T1*int(repeats)

    if delta_t > 0:
        i = 1
        for n in range(abs(delta_t)):
            if i >= len(notes_f):
                i = 1
            notes_f[i] -= 1
            i += 2
    if delta_t < 0:
        i = 1
        for n in range(abs(delta_t)):
            if i >= len(notes_f):
                i = 1
            notes_f[i] += 1
            i += 1

    Tm = 0
    for note in notes_f:
        Tm += int(note)

    f = 0
    e = 0
    for note in notes_f:
        tickm = int(note)
        if "r" in str(comm1).split(" ")[e//2] or "r" in str(comm2).split(" ")[e//2]:
            noteon = midi.NoteOnEvent(tick=0, channel=0, data=[0, 1])
            tra.append(noteon)
            noteoff = midi.NoteOffEvent(tick=tickm, channel=0, data=[0, 0])
            tra.append(noteoff)
        else:
            noteon = midi.NoteOnEvent(tick=0, channel=0, data=[60, 70])
            tra.append(noteon)
            noteoff = midi.NoteOffEvent(tick=tickm, channel=0, data=[60, 0])
            tra.append(noteoff)
        e += 1
        if e == len(str(comm1).split(" ")):
            e = 0
        f += tickm

    trackend = midi.EndOfTrackEvent(tick=1)
    tra.append(trackend)
    midi.write_midifile(file_out, pat)


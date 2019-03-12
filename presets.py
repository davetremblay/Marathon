# -*- coding: utf-8 -*-

"""Presets for marathon."""

import midi
import time

file_out = "marathon_out"+str(time.strftime('%Y-%m-%d-%Hh%Mm%Ss'))+".mid"

format_out = 1
res_out = 960
tick_rest = 0

pat = midi.Pattern(format=int(format_out), resolution=int(res_out))
tra = midi.Track()
pat.append(tra)

def length_equalization(notes,repeats):
    """TODO: Docstring for Swing.

    Args:
        morph: TODO
        repeats: TODO

    Returns: TODO

    """

    total = 0
    for note in notes:
        total += int(note)
        
    return total
        
def total_tick(notes2,total_1,total_2,repeats):
    """TODO: Docstring for Swing.

    Args:
        morph: TODO
        repeats: TODO

    Returns: TODO

    """

    ratio = total_1 / total_2
    
    pos = 0
    for note in notes2:
        notes2[pos] = int(note*ratio)
        pos += 1

    totaltick = total_1 * int(repeats)
    
    return totaltick

def rounding_correction(notes1,notes2,morph1,morph2,repeats,totaltick):
    """TODO: Docstring for Swing.

    Args:
        morph: TODO
        repeats: TODO

    Returns: TODO

    """

    correction = 0

    weight_start = float(morph1)
    weight_end = float(morph2)
    
    currenttick = 0

    notes_final = []

    for n in range(int(repeats)):
        e = 0
        for event in notes2:
            tick1 = int(notes1[e])
            tick2 = int(notes2[e])

            progress = currenttick / totaltick

            if weight_start != weight_end:
                weight_1 = (1 - progress) * (weight_end/100) + progress * (weight_start/100)
                weight_2 = progress * (weight_end/100) + (1 - progress) * (weight_start/100)
            else:
                weight_1 = 1-float(float(morph1)/100)
                weight_2 = float(float(morph1)/100)

            # rounding correction
            correction += (weight_1 * tick1) + (weight_2 * tick2) - float(int((weight_1 * tick1) + (weight_2 * tick2)))
            if correction % 1 >= 0.5:
                tick_morphed = int((weight_1 * tick1) + (weight_2 * tick2)) + int(correction) + 1
                correction = 0
            else:
                tick_morphed = int((weight_1 * tick1) + (weight_2 * tick2)) + int(correction)
                correction = 0

            notes_final.append(int(tick_morphed))
            
            currenttick += tick_morphed

            e += 1
            
    return notes_final

def finalizing(notes_final,total_1,total_2,repeats):
    """TODO: Docstring for Swing.

    Args:
        morph: TODO
        repeats: TODO

    Returns: TODO

    """

    total_morphed = 0

    for note in notes_final:
        total_morphed += int(note)

    correction_factor = (total_1*int(repeats))/total_morphed

    for note in notes_final:
        note = int(note*correction_factor)

    delta_t = total_morphed - total_1*int(repeats)

    if delta_t > 0:
        i = 1
        for n in range(abs(delta_t)):
            if i >= len(notes_final):
                i = 1
            notes_final[i] -= 1
            i += 2
    if delta_t < 0:
        i = 1
        for n in range(abs(delta_t)):
            if i >= len(notes_final):
                i = 1
            notes_final[i] += 1
            i += 1

    for note in notes_final:
        tick_morphed = int(note)
        noteon = midi.NoteOnEvent(tick=tick_rest, channel=0, data=[60, 70])
        tra.append(noteon)
        noteoff = midi.NoteOffEvent(tick=tick_morphed, channel=0, data=[60, 0])
        tra.append(noteoff)

    trackend = midi.EndOfTrackEvent(tick=1)
    tra.append(trackend)
    midi.write_midifile(file_out, pat)

def swing(morph1, morph2, repeats):
    """TODO: Docstring for Swing.

    Args:
        morph: TODO
        repeats: TODO

    Returns: TODO

    """

    # straight
    notes1 = [0, 960, 0, 960]
    # phrased
    notes2 = [0, 1440, 0, 480]

    # length equalization
    total_1 = length_equalization(notes1,repeats)
    total_2 = length_equalization(notes2,repeats)
    totaltick = total_tick(notes2,total_1,total_2,repeats)

    # rounding correction
    notes_final = rounding_correction(notes1,notes2,morph1,morph2,repeats,totaltick)

    # finalizing
    finalizing(notes_final,total_1,total_2,repeats)
    
def half_swing(morph1, morph2, repeats):
    """TODO: Docstring for HalfSwing.

    Args:
        morph: TODO
        repeats: TODO

    Returns: TODO

    """
    
    # straight
    notes1 = [0, 1920, 0, 960, 0, 960]
    # phrased
    notes2 = [0, 1920, 0, 1440, 0, 480]

    # length equalization
    total_1 = length_equalization(notes1,repeats)
    total_2 = length_equalization(notes2,repeats)
    totaltick = total_tick(notes2,total_1,total_2,repeats)

    # rounding correction
    notes_final = rounding_correction(notes1,notes2,morph1,morph2,repeats,totaltick)

    # finalizing
    finalizing(notes_final,total_1,total_2,repeats)

def hard_swing(morph1, morph2, repeats):
    """TODO: Docstring for Swing.

    Args:
        morph: TODO
        repeats: TODO

    Returns: TODO

    """
    
    # straight
    notes1 = [0, 960, 0, 960]
    # phrased
    notes2 = [0, 1800, 0, 120]

    # length equalization
    total_1 = length_equalization(notes1,repeats)
    total_2 = length_equalization(notes2,repeats)
    totaltick = total_tick(notes2,total_1,total_2,repeats)

    # rounding correction
    notes_final = rounding_correction(notes1,notes2,morph1,morph2,repeats,totaltick)

    # finalizing
    finalizing(notes_final,total_1,total_2,repeats)

def half_hard_swing(morph1, morph2, repeats):
    """TODO: Docstring for HalfSwing.

    Args:
        morph: TODO
        repeats: TODO

    Returns: TODO

    """

    # straight
    notes1 = [0, 1920, 0, 960, 0, 960]
    # phrased
    notes2 = [0, 1920, 0, 1800, 0, 120]

    # length equalization
    total_1 = length_equalization(notes1,repeats)
    total_2 = length_equalization(notes2,repeats)
    totaltick = total_tick(notes2,total_1,total_2,repeats)

    # rounding correction
    notes_final = rounding_correction(notes1,notes2,morph1,morph2,repeats,totaltick)

    # finalizing
    finalizing(notes_final,total_1,total_2,repeats)

def west_african_triplet(morph1, morph2, repeats):
    """TODO: Docstring for WestAfricanTriplet.

    Args:
        morph: TODO
        repeats: TODO

    Returns: TODO

    """

    # straight
    notes1 = [0, 480, 0, 480, 0, 480]
    # phrased
    notes2 = [0, 720, 0, 360, 0, 360]

    # length equalization
    total_1 = length_equalization(notes1,repeats)
    total_2 = length_equalization(notes2,repeats)
    totaltick = total_tick(notes2,total_1,total_2,repeats)

    # rounding correction
    notes_final = rounding_correction(notes1,notes2,morph1,morph2,repeats,totaltick)

    # finalizing
    finalizing(notes_final,total_1,total_2,repeats)

def gwana_triplet(morph1, morph2, repeats):
    """TODO: Docstring for GwanaTriplet.

    Args:
        morph: TODO
        repeats: TODO

    Returns: TODO

    """

    # straight
    notes1 = [0, 480, 0, 480, 0, 480]
    # phrased
    notes2 = [0, 576, 0, 288, 0, 576]

    # length equalization
    total_1 = length_equalization(notes1,repeats)
    total_2 = length_equalization(notes2,repeats)
    totaltick = total_tick(notes2,total_1,total_2,repeats)

    # rounding correction
    notes_final = rounding_correction(notes1,notes2,morph1,morph2,repeats,totaltick)

    # finalizing
    finalizing(notes_final,total_1,total_2,repeats)

def brazilian_sixteens(morph1, morph2, repeats):
    """TODO: Docstring for BrazilianSixteens.

    Args:
        morph: TODO
        repeats: TODO

    Returns: TODO

    """

    # straight
    notes1 = [0, 240, 0, 240, 0, 240, 0, 240]
    # phrased
    notes2 = [0, 320, 0, 160, 0, 160, 0, 320]

    # length equalization
    total_1 = length_equalization(notes1,repeats)
    total_2 = length_equalization(notes2,repeats)
    totaltick = total_tick(notes2,total_1,total_2,repeats)

    # rounding correction
    notes_final = rounding_correction(notes1,notes2,morph1,morph2,repeats,totaltick)

    # finalizing
    finalizing(notes_final,total_1,total_2,repeats)

def braffs_quintuplets(morph1, morph2, repeats):
    """TODO: Docstring for BraffsQuintuplets.

    Args:
        morph: TODO
        repeats: TODO

    Returns: TODO

    """

    # straight
    notes1 = [0, 192, 0, 192, 0, 192, 0, 192, 0, 192]
    # phrased
    notes2 = [0, 274, 0, 137, 0, 137, 0, 275, 0, 137]

    # length equalization
    total_1 = length_equalization(notes1,repeats)
    total_2 = length_equalization(notes2,repeats)
    totaltick = total_tick(notes2,total_1,total_2,repeats)

    # rounding correction
    notes_final = rounding_correction(notes1,notes2,morph1,morph2,repeats,totaltick)

    # finalizing
    finalizing(notes_final,total_1,total_2,repeats)

def vienesse_waltz(morph1, morph2, repeats):
    """TODO: Docstring for VienesseWaltz.

    Args:
        morph: TODO
        repeats: TODO

    Returns: TODO

    """

    # straight
    notes1 = [0, 960, 0, 960, 0, 960]
    # phrased
    notes2 = [0, 720, 0, 1200, 0, 960]

    # length equalization
    total_1 = length_equalization(notes1,repeats)
    total_2 = length_equalization(notes2,repeats)
    totaltick = total_tick(notes2,total_1,total_2,repeats)

    # rounding correction
    notes_final = rounding_correction(notes1,notes2,morph1,morph2,repeats,totaltick)

    # finalizing
    finalizing(notes_final,total_1,total_2,repeats)

def text_command(morph1, morph2, repeats, comm1, comm2):
    """TODO: Docstring for textCommand.

    :arg1: TODO
    :returns: TODO

    """

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

    tick_rest = 0

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

    for note in str(comm1).replace("-", " ").split(" "):
        note_list1.append(str(note))
    for note in str(comm2).replace("-", " ").split(" "):
        note_list2.append(str(note))

    notes1 = []
    notes2 = []

    #notes
    for note in note_list1:
        notes1.append(int(note_length[str(note)[0]]))

    for note in note_list2:
        notes2.append(int(note_length[str(note)[0]]))

    # dots
    pos = 0
    for note in note_list1:
        n_dots = 0
        if "." in str(note):
            n_dots += int(str(note).count("."))
            for n in range(n_dots):
                notes1[pos] += int(notes1[pos]/(2*((n+1)**2-n)))
        pos += 1
                        
    pos = 0
    for note in note_list2:
        n_dots = 0
        if "." in str(note):
            n_dots += int(str(note).count("."))
            for n in range(n_dots):
                notes2[pos] += int(notes2[pos]/(2*((n+1)**2-n)))
        pos += 1

    # tuplets
    pos = 0
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
            notes1[pos] = int(notes1[pos]*(denom/nom))
        pos += 1
    pos = 0
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
            notes2[pos] = int(notes2[pos]*(denom/nom))
        pos += 1

    notes1_f = []
    notes2_f = []

    # tying notes
    pos = 0
    for note in str(comm1).split(" "):
        ties = 0
        if "-" in str(note):
            ties += int(str(note).count("-"))
        tied_value = notes1[pos]
        posi = 1
        if ties != 0:     
            for n in range(ties):
                tied_value += int(notes1[pos+posi])
                posi += 1
        notes1_f.append(tied_value)
        pos += 1+ties
    pos = 0
    for note in str(comm2).split(" "):
        ties = 0
        if "-" in str(note):
            ties += int(str(note).count("-"))
        tied_value = notes2[pos]
        posi = 1
        if ties != 0:     
            for n in range(ties):
                tied_value += int(notes2[pos+posi])
                posi += 1
        notes2_f.append(tied_value)
        pos += 1+ties

    # length equalization
    total_1 = length_equalization(notes1,repeats)
    total_2 = length_equalization(notes2,repeats)
    totaltick = total_tick(notes2,total_1,total_2,repeats)

    # rounding correction
    notes_final = rounding_correction(notes1,notes2,morph1,morph2,repeats,totaltick)

    # finalizing
    finalizing(notes_final,total_1,total_2,repeats)


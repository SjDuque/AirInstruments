import fluidsynth
import time
import threading
import pathlib

###########################################################################
# Locate SoundFont file
###########################################################################

root = pathlib.Path(__file__).parent.parent.resolve()

SOUND_FONT_FILE = str(pathlib.Path(root, ('assets/MuseScore_General.sf3')))

###########################################################################
# Creating a dictionary for easy conversion between MIDI values and notes
###########################################################################

NOTES = ('C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#', 'A', 'A#', 'B')
OCTAVES = (-1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9)

midi_map= {}

for i in range(128):
    n = NOTES[i % 12]
    o = str(OCTAVES[i // 12])
    midi_map[n+o] = i


###########################################################################
# Instrument Data Class
###########################################################################

class InstrumentData:
    IDs = {
        'ukulele': ((8, 24), 4, ('G4', 'C4', 'E4', 'A4')),
        'bass': ((0, 87), 4, ('E1', 'A1', 'D2', 'G2')),
        'guitar': ((0, 27), 6, ('E2', 'A2', 'D3', 'G3', 'B3', 'E4')),
        'funk_guitar': ((8, 24), 6, ('E2', 'A2', 'D3', 'G3', 'B3', 'E4')),
    }

###########################################################################
# Creating a Class to play a String Instrument
###########################################################################

class String:
    def __init__(self, fs):
        self.thread = None
        self.num_plucks = 0
        self.fs = fs
    
    def pluck(self, note, vel = 100):
        self.num_plucks += 1
        self.thread = threading.Thread(target = self.play, args=(note, vel))
        self.thread.start()
    
    def play(self, note, vel):
        
        time.sleep(0.051)
        cur_plucks = self.num_plucks
        self.fs.noteon(0, midi_map[note], vel)

        start = time.time()
        while(cur_plucks == self.num_plucks and time.time() - start < 1):
            time.sleep(0.05)

        self.fs.noteoff(0, midi_map[note])
    
    def is_plucked(self):
        return self.__is_plucked

###########################################################################
# String Instrument Class
###########################################################################

class StringInstrument:

    def __init__(self, instrument = 'ukulele'):
        self.fs = fluidsynth.Synth() # Ini
        self.fs.start()
        self.sfid = self.fs.sfload(SOUND_FONT_FILE)
        self.num_strings = None
        self.tuning = None
        self.strings = None
        self.choose_instrument(instrument)
        self.thread = None

    def choose_instrument(self, instrument):
        inst = InstrumentData.IDs[instrument]
        self.fs.program_select(0, self.sfid, inst[0][0], inst[0][1])
        self.num_strings = inst[1]
        self.tuning = inst[2]
        self.strings = [String(self.fs) for i in range(self.num_strings)]

    def strum_tuned(self):

        if len(self.tuning) is not len(self.strings):
            pass
        
        for i in range(len(self.strings)):
            self.strings[i].pluck(self.tuning[i])
            time.sleep(0.075/self.num_strings)
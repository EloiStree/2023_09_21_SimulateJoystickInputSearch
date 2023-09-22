import board  # type: ignore (this is a CircuitPython built-in)
from joystick_xl.inputs import Axis, Button, Hat
from joystick_xl.joystick import Joystick
import time
import usb_midi
import adafruit_midi
import digitalio

from adafruit_midi.control_change import ControlChange
from adafruit_midi.note_off import NoteOff
from adafruit_midi.note_on import NoteOn
from adafruit_midi.pitch_bend import PitchBend
midi = adafruit_midi.MIDI(midi_in=usb_midi.ports[0], in_channel=0,midi_out=usb_midi.ports[1], out_channel=0)
joystick = Joystick()

string_msg=""
string_val=""
i =0
joystick.add_input()
joystick.update(True)
print("JS "+str(joystick.num_axes)+" "+ str(joystick.num_buttons)+" "+ str(joystick.num_hats))
while True:
    i+=1
    #joystick.update_button((0, True))
    #joystick.update_button((1, True))
    #joystick.update_button((2, True))
    #joystick.update_axis((0, 1))
    #joystick.update_axis((1, 1))
    #vjoystick.update_axis((2, 1))
    #joystick.update_axis((3, 1))
    #joystick.update_axis((4, 1))
    #joystick.update_axis((5, 1))
    #joystick.update_axis((6, 1))
    #joystick.update_axis((7, 1))
    #midi.send(NoteOn(i+60, 120))
    #joystick.update_hat((0, 3))
    #joystick.update_hat((1, 3))
    #joystick.update_hat((2, 3))
    #joystick.update_hat((3, 3))
    joystick.update()
    
    #print("Hello1"+str(joystick.button[2].value))
    #joystick.update_button((0, False))
    #joystick.update_button((1, False))
    #joystick.update_button((2, False))
    #joystick.update_axis((0, 255))
    #joystick.update_axis((1, 255))
    #joystick.update_axis((2, 255))
    #joystick.update_axis((3, 255))
    #joystick.update_axis((4, 255))
    #joystick.update_axis((5, 255))
    #joystick.update_axis((6, 255))
    #joystick.update_axis((7, 255))
    #midi.send(NoteOff(i+60, 120))
    #joystick.update_hat((0, 8))
    #joystick.update_hat((1, 8))
    #joystick.update_hat((2, 8))
    #joystick.update_hat((3, 8))
    joystick.update()
    time.sleep(0.0001)
    
    msg = midi.receive()
    if msg is not None:
        print("Received:", msg, "at", time.monotonic())
    if msg is not None:
        #  if a NoteOn message...
        if isinstance(msg, NoteOn):
            if msg.note>=0 and msg.note <= 128:
                joystick.update_button((msg.note, True))
            string_msg = 'NoteOn'
            #  get note number
            string_val = str(msg.note)
            
        #  if a NoteOff message...
        if isinstance(msg, NoteOff):
            if msg.note>=0 and msg.note <= 128:
                joystick.update_button((msg.note, False))
            string_msg = 'NoteOff'
            #  get note number
            string_val = str(msg.note)
        #  if a PitchBend message...
        if isinstance(msg, PitchBend):
            string_msg = 'PitchBend'
            #  get value of pitchbend
            string_val = str(msg.pitch_bend)
        #  if a CC message...
        if isinstance(msg, ControlChange):
            string_msg = 'ControlChange'
            if msg.control>=0 and msg.control <= 7:
                joystick.update_axis((msg.control, msg.value*2))
            #  get CC message number
            string_val = str(msg.control) +" "+str(msg.value)
        #  update text area with message type and value of message as strings
        print(string_msg+"->"+string_val)
    
    
    
from math import sin
from sys import argv
import wave

morse = [".-", "-...", "-.-.", "-..", ".", "..-.", "--.", "....", "..", ".---",
         "-.-", ".-..", "--", "-.", "---", ".--.", "--.-", ".-.", "...", "-",
         "..-", "...-", ".--", "-..-", "-.--", "--.", "-----", ".----", "..---",
         "...--", "....-", ".....", "-....", "--...", "---..", "----.", "/"]

if len(argv) < 2:
    exit()

def beep(f, sec, freq):
    vals = []
    for i in range(int(8000 * sec)):
        vals.append(wave.struct.pack('h', sin((i / 8000.0) * 6.2831 * freq) * 51.2))
    f.writeframes("".join(vals))

f = wave.open("out.wav", "w")
f.setparams((1, 2, 8000, 0, 'NONE', 'not compressed'))

for c in "".join([morse[ord(l) - 22 if '0' <= l <= '9' else ord(l) - 97 if 'a' <= l <= 'z' else -1] for l in argv[1].lower()]):
    if c != "/":
        beep(f, [0.6, 0.2][c == '.'], 1000)
    beep(f, 0.2, 0)

f.close()

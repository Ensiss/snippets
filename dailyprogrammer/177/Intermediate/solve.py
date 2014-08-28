import math
import random
import sys
import wave

morse = [".-", "-...", "-.-.", "-..", ".", "..-.", "--.", "....", "..", ".---",
         "-.-", ".-..", "--", "-.", "---", ".--.", "--.-", ".-.", "...", "-",
         "..-", "...-", ".--", "-..-", "-.--", "--.", "-----", ".----", "..---",
         "...--", "....-", ".....", "-....", "--...", "---..", "----.", "/"]

if len(sys.argv) < 2:
    exit()

def beep(f, sec, freq):
    vals = []
    for i in range(int(8000 * sec)):
        vals.append(wave.struct.pack('h', math.sin((i / 8000.0) * 2 * 3.1415 * freq) * 128 * 0.4))
    f.writeframes("".join(vals))

f = wave.open("out.wav", "w")
f.setparams((1, 2, 8000, 0, 'NONE', 'not compressed'))

for c in "".join([morse[26 + ord(l) - ord('0') if (l >= '0' and l <= '9') else ord(l) - ord('a') if (l >= 'a' and l <= 'z') else -1] for l in sys.argv[1].lower()]):
    if c != "/":
        beep(f, [0.6, 0.2][c == '.'], 1000)
    beep(f, 0.2, 0)

f.close()

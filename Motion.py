import time
import functools
import numpy
import scipy
import slab
hrtf = slab.HRTF.kemar()


'''
- changing the ITD and ILD - moving around the head (left to right) 
'''
levels = [278, 296, 314]
trials = slab.Trialsequence(levels)
for levels in trials:
    hrtfsound = hrtf.apply(levels, slab.Binaural.pinknoise(hrtf.samplerate))
    hrtfsound.play()

hrtf = slab.HRTF.kemar()
sound = slab.Binaural.pinknoise()
sig = hrtf.apply(296, slab.Binaural.pinknoise(hrtf.samplerate))
moving = sig.itd_ramp(from_itd=-0.1, to_itd= -0.1)
moving = sig.ild_ramp(from_ild=-50, to_ild=50)
moving.play()

'''
- Right to Left 
'''
#
hrtf = slab.HRTF.kemar()
sound = slab.Binaural.pinknoise(duration= 10.0)
sig = hrtf.apply(296, slab.Binaural.pinknoise(hrtf.samplerate))
moving = sig.itd_ramp(from_itd= 0.1, to_itd= -0.1)
moving = sig.ild_ramp(from_ild=50, to_ild=-50)
moving.play()

'''
looming - could so static sounds but add increasing volume / decreasing itd?
'''

#
# signal1 = hrtf.apply(314, slab.Binaural.pinknoise(hrtf.samplerate, duration=12.0))
# signal1.ild = -0.01
# signal1.itd = -14
# signal1.level = 90
# signal1.externalize()
# signal1.ramp(when= 'onset', duration=10.0).play()
#
# signal2 = hrtf.apply(314, slab.Binaural.pinknoise(hrtf.samplerate, duration=15.0))
# signal2.ild = 0.01
# signal2.itd = 0
# signal2.level = 90
# signal2.externalize()
# signal2.ramp(when= 'onset', duration=13.0).play()

'''
my life be like
'''

# vowels = ["o", "a"]
# for i in vowels:
#     vowel = slab.Sound.vowel(vowel=i, duration=1.0)
#     vowel.play()
# silence = slab.Sound.silence(duration=1.0)
# silence.play()
# sig1 = slab.Sound.vowel(vowel="o", duration= 2.0)
# sig1.play()
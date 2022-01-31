'''
setup
'''
import numpy
import scipy
import slab

_adapter_speed = 150
slab.Binaural.set_default_samplerate(44100)
hrtf = slab.HRTF.kemar()

'''
trials 
'''
# #trialsequence that plays at -90, 0 and 90, right now has no itd
levels = [278, 296, 314]
trials = slab.Trialsequence(levels)
for levels in trials:
    hrtfsound = hrtf.apply(levels, slab.Binaural.pinknoise(hrtf.samplerate))
    hrtfsound.play()


#trial sequence that changes the itd

itdlevels = []


'''
right now the sound doesnt have itd 
figure this out:
itd = sig.azimuth_to_itd(azimuth=speaker_position) -> answers are in the log 
'''

# levels = [278, 296, 314]
#
# trials = slab.Trialsequence(levels)
# for levels in trials:
#     hrtfsound = hrtf.apply(levels, slab.Binaural.pinknoise(hrtf.samplerate))
#     hrtfsound.externalize()
#     hrtfsound.play()







# for i in sourceidx:
#  HRTF.apply(sound = sound, source = i, allow_resampling= True)



#the sound


# #not the sound
# def moving_gaussian(speed=100, width=7.5, SNR=10, direction='left'):
#     """
#     Make a wide Gauss curve shaped stimulus that moves horizontally across
#     a range of virtual loudspeakers. This is the base stimulus of the experiment.
#     """
#     if direction == 'left':
#         dir = -1
#         starting_loc = _speaker_positions[-1]
#     else:
#         dir = 1
#         starting_loc = _speaker_positions[0]
#
#     def loc(time):
#         return (speed * time) * dir + starting_loc
#     # make times vector from speed and positions angle difference
#     end_time = _speaker_positions.ptp() / speed
#     time_delta = 0.01  # 10 ms
#     times = numpy.arange(0, end_time + time_delta, time_delta)
#     # step through time, saving speaker amplitudes for each step
#     speaker_amps = numpy.zeros((len(_speaker_positions), len(times)))
#     for idx, t in enumerate(times):
#         speaker_amps[:, idx] = scipy.stats.norm.pdf(_speaker_positions, loc=loc(t), scale=width)
#     # scale the amplitudes to max 0, min -SNR dB
#     maximum = scipy.stats.norm.pdf(0, loc=0, scale=width)
#     minimum = speaker_amps.min()
#     speaker_amps = numpy.interp(speaker_amps, [minimum, maximum], [-SNR, 0])
#     speaker_signals = []
#     hrtf = slab.HRTF.kemar()
#     for i, speaker_position in enumerate(_speaker_positions):
#         sig = slab.Binaural.pinknoise(duration=end_time)
#         spectral_shape = hrtf.interpolate(azimuth=speaker_position, elevation=0)
#         sig = spectral_shape.apply(sig)  # apply HRTF filter from correct direction (ITD still missing)
#         itd = sig.azimuth_to_itd(azimuth=speaker_position)
#         sig = sig.itd(itd)  # add the necessary ITD
#         sig = sig.envelope(apply_envelope=speaker_amps[i, :], times=times, kind='dB')
#         speaker_signals.append(sig)
#     sig = speaker_signals[0]
#     for speaker_signal in speaker_signals[1:]:  # add sounds
#         sig += speaker_signal
#     sig /= len(_speaker_positions)
#     sig.ramp(duration=end_time/3)  # ramp the sum
#     sig.filter(frequency=[500, 14000], kind='bp')
#     sig.level = 75
#     return sig



# #static right
# staticright = slab.Binaural.pinknoise(duration=5.0)
# staticright.left.level = 75
# staticright.right.level = 85
# staticright.externalize()
# #behind.ild(14.93)
# #behind.itd(-0.0006)
# staticright.play()

# #static left
# staticleft = slab.Binaural.pinknoise(duration=5.0)
# staticleft.left.level = 85
# staticleft.right.level = 75
# staticleft.externalize()
# staticleft.play()

# #static behind need to compute the azimuth
# staticleft = slab.Binaural.pinknoise(duration=5.0)
# staticleft.left.level = 80
# staticleft.right.level = 80
# staticleft.externalize()
# staticleft.play()



#moving from 90 to -90
#from_ild = 14.93
#to_ild = -14.93
#behind_moving = behind.ild_ramp(from_ild, to_ild)
#behind.externalize() # apply filter in place
#behind.play() # best through headphones



#nonmoving
#5 seconds of pink noise
#stillbehind.ild_ramp(from_ild=- 50, to_ild=50)
#this is incorrect, need to compute the ILDs
#stillbehind.play()

#moving
#moving = stimulus.itd_ramp(from_itd=-0.001, to_itd=0.01)
#moving.play()

#change the azimuth
#lateralized = stimulus.at_azimuth(azimuth=-90, ils=level_spectrum)




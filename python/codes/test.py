import librosa
import soundfile as sf
x,_ = librosa.load('../../musics/peppermint.wav', sr=16000)
sf.write('tmp.wav', x, 16000)
import openai
# import librosa
# import os
# os.environ['LIBROSA_DATA_DIR'] = '/path/to/librosa-data/audio'
# import numpy as np
# # import ffmpeg
# from pydub import AudioSegment

# Set up OpenAI API key
api_key = "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"
openai.api_key = api_key

f = open(r"C:\Users\smita\PycharmProjects\pythonProject6\.venv\Scripts\music_notes.txt", "w")

def getMusic(song) :
    prompt = "Define all the notes and durations for a sonic pi program to compose the complete music of the" + song + "."
    response = openai.ChatCompletion.create(model = "gpt-3.5-turbo",
                                            messages=[{"role": "system", "content": prompt}])
    content = response
    print(content.choices[0].message.content) # delete after
    f.write(content.choices[0].message.content)

getMusic("twinkle twinkle little star")



#
# # Load an MP3 file
# audio = AudioSegment.from_mp3(r"C:\Users\smita\Desktop\MakeUofT\76EFF\Twinkle Twinkle Little Star.mp3")
#
# filename = librosa.ex(os.environ['LIBROSA_DATA_DIR'])
# librosa.load(filename, offset=15.0, duration=5.0)
#
# y, sr = librosa.load(r"C:\Users\smita\Desktop\MakeUofT\76EFF\Twinkle Twinkle Little Star.mp3")

# def extract_melody(audio_file, output_file, frame_length=2048, hop_length=512, threshold=0.5):
#     # Load the audio file
#     y, sr = librosa.load(audio_file)
#
#     # Convert to frequency domain
#     D = np.abs(librosa.stft(y, n_fft=frame_length, hop_length=hop_length))
#
#     # Find dominant frequencies
#     max_freq_indices = np.argmax(D, axis=0)
#     dominant_freqs = librosa.fft_frequencies(sr=sr, n_fft=frame_length)[max_freq_indices]
#
#     # Extract melody by applying a threshold
#     melody_mask = dominant_freqs > threshold
#     melody_freqs = dominant_freqs * melody_mask
#
#     # Reconstruct melody
#     melody_stft = np.zeros_like(D)
#     for i in range(melody_stft.shape[1]):
#         if melody_mask[i]:
#             idx = np.argmin(np.abs(librosa.fft_frequencies(sr=sr, n_fft=frame_length) - melody_freqs[i]))
#             melody_stft[idx, i] = D[idx, i]
#
#     # Inverse Fourier transform to get time-domain signal
#     melody_signal = librosa.istft(melody_stft, hop_length=hop_length)
#
#     # Save the simplified melody to a new audio file
#     librosa.output.write_wav(output_file, melody_signal, sr)
#
# # Example usage:
# audio_file = "your_song.wav"
# output_file = "simple_melody.wav"
# extract_melody(audio_file, output_file)
import librosa

# Loading audio file
audio_file = "audio_sorohanro_-_solo-trumpet-06.ogg"
y, sr = librosa.load(audio_file)

# Extracting the chroma features and onsets
chroma = librosa.feature.chroma_stft(y=y, sr=sr)
onset_frames = librosa.onset.onset_detect(y=y, sr=sr)

first = True
notes = []
for onset in onset_frames:
  chroma_at_onset = chroma[:, onset]
  note_pitch = chroma_at_onset.argmax()
  # For all other notes
  if not first:
      note_duration = librosa.frames_to_time(onset, sr=sr)
      notes.append((note_pitch,onset, note_duration - prev_note_duration))
      prev_note_duration = note_duration
  # For the first note
  else:
      prev_note_duration = librosa.frames_to_time(onset, sr=sr)
      first = False
print("Note pitch \t Onset frame \t Note duration")
for entry in notes:
  print(entry[0],'\t\t',entry[1],'\t\t',entry[2])

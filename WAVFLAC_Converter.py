from pydub import AudioSegment
import os


def flac_to_wav(input_flac_file, output_folder):
    output_file_name = os.path.splitext(input_flac_file)[0] + ".wav"
    output_file_path = output_file_name.split("/")[-1]
    audio = AudioSegment.from_file(input_flac_file, format='flac')
    audio.export(f"{output_folder}/{output_file_path}", format='wav')
    print(f"Converted {input_flac_file} to {output_file_name}")

def wav_to_flac(input_wav_file, output_folder):
    output_file_name = os.path.splitext(input_wav_file)[0] + ".flac"
    output_file_path = output_file_name.split("/")[-1]
    audio = AudioSegment.from_wav(input_wav_file)
    audio.export(f"{output_folder}/{output_file_path}", format="flac")
    print(f"Converted {input_wav_file} to {output_file_name}")

def get_itempath_for_items_in_folder(folder_path):  
    item_list = [] 
    for item in os.listdir(folder_path):
        item_path = f"{folder_path}/{item}"
        item_list.append(item_path)
    return item_list

# Specify the paths for the input FLAC file and the desired output WAV file
input_file = 'Stuff/Test.wav'
input_file2 = 'Stuff/Test.flac'
output_folder = 'Stuff'

# Convert the FLAC file to WAV format
#wav_to_flac(input_file)
#flac_to_wav(input_file2)
for x in get_itempath_for_items_in_folder("Testfiles"):
    flac_to_wav(x, "WavFiles")
for x in get_itempath_for_items_in_folder("WavFiles"):
    wav_to_flac(x, "FlacFiles")

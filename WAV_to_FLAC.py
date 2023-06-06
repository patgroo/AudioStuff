import os
from pydub import AudioSegment

# Input and output directories
input_folder = "Testfiles"
output_folder = "FlacFiles"

# Create the output folder if it doesn't exist
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

# Search for WAV files in the input folder
for file_name in os.listdir(input_folder):
    if file_name.endswith(".wav"):
        # Load the WAV file using AudioSegment
        input_path = os.path.join(input_folder, file_name)
        audio = AudioSegment.from_wav(input_path)

        # Create the output file name and path
        output_file_name = os.path.splitext(file_name)[0] + ".flac"
        output_path = os.path.join(output_folder, output_file_name)

        # Export the audio as FLAC
        audio.export(output_path, format="flac")

        print(f"Converted {file_name} to {output_file_name}")

print("Conversion complete.")

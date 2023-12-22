from moviepy.editor import *

welcome = """""""""""""""""""""""""""""""""""""""
          " Welcome to Video to Audio Converter "
          """""""""""""""""""""""""""""""""""""""
print (welcome)

# Delete original file after conversion
delete_original = True # Set to False if you want to keep the original file

# defaults
default_source_path = "./videos/"
default_output_path = "./audios/"

# Create Directories if not exists
if not os.path.exists(default_source_path):
    os.mkdir(default_source_path)
if not os.path.exists(default_output_path):
    os.mkdir(default_output_path)

source_path = "./videos/" # or use default_source_path
output_path = "C:/Users/Admin/Music/" # or use default_output_path

for file in os.listdir(source_path):
    file_name = file[:-4] + ".mp3"

    # If already converted, cleanup then skip
    if (os.path.exists(output_path + file_name)):
        print ("Already converted. Removing file: " + file_name)
        # Remove
        os.remove(source_path + file)
        continue
    
    # If not mp4, skip
    if not file.endswith(".mp4"):
        continue
    
    # Convert
    clip = VideoFileClip(source_path + file)
    clip.audio.write_audiofile(output_path + file_name)
    clip.close()

    # Delete original
    if delete_original == True:
        os.remove(source_path + file)
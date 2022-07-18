import os
import ffmpeg # pip install ffmpeg-python

start_dir = os.getcwd() # Get the file path

# Function that convert a .mkv file to .mp4 file (REQUIRE FFMPEG.EXE IN THE SAME FOLDER THAT THIS SCRIPT)
def convert_to_mp4(mkv_file):
    name, ext = os.path.splitext(mkv_file)
    out_name = name + ".mp4"
    ffmpeg.input(mkv_file).output(out_name).run()
    print("Finished converting {}".format(mkv_file))

# for-loop that iterate all the files in the actual path
for path, folder, files in os.walk(start_dir):
    for file in files:
        # If the loop find a .mkv file, call the previous function to convert it
        if file.endswith('.mkv'):
            print("Found file: %s" % file)
            convert_to_mp4(os.path.join(start_dir, file))
        else:
            pass
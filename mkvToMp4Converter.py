import os
import ffmpeg # pip install ffmpeg-python
import sys

start_dir = os.getcwd() # Get the file path

# Function that convert a .mkv file to .mp4 file (REQUIRE FFMPEG.EXE IN THE SAME FOLDER THAT THIS SCRIPT)
def convert_to_mp4(mkv_file):
    name, ext = os.path.splitext(mkv_file)
    out_name = name + ".mp4"
    ffmpeg.input(mkv_file).output(out_name).run()
    print("Finished converting {}".format(mkv_file))


def convert_folder_to_mp4():
    # for-loop that iterate all the files in the actual path
    for path, folder, files in os.walk(start_dir):
        for file in files:
            # If the loop find a .mkv file, call the previous function to convert it
            if file.endswith(".mkv"):
                print("Found file: %s" % file)
                convert_to_mp4(os.path.join(start_dir, file))
            else:
                pass


if __name__ == "__main__":
    if (len(sys.argv) == 1): # checks if the user has opened the script with a file, in this case the script will only convert that file. 
                             # Otherwise will convert all the .mkv files in the actual folder
        print("No file has been passed, all the .mkv files in actual folder will be convert. Press any key to continue")
        input()
        convert_folder_to_mp4()
    else:
        print("A file has been passed: " + sys.argv[1])
        print("Press Enter to continue")
        input()
        convert_to_mp4(sys.argv[1])

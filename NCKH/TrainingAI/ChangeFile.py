import os
import glob

def rename_images(directory: str) -> None:
    # Get a list of all JPEG files in the directory
    files = glob.glob(os.path.join(directory, "*.jpg")) + glob.glob(os.path.join(directory, "*.png"))

    # Sort the files by their names
    files.sort()

    # Rename the files
    for i, file in enumerate(files, start=1):
        # Get the file name without the extension
        name, extension = os.path.splitext(os.path.basename(file))

        # Construct the new file name with the index and extension
        new_name = f"{"i"}{i}{extension}"

        # Construct the new file path
        new_path = os.path.join(directory, new_name)

        # Rename the file
        os.rename(file, new_path)

# Call the function with the directory path
rename_images("./image")
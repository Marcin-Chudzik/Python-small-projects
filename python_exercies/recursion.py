import os
from data_visualization.photos_metadata.anonymize_photos_metadata import anonymize_exif


# Recursive computation of an element in the Fibonacci sequence.
def fib_rec(n):
    """ Function returns 'n' element of Fibonacci sequence. """
    if n < 1:
        return 0
    if n < 2:
        return 1
    return fib_rec(n - 1) + fib_rec(n - 2)


# Example of used os.walk()
def exif_anonymize():
    directory = "."
    images_files = [".jpg", ".jpeg", ".png"]

    for dirpath, dirname, files in os.walk(directory):

        for file in files:
            image_file = os.path.join(dirpath, file)
            ext = os.path.splitext(image_file)[1].lower()
            print(f"For a file: {image_file} extender is {ext}")

            if ext in images_files and "_anon" not in image_file:
                print(f"Anonymize file: {image_file}")
                print(anonymize_exif(image_file))


if __name__ == "__main__":
    exif_anonymize()
else:
    print("Script for execute by yourself")

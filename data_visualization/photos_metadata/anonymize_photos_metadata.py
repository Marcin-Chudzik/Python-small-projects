import sys
import os
from exif import Image


def test_file(file: str) -> bool:
    """ Checking a file existing """
    if not os.path.exists(file):
        return False
    return True


def open_image(file: str) -> Image or bool:
    """ Open a graphic file """
    with open(file, 'rb') as image_file:
        try:
            image = Image(image_file)
        except:
            return False
    # After a file close
    return image


def info_exif(file_name: str):
    """ Downloading an Exif data and displaying them """
    if not test_file(file_name):
        print(f"File {file_name} not exists.")
        return None

    image_data = open_image(file_name)
    if not image_data:
        print("Wrong data!")
        return None

    if not image_data.has_exif:
        print("Wrong data!")
        return None

    image_attrs = image_data.get_all()
    for attr in image_attrs:
        value = image_attrs[attr]
        print(f"Attribute: {attr} = {value}")


def anonymize_exif(file_name: str):
    """ Replacing an original Exif data with our imagined """
    image_data = open_image(file_name)
    if not image_data:
        return "Wrong data!"

    if not image_data.has_exif:
        return f"No EXIF data for a file: {file_name}"

    image_attrs = image_data.get_all()
    for attrib in image_attrs:
        if "gps" in attrib or "maker_note" in attrib or "date" in attrib:
            del image_data[attrib]
        elif "make" in attrib or "model" in attrib or "software" in attrib:
            image_data[attrib] = "Python"

    new_file = os.path.splitext(file_name)[0] + "_anon" + os.path.splitext(file_name)[1]

    with open(new_file, "wb") as anon_file:
        anon_file.write(image_data.get_file())

    return f"Done! -> {new_file}"


if __name__ == "__main__":
    args = sys.argv
    if len(args) == 2:
        print(f"Starting for one file: {args[1]} - information")
        info_exif(args[1])
        sys.exit(0)
    else:
        print(f"Calling only a script {args[0]} is not able,")
        sys.exit(2)

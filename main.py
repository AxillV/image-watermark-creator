import os
from PIL import Image

# Set the path and change working directory to the path of the images.
path = "test"
os.chdir(path)

# Set some constants for the desired size of the x axis for the image and the logo filename.
X_FIT_SIZE = 800
LOGO_FILENAME = "testing.png"

# Open the logo and also set some variables for its width and height.
logoIm = Image.open(LOGO_FILENAME)
logoWidth, logoHeight = logoIm.size

# Create 2 new folders in the directory, don't raise an error if the folder already exists.
os.makedirs("With Logo", exist_ok=True)
os.makedirs("Without Logo", exist_ok=True)

# Loop over all files in the working directory.
for filename in os.listdir('.'):
    if not (filename.endswith('.png') or filename.endswith('.jpg')) or filename == LOGO_FILENAME:
        continue  # Skip non-image files and the logo file itself.

    # If the file passes through the check, open the image and save its width and height
    im = Image.open(filename)
    width, height = im.size

    # Check if image needs to be resized.
    if width > X_FIT_SIZE or width < X_FIT_SIZE:

        # Calculate the new width and height to resize to.
        height = int((X_FIT_SIZE / width) * height)
        width = X_FIT_SIZE

        # Resize the image.
        print("Resizing {0}...".format(filename))
        im = im.resize((width, height))

    # Save the changes for the image without the logo.
    im.save(os.path.join("Without Logo", filename))

    # Create 4 instances of the image, so we can edit each one and paste the logo on a different
    # corner each time without keeping the old one. We need to do this so we don't reference
    # the exact im Image because then every change to imBR affects im and vice-versa.
    imBR = im.resize((width, height))
    imBL = im.resize((width, height))
    imTL = im.resize((width, height))
    imTR = im.resize((width, height))

    # Add the logo to the image and save the image as the name + corner of logo.
    # This is being done for all 4 corners.
    # The last line of code in the group of code for each corner, puts the
    # location of the logo between the name and the extension (.png or .jpg).

    # Add logo to bottom right corner.
    print('Adding logo to the bottom right corner of {0}...'.format(filename))
    imBR.paste(logoIm, (width - logoWidth, height - logoHeight), logoIm)
    imBR.save(os.path.join('With Logo', "{0}-BottomRight{1}".format(filename[:-4], filename[-4:])))

    # Add logo to bottom left corner.
    print('Adding logo to the bottom left corner of {0}...'.format(filename))
    imBL.paste(logoIm, (0, height - logoHeight), logoIm)
    imBL.save(os.path.join('With Logo', "{0}-BottomLeft{1}".format(filename[:-4], filename[-4:])))

    # Add logo tp top left corner.
    print('Adding logo to the top left corner of {0}...'.format(filename))
    imTL.paste(logoIm, (0, 0), logoIm)
    imTL.save(os.path.join('With Logo', "{0}-TopLeft{1}".format(filename[:-4], filename[-4:])))

    # Add logo to top right corner.
    print('Adding logo to the top right corner of {0}...'.format(filename))
    imTR.paste(logoIm, (width - logoWidth, 0), logoIm)
    imTR.save(os.path.join('With Logo', "{0}-TopRight{1}".format(filename[:-4], filename[-4:])))

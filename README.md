# image2pdf

Convert a list of images to a single pdf, one page per image.

NOTE: I recommend using this tool instead of my very simple script, because the Pillow library seems to re-encode images for the pdf, which is very much not what I wanted, and this other tool actually handles that correctly: https://gitlab.mister-muffin.de/josch/img2pdf

## Install

Either use the python script and install the dependencies in `requirements.txt`, or download a binary release from the GitHub releases page (Windows only, built with pyinstaller).

## Usage

    image2pdf <output.pdf> <inputimage.ext>...

**Example:**

    image2pdf mynewdoc.pdf img1.jpg img2.png img3.webp

## License

Licensed under the MIT license, see the [LICENSE](LICENSE) file in the repository.

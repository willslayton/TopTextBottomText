# TopTextBottomText
Old style meme generator written in Python using PIL.

## Usage
*\*Requires **PIL**, **os**, and **random** and the system to have the font "Impact" to work properly.*

`TopTextBottomText.Meme(background, top, bottom)`generates a meme using a path to an image and top/bottom text.

`TopTextBottomText.randomMeme(directory, top, bottom)`picks random file from a directory for image, then generates meme.

The final image should be titled `freshmeme.png` and will overwrite itself upon another call.

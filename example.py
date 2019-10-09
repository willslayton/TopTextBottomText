import TopTextBottomText
# An example of usage where the background is randomly chosen from a folder called 'Templates' and a user can enter their own top/bottom text on CLI.

top = input("Top text > ")
bottom = input("Bottom text > ")
TopTextBottomText.randomMeme("Templates", top, bottom)
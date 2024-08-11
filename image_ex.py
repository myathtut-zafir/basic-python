from PIL import Image # type: ignore

word=Image.open('world_matrix.png')
mask=Image.open('mask.png')
words=word.paste(mask,(0,0),mask)
words_resize=words.resize(1015,559) # type: ignore
col=words_resize.putalpha(0)
print(mask)
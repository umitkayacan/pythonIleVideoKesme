from moviepy.editor import *

myvideo1=VideoFileClip('DSC_1618.MOV') ##Video Dosyası

myvideo1edited=myvideo1.subclip(5,10) ##Başlangıç ve Bitiş Saniyeleri
myvideo1edited.write_videofile('deneme.mp4',codec='libx264') ##Yeni dosya adı ve Codec seçimi
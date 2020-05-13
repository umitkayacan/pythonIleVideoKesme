# moviepy Modülünü Kullanarak Video Kesme

1.  https://imagemagick.org/script/download.php adresinden uygun exe'yi indirip kuralım

2. https://github.com/Zulko/moviepy adresinden tüm repository'i indirelim

3. İndirdiğimiz dosyayı herhangi bir yer açalım, ve moviepy/config.py dosyasını editleyelim, editleyeceğimiz IMAGEMAGICK_BINARY
değikeninin değeridir. Buraya, az önce kurduğumuz imagemagick'in convert exe'sinin yolunu yazıyoruz. 
IMAGEMAGICK_BINARY = os.getenv("IMAGEMAGICK_BINARY", "auto-detect")
auto-detect'i değiştirelim
IMAGEMAGICK_BINARY = os.getenv("IMAGEMAGICK_BINARY", "C:\Program Files\ImageMagick-7.0.10-Q16\convert.exe")


from gtts import gTTS
import os
story = """
Fil ve fare çok iyi arkadaşlarmış. Bir gün ormanda yürürlerken karşılarına kocaman bir çuval dolusu fıstık çıkmış. İki arkadaş da fıstığı çok severlermiş, çok heveslenmişler. Yuvalarına taşımaya karar vermişler. Fil çuvalı yerinden kaldırmaya çalışmış ama nafile. Çuval o kadar ağırmış ki yerinden kalkmıyormuş. Birkaç kere daha denemiş. Olmamış. En sonunda vazgeçmiş. 

Üzgün bir şekilde yuvalarına dönmüşler. Fil o kadar yorulmuş ki hemen uyuyakalmış. Uyandığında ise şaşırmış. Çünkü fıstık çuvalı yanındaymış. "Nasıl oldu bu iş?" diye sormuş fareye, "Bunu kıpırdatmak bile imkansızdı".

Fare de demiş ki, "Haklısın, çuvalı taşıyamazdım ama ben sadece 1 fıstık taşıyabiliyordum. Öyle de yaptım. Her defasında 1 fıstık."

Kıssadan hisse, bugün kapasitenizin üstünde gibi görünen bir hedefi kapasiteniz dahilinde küçük küçük parçalara bölerseniz "imkansız" diye bir şey olmaz.
"""

tts = gTTS(text=story, lang='tr')
tts.save("fil_ve_fare.mp3")
#os.system("mpg321 good.mp3")


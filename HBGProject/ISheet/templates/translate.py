import goslate

text = "Shaji is an idiot man"
gs = goslate.Goslate()
translatedText = gs.translate(text,'hi')

print(translatedText)

gs = None

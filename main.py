import pandas
from googletrans import Translator

translator = Translator()

words_tr = ["Sokak", "Cadde", "İnsan", "Dünya",
            "Sahil", "Özgürlük", "Yaşam", "Galibiyet"]

df = pandas.DataFrame(columns=["Türkçe", "İngilizce", "Fransızca",
                           "Almanca", "İspanyolca", "Arapça", "Rusça"])

for word in words_tr:
    df = df._append(
        {
            "Türkçe" : word,
            "İngilizce" : translator.translate(word, dest="en").text,
            "Fransızca" : translator.translate(word,dest="fr").text,
            "Almanca" : translator.translate(word,dest="de").text,
            "İspanyolca" : translator.translate(word,dest="fr").text,
            "Arapça" : translator.translate(word,dest="ar").text,
            "Rusça" : translator.translate(word,dest="ru").text,
        },
        ignore_index=True)

print(df)





import os
from collections import Counter
import nltk
from nltk.corpus import stopwords

def find_most_common_words(folder_path, limit=25):
    word_counter = Counter()

    # Mendownload stopwords jika belum tersedia
    nltk.download("stopwords")

    # Mengambil stopwords dalam bahasa Indonesia dan Inggris
    stop_words_indonesia = set(stopwords.words("indonesian"))
    stop_words_english = set(stopwords.words("english"))

    for filename in os.listdir(folder_path):
        if filename.endswith(".txt"):
            file_path = os.path.join(folder_path, filename)
            with open(file_path, "r") as file:
                words = file.read().lower().split()
                # Menyaring stopwords
                words = [word for word in words if word not in stop_words_indonesia and word not in stop_words_english]
                word_counter.update(words)

    most_common_words = word_counter.most_common(limit)
    return most_common_words

# Ganti "folder_path" dengan path folder yang ingin Anda cari
folder_path = "hasil"
most_common_words = find_most_common_words(folder_path, limit=25)

if most_common_words:
    print("25 kata paling sering (setelah penyaringan stopwords):")
    for word, frequency in most_common_words:
        print("Kata:", word)
        print("Frekuensi:", frequency)
        print()
else:
    print("Tidak ada file .txt dalam folder tersebut.")

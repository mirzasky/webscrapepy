import os
from collections import Counter
import nltk
from nltk.corpus import stopwords
import mysql.connector
from mysql.connector import Error

def find_most_common_words(folder_path, limit=25):
    word_counter = Counter()

    nltk.download("stopwords")
    stop_words_indonesia = set(stopwords.words("indonesian"))
    stop_words_english = set(stopwords.words("english"))

    for filename in os.listdir(folder_path):
        if filename.endswith(".txt"):
            file_path = os.path.join(folder_path, filename)
            with open(file_path, "r") as file:
                words = file.read().lower().split()
                words = [word for word in words if word not in stop_words_indonesia and word not in stop_words_english]
                word_counter.update(words)

    most_common_words = word_counter.most_common(limit)
    return most_common_words

def insert_words_to_database(words):
    try:
        connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="scraping"
        )
        
        cursor = connection.cursor()
        insert_query = "INSERT INTO websc (waktu, kata, frekuensi) VALUES (NOW(), %s, %s)"

        for word, frequency in words:
            data = (word, frequency)
            cursor.execute(insert_query, data)

        connection.commit()
        print("Kata-kata berhasil dimasukkan ke dalam basis data")

    except Error as e:
        print("Terjadi kesalahan saat menyimpan data ke dalam basis data:", e)

    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()

# Ganti "folder_path" dengan path folder yang ingin Anda cari
folder_path = "hasil"
most_common_words = find_most_common_words(folder_path, limit=25)

if most_common_words:
    insert_words_to_database(most_common_words)
else:
    print("Tidak ada file .txt dalam folder tersebut.")

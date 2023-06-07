import os
import requests
from bs4 import BeautifulSoup

# Fungsi untuk melakukan scraping berdasarkan URL
def scrape_url(url):
    try:
        response = requests.get(url)
        response.raise_for_status()  # Membuang exception jika terjadi error pada server
        
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # Mengambil judul dari halaman web
        title = soup.title.string
        
        # Mengambil isi konten dari halaman web
        content = soup.get_text()
        
        return title, content
    
    except requests.exceptions.RequestException as e:
        print("Terjadi kesalahan saat mengakses URL:", url)
        print("Error:", str(e))
        return None, None
    
    except (AttributeError, KeyError) as e:
        print("Judul tidak ditemukan pada halaman:", url)
        print("Error:", str(e))
        return None, None

# Fungsi untuk menyimpan hasil scraping dalam file .txt
def save_to_file(title, content):
    if title is not None and content is not None:
        folder = 'hasil'
        if not os.path.exists(folder):
            os.makedirs(folder)
        
        filename = os.path.join(folder, title + '.txt')
        with open(filename, 'w', encoding='utf-8') as file:
            file.write(content)
        print("Hasil scraping disimpan dalam file", filename)

# Membaca daftar URL dari file .txt
def read_urls_from_file(filename):
    urls = []
    with open(filename, 'r') as file:
        for line in file:
            urls.append(line.strip())
    return urls

# Main program
if __name__ == "__main__":
    # Nama file .txt yang berisi daftar URL
    url_filename = 'daftar_url.txt'
    
    # Membaca daftar URL dari file .txt
    urls = read_urls_from_file(url_filename)
    
    # Melakukan scraping untuk setiap URL
    for url in urls:
        title, content = scrape_url(url)
        save_to_file(title, content)

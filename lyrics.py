import tkinter as tk
import random

# --- Konfigurasi Layar ---
WINDOW_WIDTH = 800
WINDOW_HEIGHT = 500
PARTICLE_COUNT = 150

# --- Data Lirik (Teks, Durasi tampil dalam milidetik) ---
# Kamu bisa menambahkan lirik lainnya di sini
lyrics_data = [
    ("Yeah i miss you", 3500),
    ("I know it's true", 3000),
    ("But what if I call?", 3000),
    ("And you pick up the phone", 3500),
    ("Merry Christmas", 4000)
]

# --- Setup Jendela Utama ---
root = tk.Tk()
root.title("Animasi Lirik")
root.geometry(f"{WINDOW_WIDTH}x{WINDOW_HEIGHT}")
root.configure(bg="#000000") # Latar belakang hitam
root.resizable(False, False)

# --- Canvas untuk Animasi Salju/Hujan ---
canvas = tk.Canvas(root, bg="#000000", highlightthickness=0)
canvas.pack(fill="both", expand=True)

# --- Label untuk Teks Lirik ---
# Persis seperti di gambar, menggunakan font Helvetica, bold, dan warna putih
lyric_label = tk.Label(root, text="", font=("Helvetica", 30, "bold"), fg="white", bg="#000000")
lyric_label.place(relx=0.5, rely=0.5, anchor="center")

# --- Logika Partikel (Hujan/Salju) ---
particles = []
for _ in range(PARTICLE_COUNT):
    x = random.randint(0, WINDOW_WIDTH)
    y = random.randint(0, WINDOW_HEIGHT)
    speed = random.uniform(2, 6)
    length = random.randint(4, 12) # Panjang garis vertikal
    
    # Membuat garis putih kecil yang terlihat seperti hujan/meteor
    item = canvas.create_line(x, y, x, y + length, fill="white", width=2)
    particles.append({'item': item, 'speed': speed, 'length': length})

def animate_particles():
    for p in particles:
        canvas.move(p['item'], 0, p['speed']) # Menggerakkan ke bawah
        pos = canvas.coords(p['item'])
        
        # Jika partikel melewati batas bawah layar, kembalikan ke atas
        if pos[1] > WINDOW_HEIGHT:
            x = random.randint(0, WINDOW_WIDTH)
            length = p['length']
            canvas.coords(p['item'], x, -length, x, 0)
            
    root.after(30, animate_particles) # Mengulang fungsi setiap 30ms (~33 fps)

# --- Logika Sinkronisasi Lirik ---
def play_lyrics(index=0):
    if index < len(lyrics_data):
        text, duration = lyrics_data[index]
        lyric_label.config(text=text) # Update teks di layar
        
        # Jadwalkan lirik berikutnya
        root.after(duration, play_lyrics, index + 1)
    else:
        # Loop kembali ke awal jika sudah habis (opsional)
        play_lyrics(0)

# --- Menjalankan Program ---
animate_particles()           # Mulai animasi hujan
root.after(1000, play_lyrics) # Tunggu 1 detik sebelum lirik pertama muncul

root.mainloop() # Menahan jendela agar tetap terbuka
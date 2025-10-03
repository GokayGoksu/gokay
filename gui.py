import tkinter as tk
from tkinter import messagebox
import numpy as np
import cv2
import math

def olustur():
    try:
        res_x = int(entry_res_x.get())
        res_y = int(entry_res_y.get())
        h = float(entry_h.get())
        fov_x = float(entry_fov_x.get())
        fov_y = float(entry_fov_y.get())
        en = float(entry_en.get())
        boy = float(entry_boy.get())
    except ValueError:
        messagebox.showerror("Hata", "Lütfen tüm değerleri doğru girin!")
        return
    
    # Alan hesaplama
    Length_x = 2 * math.tan(math.radians(fov_x / 2)) * h
    Length_y = 2 * math.tan(math.radians(fov_y / 2)) * h
    
    GSD_x = Length_x / res_x
    GSD_y = Length_y / res_y
    
    pixel_x = int(en / GSD_x)
    pixel_y = int(boy / GSD_y)
    
    # Görüntü oluştur
    img = np.zeros((res_y, res_x, 3), dtype=np.uint8)
    center_x = res_x // 2
    center_y = res_y // 2
    top_left = (center_x - pixel_x // 2, center_y - pixel_y // 2)
    bottom_right = (center_x + pixel_x // 2, center_y + pixel_y // 2)
    
    cv2.rectangle(img, top_left, bottom_right, (255,255,255), -1)
    
    # Kaydet ve göster
    cv2.imwrite("output_gui.png", img)
    cv2.imshow("Insan Dikdortgen", img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

# ---------------- GUI ----------------
root = tk.Tk()
root.title("Drone İnsan Görüntü Hesaplama")

# Etiketler ve giriş kutuları
tk.Label(root, text="Çözünürlük X:").grid(row=0, column=0)
entry_res_x = tk.Entry(root)
entry_res_x.grid(row=0, column=1)
entry_res_x.insert(0, "1920")

tk.Label(root, text="Çözünürlük Y:").grid(row=1, column=0)
entry_res_y = tk.Entry(root)
entry_res_y.grid(row=1, column=1)
entry_res_y.insert(0, "1080")

tk.Label(root, text="Drone yüksekliği (m):").grid(row=2, column=0)
entry_h = tk.Entry(root)
entry_h.grid(row=2, column=1)
entry_h.insert(0, "50")

tk.Label(root, text="FOV X (°):").grid(row=3, column=0)
entry_fov_x = tk.Entry(root)
entry_fov_x.grid(row=3, column=1)
entry_fov_x.insert(0, "60")

tk.Label(root, text="FOV Y (°):").grid(row=4, column=0)
entry_fov_y = tk.Entry(root)
entry_fov_y.grid(row=4, column=1)
entry_fov_y.insert(0, "36")

tk.Label(root, text="İnsan en (m):").grid(row=5, column=0)
entry_en = tk.Entry(root)
entry_en.grid(row=5, column=1)
entry_en.insert(0, "0.5")

tk.Label(root, text="İnsan boy (m):").grid(row=6, column=0)
entry_boy = tk.Entry(root)
entry_boy.grid(row=6, column=1)
entry_boy.insert(0, "1.7")

# Oluştur butonu
tk.Button(root, text="Oluştur", command=olustur).grid(row=7, column=0, columnspan=2)

root.mainloop()

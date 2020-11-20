import os
import time


while True:
    try:
        os.system('cls' if os.name == 'nt' else 'clear')
       
        print("===== Program Pengulangan NIM =====")
        NIM = int(input("Mohon Masukkan Nim + 10: "))
        n = 1
        m = 1
        while n <= NIM:
            print (m)
            m += 1
            if m == 10:
                m -= 9
            n += 1
        break
    except ValueError:
        print("Ups! Itu bukan nomor yang valid. Coba lagi...")
        time.sleep(1.0)

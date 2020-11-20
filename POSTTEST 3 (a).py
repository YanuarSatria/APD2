def show_menu():
	print(' ')
	print('==================')
	print('TOKO KUE KANG SULE')
	print('==================')
	print(' ')

	print('Daftar KUE Yang Sedang Promo')
	print('[1]. Kue Keju    Harga Normal Rp. 6000 (Stok:25)')
	print('[2]. Kue Coklat  Harga Normal Rp. 3500 (Stok:35)')

	kode = str(input('\nMasukkan Kode \t : '))
	if(kode == '1'):
		print('\nAnda Memilih Kue KEJU')
		jb = int(input('\nJumlah Kue\t\t : '))
		harga = 6000
		jwb = jb*harga
		if jb < 4 : disc = 0
		elif jb > 3 and jb <=15  : disc = 0.1*harga*jb
		elif jb > 15 and jb <=25 : disc = 0.15*harga*jb
		elif jb > 25 :
			print('Stok tidak Tersedia')
	elif(kode == '2'):
		print('\nAnda Memilih Kue COKLAT')
		jb = int(input('\nJumlah Kue\t\t : '))
		harga = 3500
		jwb = jb*harga
		if jb < 5 : disc = 0
		elif jb > 4 and jb <=20  : disc = 0.07*harga*jb
		elif jb > 20 and jb <=35 : disc = 0.12*harga*jb
		elif jb > 35 :
			print('Stok tidak Tersedia')

	else:
		print('\nMaaf kode yang dimasukkan tidak cocok')
		back_to_menu()
	ht = jwb - disc

	print("Harga Total Sebelum Diskon\t : Rp. ",jwb)
	print("Potongan Harga           \t : Rp. ",disc)
	print("Harga Yang Harus Di Bayar\t : Rp. ",ht)
	print(" ")
	print("==================================")
	print("           Terima Kasih           ")

def back_to_menu():
	print("\n")
	input("Tekan Enter untuk kembali...")
	show_menu()

show_menu()
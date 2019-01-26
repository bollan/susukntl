print "isi data :"

nama = raw_input("Nama  : ")
umur = input("Umur : ")
alamat = raw_input("Alamat : ")

# format teks
textnya = "Nama : {}\nUmur : {}\nAlamat : {}".format(nama, umur, alamat)
#buka file untuk ditulis

fileku = open("iniadalahfilenya.txt", "a")

#!/usr/bin/env python
# coding: utf-8

# In[96]:


import sys,shelve, pyperclip
import os

class akun :
    def __init__(self):
        self.data = []
        self.file = 'filepass'
        
        
    def liat_list(self):
        filepass = shelve.open(self.file)
        isi_key = list(filepass)
        return isi_key
        filepass.close()
        
    def baca(self):
        panggil = input("panggil key : ")
        filepass = shelve.open(self.file)
        liat = filepass[panggil]
        return liat
        filepass.close()

    def hapus(self):
        key = input("hapus key untuk dihapus : ")
        filepass = shelve.open(self.file)
        del filepass[key]
        filepass.close()

    def edit(self):
        key = input("Masukan key untuk di update : ")
        filepass = shelve.open(self.file)
        print("Kosongkan nilai jika sudah selesai")
        while True:
            values = input("masukan nilai : ")
            if values == "":
                break
            else:
                self.data.append(values)
        del filepass[key]

        filepass[key] =self.data
        filepass.close()

        self.data  = []


    def tulis_file(self):
        mode = input("'w' untuk menulis ulang, 'a' untuk menambahkan tulisan : ")
        
        if (mode=='w' or mode == 'a'):
            
            key = input('key :')
            
            print("Kosongkan nilai jika sudah selesai")
            while True:
                values = input("masukan nilai : ")
                
                if values == "":
                    break
                else:
                    self.data.append(values)
                
            
            if mode == 'w':
                filepass = shelve.open(self.file)
                
                if len(filepass) != 0:
                    filepass.clear()
                    
                filepass[key] = self.data
                print(filepass[key])
                filepass.close()
                
                
            elif mode == 'a':
                filepass = shelve.open(self.file)
                filepass[key] = self.data
                print(filepass[key])
    #             filepass.write("{}".format(self.data))
                filepass.close()

            self.data = []
            
        else :
            print(mode== 'w')
            print("ikutin perintah!!!")
            sys.exit()
        filepass.close()

excute = akun()


if (len(sys.argv) == 1):
	print("Silahkan ikutin Peritah")
	print('''
        ada function :

        "liat_list = l", 
        "baca = b", 
        "tulis_file = t",
        "hapus 1 key = d"
        "update 1 key = u"

        ''')

elif (len(sys.argv) == 2):
	if (sys.argv[1] == 'l'):
		print(excute.liat_list())
	elif (sys.argv[1] == 'b'):
		print(excute.baca())
	elif (sys.argv[1] == 't'):
		excute.tulis_file()
	elif (sys.argv[1] == 'd'):
		excute.hapus()
	elif (sys.argv[1] == 'u'):
		excute.edit()
	else:
		print("Ikutin Perintah!!!")
		sys.exit()

else:
	print('list jangan lebih dari 2')
	print('jumlah list ada', len(sys.argv))

# In[ ]:





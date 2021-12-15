#!/usr/bin/env python
# coding: utf-8

# In[22]:


import sys

class bentuk:
    def __init__(self, jumlah):
        self.jumlah = jumlah
    
    def  segitiga_siku_siku(self):
    	for i in range(1, self.jumlah):
        	print('x'*i)
    	print()

    def segitiga_sama_kaki(self):	
        for i in range(self.jumlah, 0,-1):
            print(' '*i, end='')
            print('x'*(self.jumlah-i-1),end='')
            print('x'*(self.jumlah-i))
        print()
          
    def tampil(self):
    	print('---segitiga_siku_siku---')
    	self.segitiga_siku_siku()
    	print('---segitiga_sama_kaki---')
    	self.segitiga_sama_kaki()

creat = bentuk(int(sys.argv[1]))
# creat.segitiga_siku_siku()
creat.tampil()


# In[23]:


# panggil = bentuk(5)


# In[24]:


# panggil.segitiga_siku_siku()


# In[ ]:





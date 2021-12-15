#!/usr/bin/env python
# coding: utf-8

# In[12]:


#! python3
# pw.py - An insecure password locker program.
PASSWORDS = {'email1': 'koerniazoleda31@gmail.com ulda1234',
 'email2': 'koerzoelmatondang 20ELD@890',
 'VALORANT1': 'KAZUMA31300, ulda1234',
 'VALORANT2': 'WARRIOR31300 , ulda1234'}


# In[13]:


PASSWORDS


# In[14]:


import sys, pyperclip
if len(sys.argv) < 2:
    print('Usage: python pw.py [account] - copy account password')
    sys.exit()

account = sys.argv[1] # first command line arg is the account name


# In[11]:


if account in PASSWORDS:
    pyperclip.copy(PASSWORDS[account])
    print('PASSWORD for '+ account + ' copied to clipboard.')
else:
    print('There is no account named '+account)


# In[ ]:





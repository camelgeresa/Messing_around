# -*- coding: utf-8 -*-

import os
current_dir = os.getcwd()
print(current_dir)

def funky_function(n):
   for x in range(n):
      print(x)
   return n+1

print('main branch only!')
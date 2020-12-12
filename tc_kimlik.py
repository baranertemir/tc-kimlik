#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Dec 12 15:23:50 2020

@author: ayca22
""" 

class tckimlik():
    
    def __init__(self,tc): 
        # Burada __init__ kullanilarak TC Kimlik numarasinin ilk 9 hanesi alinir.
        self.tc = tc
        
    def check(self):
       tc1 = self.tc
       # Onume cikabilecek hatalari engellemek adina aldigimiz TC degerini tc1 degiskenine atadim.
       
       if int(tc1[0]) != 0 and len(tc1) == 9:
           # İlk hane 0 olamaz.
           # Verilen degerin ilk hanesinin 0 olmadigindan ve 9 haneli bir deger oldugundan emin oluyorum.
           one = int(tc1[0]) + int(tc1[2]) + int(tc1[4]) + int(tc1[6]) + int(tc1[8])
           #TC kimlik numaralarımızın 1. 3. 5. 7. ve 9. hanelerinin toplamının 7 katından, 2. 4. 6. ve 8. hanelerinin toplamı çıkartıldığında, elde edilen sonucun 10'a bölümünden kalan, yani mod10'u bize 10. haneyi verir.
           # TC kimlik numarasinin 1. 3. 5. 7. ve 9. halenerini one degiskenine atiyorum.
           two = int(tc1[1]) + int(tc1[3]) + int(tc1[5]) + int(tc1[7])
           # TC kimlik numarasinin. 4. 6. ve 8. hanelerini two degiskenine atiyorum.
           
           seven = one * 7
           # 1. 3. 5. 7. ve 9. hanelerinin 7 ile carpimini seven degiskenine atadim.
           sevenn = seven - two
           # 1. 3. 5. 7. ve 9. hanelerinin 7 katindan 2. 4. 6. ve 8. hanelerinin toplamı çıkartiliyor ve sevenn degiskenine esitliyorum.
           on = sevenn % 10
           # En son olarak sevenn degiskeninin 10'a bolumunden kalani aliyoruz ve 10. hanemizi on degiskenine atiyoruz.
           
           toplam = one + two + on
           # one, two, on degiskenlerinin toplami aliniyor.
           onbir = toplam % 10
           # Toplamlarinin 10'a bolumunden son olarak 11.hanemizi elde ediyoruz.
           on1 = str(on) + str(onbir)
           # Buldugumuz 10. hane ve 11. haneyi string degerinde toplayip on1 degiskenine esitliyorum.
           return tc1+on1
           # Ilk basta aldigimiz ilk 9 haneye yaptigimiz islemler sonucu cikan son iki haneyi ekliyoruz.
           
       else:
           print("TC kimlik numarasini 9 haneli girdiginizden ve ilk hanesinin 0 olmadigindan emin olun.")

tc2 = input("TC Kimlik Numaranizin Ilk 9 Hanesi:")
tc = tckimlik(tc2)


print("TC Kimlik Numarasi:",tc.check())
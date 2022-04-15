aloma0 = {
  'ism':'Abu Abdulloh Muhammad ibn Ismoil ',
  'tyil':810,
  'tjoy':'Buxoro',
  'yashagan':60,
  'asarlari':['Al-jome as-sahih','Al-adab al-mufrad','At-tarix al-kabir','At-tarix as-sag\'ir']
         }
aloma1 = {
  'ism':'Abdulla Qodiriy',
  'tyil':1894,
  'tjoy':'Toshkent',
  'yashagan':44,
  'asarlari':['O\'tkan kunlar','Mehrobdan chayon','Obid ketmon']
         }
aloma2 = {
  'ism':'Erkin Vohidov',
  'tyil':1936,
  'tjoy':'Farh\'ona',
  'yashagan':80,
  'asarlari':['Tong nafasi','Qo\'shiqlarim sizga','O\'zbegim','Qiziquvchan Matmusa']
}
aloma3 = {
  'ism':'Alisher Navoiy',
  'tyil':1441,
  'tjoy':'Xirot',
  'yashagan':60,
  'asarlari':['Xamsa','Lison ut-Tayr','Mahbub Al-Qulub','Munojat']
}
alomalar = [aloma0, aloma1, aloma2, aloma3]
for shaxs in alomalar:
  print(f"{shaxs['ism']} {shaxs['tyil']}-yil {shaxs['tjoy']}da tavalud topgan, {shaxs['yashagan']} umir ko'rgan.")

for aloma in alomalar:
 ism = aloma['ism']
 asarlari= aloma['asarlari']
 print(f"{ism}ning asarlari:")
 for asar in asarlari:
       print(asar)  

   
    

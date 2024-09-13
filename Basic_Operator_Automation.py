#23100011020
#MUSTAFA SATI TUTKUN
#BAHAR DONEMI FINAL PROJESI
import datetime
import os
clients = {}
ids = []
paketler = {
    1: {"Konusma": 500, "SMS": 250, "Internet": 5, "Fiyat": 80, "IndirimOran": 0.05, "PuanArtirim":40},
    2: {"Konusma": 750, "SMS": 250, "Internet": 10, "Fiyat": 120, "IndirimOran": 0.08, "PuanArtirim":50},
    3: {"Konusma": 500, "SMS": 500, "Internet": 15, "Fiyat": 150,"IndirimOran": 0.1, "PuanArtirim":75},
    4: {"Konusma": 750, "SMS": 750, "Internet": 20, "Fiyat": 180, "IndirimOran": 0.15, "PuanArtirim":90},
    5: {"Konusma": 1000, "SMS": 1000, "Internet": 25, "Fiyat": 250, "IndirimOran": 0.2, "PuanArtirim":100}
}

def musteriekle():
   while True:
    musterid = input("Lutfen musteri ID giriniz: ")
    try:
      musterid=int(musterid)
    except ValueError:
      print("MUSTERI ID SAYILARDAN OLUSMALI!")
      continue
    if musterid in ids:
        print("Bu ID zaten var.")
        continue
    ids.append(musterid)
    clients[musterid] = {}
    ad = input("Musteri ad giriniz: ")
    soyad = input("Musteri soyad giriniz: ")
    katilmayili = datetime.datetime.today().year
    while True:
     paket = input("Paket tipini seciniz (1-5): ")
     if paket not in "12345":
         print("Gecersiz paket secimi!")
         continue
     else:
         paket=int(paket)
         break

    clients[musterid]["Ad"] = ad.upper()
    clients[musterid]["Soyad"] = soyad.upper()
    clients[musterid]["Katilmayili"] = katilmayili
    clients[musterid]["Pakettipi"] = paket
    clients[musterid]["Faturafiyat"]=paketler[clients[musterid]["Pakettipi"]]["Fiyat"]
    clients[musterid]["Puan"]=0
    print("Musteri eklendi.")
    print("MENU'ye donuluyor...")
    break

def musteriarama():
   while True:
    arananid=input("Lutfen musteri ID giriniz: ")
    try:
     arananid=int(arananid)
    except ValueError:
     print("MUSTERI ID SAYILARDAN OLUSMALI!")
     continue
    if arananid in ids:
     print("-MUSTERI BILGILERI-")
     print("AD: {}".format(clients[arananid]["Ad"]))
     print("SOYAD: {}".format(clients[arananid]["Soyad"]))
     print("KATILMA YILI: {}".format(clients[arananid]["Katilmayili"]))
     print("-PAKET BILGILERI-")
     pakettipi = clients[arananid]["Pakettipi"]
     print("PAKET TİPİ: {}".format(pakettipi))
     print("KONUSMA: {} DK".format(paketler[pakettipi]["Konusma"]))
     print("SMS: {} TANE".format(paketler[pakettipi]["SMS"]))
     print("INTERNET: {} GB".format(paketler[pakettipi]["Internet"]))
     print("FATURA FIYATI: {} TL".format(paketler[clients[arananid]["Pakettipi"]]["Fiyat"]))
     print("MENU'ye donuluyor...")

    else:
      print("Musteri bulunamadi.")
      print("MENU'ye donuluyor...")

    break




def guncelleme():
  while True:
   guncellenenid=input("Lutfen musteri ID giriniz:")
   try:
    guncellenenid=int(guncellenenid)
   except ValueError:
    print("MUSTERI ID SAYILARDAN OLUSMALI!")
    continue
   if guncellenenid in ids:
        pakettipi = clients[guncellenenid]["Pakettipi"]
        print("PAKET TİPİ: {}".format(pakettipi))
        print("KONUŞMA: {} DK".format(paketler[pakettipi]["Konusma"]))
        print("SMS: {} TANE".format(paketler[pakettipi]["SMS"]))
        print("INTERNET: {} GB".format(paketler[pakettipi]["Internet"]))
        print("FATURA FİYATI: {} TL".format(clients[guncellenenid]["Faturafiyat"]))
        while True:
          pakettemp=input("Yeni paket tipini giriniz:")
          if pakettemp not in "12345" or len(pakettemp)>1:
            print("Gecersiz paket secimi!")
            continue
          else:
            pakettemp=int(pakettemp)
            clients[guncellenenid]["Pakettipi"]=pakettemp
            clients[guncellenenid]["FaturaFiyat"]=paketler[clients[guncellenenid]["Pakettipi"]]["Fiyat"]
            print("Musteri paket tipi guncellendi.")
            break

   else:
       print("Musteri bulunamadi.")
       print("MENU'ye donuluyor...")

   break

def musterisilme():
   while True:
    silinecekid=input("Lutfen musteri ID giriniz:")
    try:
     silinecekid=int(silinecekid)
    except ValueError:
     print("MUSTERI ID SAYILARDAN OLUSMALI!")
     continue
    if silinecekid in ids:
        del clients[silinecekid]
        ids.remove(silinecekid)
        print("Musteri silindi.")
        print("MENU'ye donuluyor...")
    else:
       print("Musteri bulunamadi.")
       print("MENU'ye donuluyor...")
    break


def faturapuanhesap():
    print("Her yeni yilda faturalarda müdavim indirimi uygulanir.Indirim oranlari paketlere gore degismektedir.")
    print("Sistem indirimli faturalari hesaplayip musteri paket bilgilerine aktaracaktir.")
    def indirimlifaturavepuan(indirimid):
        year=int(datetime.datetime.today().year)-clients[indirimid]["Katilmayili"]
        if year>0:
          indirim=paketler[clients[indirimid]["Pakettipi"]]["Fiyat"]*paketler[clients[indirimid]["Pakettipi"]]["IndirimOran"]
          yenifatura=paketler[clients[indirimid]["Pakettipi"]]["Fiyat"]-indirim
          clients[indirimid]["Puan"]+=paketler[clients[indirimid]["Pakettipi"]]["PuanArtirim"]
        else:
          yenifatura = paketler[clients[indirimid]["Pakettipi"]]["Fiyat"]
        return yenifatura


    for faturaid in clients.keys():
        clients[faturaid]["Faturafiyat"]=indirimlifaturavepuan(faturaid)
    print("Butun faturalar hesaplandi ve sistemde degistirildi.")
    print("MENU'ye donuluyor...")

def hediyekulakliksorgu():
   while True:
    hediyesorguid=input("Lutfen musteri ID giriniz:")
    try:
        hediyesorguid=int(hediyesorguid)
    except ValueError:
        print("MUSTERI ID SAYILARDAN OLUSMALI!")
        continue
    if hediyesorguid in ids:
     if clients[hediyesorguid]["Puan"]>=200:
         print("BU MUSTERI HEDIYE KULAKLIK ALMA HAKKI KAZANMIS.")
         hediyesecim=input("Kulaklik hediyesi alinacak mi?(E/H):")
         if hediyesecim=='E' or hediyesecim=='e':
             clients[hediyesorguid]["Puan"]-=200
         print("Islem tamamlandi.")
     else:
         print("BU MUSTERININ HEDIYE KULAKLIK ALMA HAKKI YOKTUR.ŞU ANKI PUANI: {}".format(clients[hediyesorguid]["Puan"]))
     print("MENU'ye donuluyor...")
     break
    else:
        print("Musteri bulunamadi.")
        print("MENU'ye donuluyor...")
        break

def verileri_kaydet(dosya_adi):
    with open(dosya_adi, "w") as dosya:
        dosya.write("TTKN OPERATOR A.S."+"\n"+"\n"+"ID"+"\t"+"\t"+"AD"+"\t"+"\t"+"SOYAD"+"\t"+"\t"+"KATILMA YILI"+"\t"+"\t"+"PAKET TIPI"+"\t"+"\t"+"PUAN"+"\n"+"\n"+"\n")
        for key in clients.keys():
         print(key,"\t",clients[key]["Ad"],"\t",clients[key]["Soyad"],"\t",clients[key]["Katilmayili"],"\t","\t",clients[key]["Pakettipi"],"\t","\t",clients[key]["Puan"],"\n",file=dosya,end="\n")


def controlmenu():
 dosyaadi="23100011020.txt"
 while True:
  print("--TUTKUN OPERATOR A.S.--")
  print("-CALISAN ARAYUZU-")
  print("MUSTERI SISTEMI(EKLEME,ARAMA,GUNCELLEME VB. ISLEMLER)(1)")
  print("PAKETLER(TARIFELER) HAKKINDA BILGILER(2)")
  print("ARAYUZDEN CIKIS(3)")
  sistemsecim=input("Hangi islemi yapacaksiniz?:")
  try:
   sistemsecim=int(sistemsecim)
  except ValueError:
   print("ISLEM SECIMI RAKAM OLMALI!")
   continue
  except BaseException:
   print("Bilinmeyen bir hata olustu,program yeniden baslatiliyor...")
   continue
  if sistemsecim==1:
   while True:
     verileri_kaydet(dosyaadi)
     print("MUSTERI EKLEME(1)")
     print("MUSTERİ ARAMA(2)")
     print("MUSTERİ PAKET GUNCELLEME(3)")
     print("MUSTERI SILME(4)")
     print("HEDIYE KULAKLIK SORGUSU(5)")
     print("INDIRIM VE PUAN HESABI(6)")
     print("ARAYUZUNE DON(7)")
     menusecim=input("Yapilacak islemi seciniz: ")
     try:
        menusecim=int(menusecim)
     except ValueError:
        print("ISLEM SECIMI RAKAM OLMALI!")
        continue
     except BaseException:
        print("Bilinmeyen bir hata olustu,basa donuluyor...")
        continue
     if menusecim==1:
        musteriekle()
     elif menusecim==2:
        musteriarama()
     elif menusecim==3:
        guncelleme()
     elif menusecim==4:
        musterisilme()
     elif menusecim==5:
        hediyekulakliksorgu()
     elif menusecim==6:
        faturapuanhesap()
     elif menusecim==7:
        print("Arayuzune donuluyor...")
        break
     else:
        print("Gecersiz secenek sectiniz!")
  elif sistemsecim==2:
    while True:
     print("----------------TARİFELER----------------")
     print("!ÖNEMLİ NOTLAR!")
     print("LÜTFEN BU TARİFELERİ VE PAKET BİLGİLERİNİ MÜŞTERİYE AYRINTILI BİR ŞEKİLDE SUNUN.")
     print("FİYATLAR AYLIKTIR.")
     print("MÜŞTERİ TARİFE DEĞİŞTİRDİĞİNDE O AY İLK TARİFE FİYATI DİĞER AY İSE SONRAKİ TARİFE FİYATI İLE FATURALANDIRILIR.")
     print("İNDİRİM ORANI HER YENİ YILDA UYGULANAN İNDİRİMDİR MİKTARIDIR.ANCAK FATURA FİYATLARI ZAMLANABİLİR.")
     print("PUAN ARTIRIM HER YENİ YILDA MÜŞTERİ PUANININ ARTIRIM MİKTARIDIR.(200 PUANDA 1 KULAKLIK ALMA HAKKI KAZANILIR.")
     print("!PROGRAMDAN ÇIKARSANIZ PROGRAM YENİDEN BAŞLATILDIĞINDA ESKİ VERİLER SİLİNİR!(ESKİ VERİLER YEDEKLENİLSE BİLE ONLAR ÜZERİNDE BU PROGRAM İLE DEĞİŞİM YAPILAMAZ.)")
     print("TARİFE 1")
     print("Özellikler""\n"
           "Konuşma Süresi: 500 dakika""\n"
           "SMS: 250 mesaj""\n"
            "İnternet: 5 GB""\n"
            "Fiyat: 80 TL""\n"
            "İndirim Oranı: %5""\n"
             "Puan Artirim: 40")
     print("Bu tarife, orta seviyede konuşma ve mesajlaşma ihtiyaçları olan kullanıcılar için idealdir.5 GB internet paketiyle basit internet ihtiyacı karşılanabilir.")
     print("\n")
     print("TARİFE 2")
     print("Özellikler""\n"
           "Konuşma Süresi: 750 dakika""\n"
           "SMS: 250 mesaj""\n"
           "İnternet: 10 GB""\n"
           "Fiyat: 120 TL""\n"
           "İndirim Oranı: %8""\n"
           "Puan Artirim: 50")
     print("Daha fazla konuşma süresi ve internet kullanımı arayan kullanıcılar için uygundur.")
     print("\n")
     print("TARİFE 3")
     print("Özellikler""\n"
           "Konuşma Süresi: 500 dakika""\n"
           "SMS: 500 mesaj""\n"
           "İnternet: 15 GB""\n"
           "Fiyat: 150 TL""\n"
           "İndirim Oranı: %10""\n"
           "Puan Artirim: 75")
     print("Hem konuşma hem de mesajlaşma konusunda yüksek ihtiyaçları olan kullanıcılar için tasarlanmıştır.15 GB internet paketi,yoğun internet kullanıcıları için idealdir.")
     print("\n")
     print("TARİFE 4")
     print("Özellikler""\n"
           "Konuşma Süresi: 750 dakika""\n"
           "SMS: 750 mesaj""\n"
           "İnternet: 20 GB""\n"
           "Fiyat: 180 TL""\n"
           "İndirim Oranı: %15""\n"
            "Puan Artirim: 90")
     print("Konuşma, mesajlaşma ve internet kullanımında yüksek ihtiyaçları olan kullanıcılar için en uygun tarifelerden biridir.20 GB internet paketi ile geniş bir kullanım alanı sağlar.")
     print("\n")
     print("TARİFE 5")
     print("Özellikler""\n"
           "Konuşma Süresi: 1000 dakika""\n"
           "SMS: 1000 mesaj""\n"
           "İnternet: 25 GB""\n"
           "Fiyat: 250 TL""\n"
           "İndirim Oranı: %20""\n"
           "Puan Artirim: 100")
     print("En yüksek konuşma, mesajlaşma ve internet kullanımını içeren bu tarife,yoğun kullanıcılar için tasarlanmıştır.25 GB internet paketi ile her türlü internet ihtiyacı karşılanabilir.")
     print("\n")
     print("-----------TTKN OPERATOR A.Ş.-----------")
     print("\n")
     while True:
      donuscntrol=0
      menuyedonus=input("MENU'ye donmek istiyor musunuz?(E/H):")
      if menuyedonus=='E' or menuyedonus=='e':
         donuscntrol=1
         break
      elif menuyedonus=='H' or menuyedonus=='h':
         break
      else:
         print("Gecersiz secenek sectiniz!")
     os.system("cls")
     if donuscntrol==1:
         break

  elif sistemsecim==3:
      while True:
        cikiscntrol=0
        cikmasecim=input("Programdan cikilisin mi?(E/H):")
        if cikmasecim=='E' or cikmasecim=='e':
            cikiscntrol=1
            break
        elif cikmasecim=='H' or cikmasecim=='h':
            break
        else:
           print("Gecersiz secenek sectiniz!")
      if cikiscntrol==1:
       print("PROGRAMDAN CIKILIYOR...")
       break
  else:
     print("GECERSIZ SECENEK SECTINIZ!")

controlmenu()
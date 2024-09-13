# Basic_Operator_Automation
a basic operator automation with Python programming language
-------------------------------------------------------------------------------------------------------------
Bu proje küçük-orta telefon operatörleri için hazırlanmıştır. 
İçinde belirli fonksiyonlar olan bazı işlemleri yerine getirebilen bir programdır. 
Fonksiyonlar, sınırlar ve gereksinimler aşağıdaki gibidir: 
Müşteri Ekleme: 
ID, ad, soyad ve seçilen paket tipini alır ve kaydeder. 
Müşteri Arama: 
ID alarak müşteri ve paket bilgilerini yazar.  
Müşteri Silme: 
ID alarak o ID’ deki müşterinin kaydını siler. 
Güncelleme: 
ID alır, o ID’ deki müşterinin paket bilgisini yazdırır ve girilen paket tipine göre müşteri paket 
tipini değiştirir. 
Fatura ve puan hesabı: 
Müşterilere paket tipine göre her yeni yıl fatura indirimi ve puan artırımı yapılır. İndirimli 
fatura ve artırılmış güncel puan kaydedilir. (2023 Aralık’ta kaydolan birisi 2024 yılında indirim 
alabilir. Her yeni yıl indirim miktarı artar. İndirim yılda bir seferlik değildir.) 
DİKKAT!  
Bu işlem sadece her yeni yılda sadece 1 kere yapılmalıdır. Yoksa fazladan indirim yapılabilir. 
Hediye kulaklık sorgusu: 
Müşteri puanı 200’ e ulaştığında 1 hediye kulaklık alma hakkı kazanır. Bu durumun 
sorgulanması için bir fonksiyondur. ID alınır puanı 200’ü geçiyorsa belirtilir. Kulaklık alınırsa 
puanından 200 puan azaltılır. 
Verileri kaydetme: 
Bu fonksiyon her işlem yapıldığında gerekli verileri “MUSTERILER.txt” adlı dosyaya kaydeder 
ve güncellenmiş verileri tekrardan yazar.
----------------------------------------------------------------------------------------------------------------
This project is prepared for small-medium telephone operators.
It is a program that can perform some operations in certain functions.
Functions, quantities and features are as follows:
Adding Customer: 
Gets ID, advertisement, surname and selected package type and becomes a member.
Searching for Customer: 
Gets ID and writes customer and package information.
Delete Customer: 
It takes an ID and deletes the customer's record with that ID.
Update: 
Gets ID, prints package information on that ID and changes customer package type according to the entered package type.
Invoice and points account: 
Customers are given invoice discount and point increase every new year according to package type. Discounted invoice and increased current points are shown. (Someone who registered in December 2023 can get a discount in 2024. The discount amount increases every new year. The discount is not a one-time annual discount.) 
Attention!
This operation should be done only once every new year. Otherwise, additional discounts may be applied.
Gift headphone query: 
When the payment points reach 200, they gain the right to receive 1 gift headphone. This is a function for querying this situation. If the ID is taken, the score is indicated as 200. If the headset is taken, the score is reduced by 200 points. 
Saving data: 
This function saves the necessary data for each transaction to the file named “MUSTERILER.txt” and rewrites the updated data.

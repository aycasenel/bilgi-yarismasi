#bilgileri depolamak için bir uygulama oluşturun
#kütüphaneleri import edelim
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import*

class Question():
    def __init__(self,g_soru,g_dogru_cvp,g_yanlis1,g_yanlis2,g_yanlis3):
        self.soru = g_soru
        self.dogru_cvp = g_dogru_cvp
        self.yanlis1 = g_yanlis1
        self.yanlis2 = g_yanlis2
        self.yanlis3 = g_yanlis3


uygulamam = QApplication([])

pencerem = QWidget()
pencerem.setWindowTitle("Bilgi Yarışması")
pencerem.resize(400,400)
pencerem.show()

# gerekli widgetları oluşturalım
soru_label = QLabel("İstanbul kaç yılında fethedilmiştir?")
cevapla_butonu = QPushButton("Cevapla")

# seçenekleri oluşturalım
GroupBox = QGroupBox("Cevap Seçenekleri")

rbtn_1 = QRadioButton("1923")
rbtn_2 = QRadioButton("1453")
rbtn_3 = QRadioButton("1071")
rbtn_4 = QRadioButton("1845")

# Group Box Konumlandırması
secenek_sutun_1 = QVBoxLayout()
secenek_sutun_2 = QVBoxLayout()

secenek_yatay_genel = QHBoxLayout()

secenek_sutun_1.addWidget(rbtn_1)
secenek_sutun_1.addWidget(rbtn_2)

secenek_sutun_2.addWidget(rbtn_3)
secenek_sutun_2.addWidget(rbtn_4)

secenek_yatay_genel.addLayout(secenek_sutun_1)
secenek_yatay_genel.addLayout(secenek_sutun_2)

GroupBox.setLayout(secenek_yatay_genel)

#Cevap formunun (Group Baox ının) oluşturulması
#GroupBox.hide()

cevap_etiketi = QLabel("Doğru / Yanlış")
dogru_cevap_etiketi = QLabel("Doğru cevap burada gözükecek")

#doğru cevap grupbax ı oluşturalım
DogruGroupBox = QGroupBox("Test Sonucu")

cevap_konumu = QVBoxLayout()
cevap_konumu.addWidget(cevap_etiketi, alignment=Qt.AlignLeft)
cevap_konumu.addWidget(dogru_cevap_etiketi, alignment=Qt.AlignCenter)

DogruGroupBox.setLayout(cevap_konumu)

# widgetları konumlandırma
soru_konumu = QHBoxLayout()
groupBox_konumu = QHBoxLayout()
buton_konumu = QHBoxLayout()

soru_konumu.addWidget(soru_label,alignment=Qt.AlignCenter)
groupBox_konumu.addWidget(GroupBox)
#yeni oluşturulan doğru cevap gruop boxı konumlandırma
groupBox_konumu.addWidget(DogruGroupBox)
buton_konumu.addWidget(cevapla_butonu,alignment=Qt.AlignCenter)

dikey_konumla = QVBoxLayout()

dikey_konumla.addLayout(soru_konumu)
dikey_konumla.addLayout(groupBox_konumu)
dikey_konumla.addLayout(buton_konumu)

pencerem.setLayout(dikey_konumla)
#-----------------------------

RadioGroup = QButtonGroup()
RadioGroup.addButton(rbtn_1)
RadioGroup.addButton(rbtn_2)
RadioGroup.addButton(rbtn_3)
RadioGroup.addButton(rbtn_4)

DogruGroupBox.hide()
def cevabi_goster():
    #soru formu gizlenecek
    GroupBox.hide()
    #cevap formu gösterilecek
    DogruGroupBox.show()
    #Buton üzerindeki yazı değişecek
    cevapla_butonu.setText("Sonraki Soru")

def sonraki_soruyu_goster():
    DogruGroupBox.hide()
    GroupBox.show()
    cevapla_butonu.setText("Cevapla")

    RadioGroup.setExclusive(False)
    rbtn_1.setChecked(False)
    rbtn_2.setChecked(False)
    rbtn_3.setChecked(False)
    rbtn_4.setChecked(False)
    RadioGroup.setExclusive(True)

#Doğru - Yanlış kontrolü 

def kontrol_et():
    global dogru_cevap_sayisi
    if radio_buton_listesi[0].isChecked():
        cevap_etiketi.setText("Tebrikler. Doğru!")
        cevabi_goster()

        dogru_cevap_sayisi += 1
        print("İstatistik:")
        print("Toplam Soru:",soru_sayisi)
        print("Doğru cevap saysı:",dogru_cevap_sayisi)
        print("şuanki puanınız:",(dogru_cevap_sayisi/soru_sayisi)*100)

    else:
        cevap_etiketi.setText("Cevabınız Yanlış!")
        cevabi_goster()
        print("şuanki puanınız:",(dogru_cevap_sayisi/soru_sayisi)*100)



from random import shuffle
radio_buton_listesi = [rbtn_1,rbtn_2,rbtn_3,rbtn_4]
#[rbtn_3,rbtn_4,rbtn_1,rbtn_2]
def soru_sor(s : Question):
    soru_label.setText(s.soru)
    shuffle(radio_buton_listesi)
    radio_buton_listesi[0].setText(s.dogru_cvp)
    radio_buton_listesi[1].setText(s.yanlis1)
    radio_buton_listesi[2].setText(s.yanlis2)
    radio_buton_listesi[3].setText(s.yanlis3)
    dogru_cevap_etiketi.setText(s.dogru_cvp)
    sonraki_soruyu_goster()

#soru_sor
soru1 = Question("Türkiye'nin Başkenti Neresi ?","Ankara","İzmir","Bursa","İStanbul")
soru_listesi = []
soru_listesi.append(soru1)
soru2 = Question("Ankara'nın nüfusu kaç?","6 milyon","1 milyon","10 milyon","20 milyon")
soru_listesi.append(soru2)
soru3 = Question("Kaç mevsim var ?","4","5","6","7")
soru_listesi.append(soru3)
soru4 = Question("-fe- hangi elementin sembolüdür?","demir","bakır","altın","gümüş")
soru_listesi.append(soru4)
soru5 = Question("Türkiye'nin yüzölçümü en büyük komşusu hangisidir?","İran","Suriye","Bulgaristan","Azerbaycan")
soru_listesi.append(soru5)
soru6 = Question("Dünyanın en büyük okyanusu hangisidir?","Pasifik Okyanusu","Hint Okyanusu","Atlantik Okyanusu","Arktik Okyanusu")
soru_listesi.append(soru6)
soru7 = Question("Romen Rakamında Hangi Sayı Yoktur?","0","50","100","1000")
soru_listesi.append(soru7)
soru8 = Question("Aspirinin hammmaddesi nedir?","Söğüt","Köknar","Kavak","Meşe")
soru_listesi.append(soru8)
soru9 = Question("Kaç yılda bir şubat ayı 29 çeker?","4","3","2","5")
soru_listesi.append(soru9)
soru10 = Question("Dünyanın en uzun nehrinin adı nedir?","Amazon nehri","Nil nehri","Kongo nehri","Tuna nehri")
soru_listesi.append(soru10)



#soru listesindeki sorulara ulaşmak için kullanılacak değişken
soru_sayaci = -1

def siradaki_soru():
    global soru_sayaci

    global soru_sayisi

    soru_sayisi += 1
    print("İstatistik:")
    print("Toplam Soru:",soru_sayisi)
    print("Doğru cevap saysı:",dogru_cevap_sayisi)

    soru_sayaci = soru_sayaci + 1 # soru_sayaci = 0
    if soru_sayaci >= len(soru_listesi):
        soru_sayaci = 0
    soru = soru_listesi[soru_sayaci]
    soru_sor(soru)

def butona_tikla():
    if cevapla_butonu.text() == "Cevapla":
        kontrol_et()
    else:
        siradaki_soru()

#23 OCak 2022 dersi
#puan hesaplaması yapılacak
soru_sayisi = 0 # sorulan soruları sayacak
dogru_cevap_sayisi = 0 # verilen doğru yanıtları sayacak

siradaki_soru()
cevapla_butonu.clicked.connect(butona_tikla)
uygulamam.exec_()


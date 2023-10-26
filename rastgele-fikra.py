import random

# Kendi fıkralarınızı burada liste olarak tanımlayın
fikralar = [
    "Adam, papağanını gümrükten kolayca geçirebilmek amacıyla bir kutuya koymuş. Kutunun üstüne de “Kırılacak eşya” diye not düşmüştür. Gümrük memuru eşyayı kontrol etmek için şöyle bir sallar; Papağan; Şangur şungur.. Şangur şungur…",
    "Bir gün, Bir mecliste konuşulurken, Amerikalı  : -Biz Mars'a gideceğiz, demiş. Alman : -Biz yakıtsız giden otomobil üreteceğiz, demiş. Fransız : -Atom bombasını etkisiz hale getirecek projelerimiz var, demiş. Bizim Karadenizli de onlardan geri kalmamak için : -Biz de güneşe gideceğiz, demiş. -Güneşe gidemezsiniz, demişler. Güneş yakar. Karadenizli gülümsemiş : -O kadar da enayi değiliz, tabi, demiş. Akşam serinliğinde gideceğiz.",
    "Temelle Dursun ormanda yürüyorlar.Bir ara Temel Dursuna sesleniyor : -Dursun ormanın güzelliğine bak. Dursun: -Ağaçlardan göremiyorumki. ",]

# Rastgele bir fıkra seçin
secilen_fikra = random.choice(fikralar)

# Seçilen fıkrayı ekrana yazdırın
print(secilen_fikra)
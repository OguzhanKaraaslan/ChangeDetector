

## Change Detector (via Twitter API) 


Merhaba, öncelikle neden böyle bir uygulama yapma ihtiyacı hissettim ondan bahsetmek istiyorum :) Yaklaşık bir sene önce *Kennedy Lugar Youth Exchange and Study* adlı lise düzeyinde bir yurtdışı değişim programından haberim oldu. Fakat maalesef başvuru tarihini çoktan kaçırmıştım. Belki de bu benim bir seneme mâl olmuş olabilir :) Yaklaşık birkaç gün önce her zamanki gibi sitenin duyurular kısmına göz atarken böyle küçük bir şey yazmayı düşündüm. ( Ayrıca arkadaşların XSS zafiyeti nedir? zafiyeti nasıl önleriz? konularına daha çok ilgi göstermeleri gerektiğini söylemeden geçmek istemiyorum :) )  Benim en azından dile alışma sürecimde (gerek syntax, gerek temel yapılar) bu küçük aracın iyi rol oynadığını düşünüyorum :)
  
### Kullanıma Geçmeden Önce ###

Arkadaşlar, değişikleri kendime mail atması haricinde   (telnet veya smtp kullanmanın dışında) farklı bir şey yapmasını istiyordum. Bunun için aklıma ilk olarak tabiki de sosyal medyayı kullanmak geldi.  Twitter'ı  daha aktif kullandığım için Twitter'ı tercih ettim. Crontab kullanarak programı belirli süreler içerisinde çalıştırıyorum. Böylece sizde kendi kullandığınız Twitter hesabınıza göndereceğiniz direkt mesaj veya mention ile bu değişikliği ve ayrıca bu izlediğiniz url in screenshotunu tweet halinde görebileceksiniz. Küçük aracımız bir Twitter API kullanmakta. Doğal olarak twitter hesabınızla bir uygulama yaratmanız gerekmekte. 

**Bunun için öncelikle:**

- Ayrı bir twitter hesabı açıp kullanmanızı kesinlikle tavsiye ederim. Böylece kendi timelineımıza kendimiz düşmemiş oluruz :)

- [https://apps.twitter.com/app/new](https://apps.twitter.com/app/new "Twitter Application Management ") kısmından uygulamamızı yaratıyoruz.

- Consumer Keylerimizi ve Access Tokenlarımızı ilgili yere yazıyoruz. 


### Crontab ile Zamanlama ###



**Cron**, biz **Linux** ve **Unix** kullanıcılarına komutlarımızı veya scriptlerimizi belirlediğimiz tarih ve zamanda çalıştırmamıza olanak sağlıyor. Yani periyodik olarak kullanabiliyoruz. Genellikle sysadminler kullanmakta. Peki ne için kullanıyorlar; bir diskin **yedeğini almak** veya **/tmp/ dizinini temizlemek** vs. işler için. Cron daemon'u arkaplanda **/etc/cron/*** dizinleri ile çalışmakta ve ayrıca **/var/spool/cron/** dizinini de kontrol etmekte. 

Peki biz nasıl kullanacağız? Crontab dosyası kişiselleştirilmek için beş alana ayrılmış durumda. Yani aslında bu sizin biraz keyfinize kalıyor :) Aşağıdaki resim bu konuda yardımcı olabilir.

[CrontabSyntax](http://i.imgur.com/68YFfrW.png)

*Eğer resim gözükmüyorsa; resmi imgur'a upload ettim.. evet.. Arkadaşlar özgürlüklerin kısıtlandığı ülkemizde en azından bir vpn kurmayı öğrenmeniz sizin için faydalı olacaktır. "**user --> vpn (1) ---> tor network --> vpn (2) --> destination*"  ---> *Sizden kimse böyle bir şey beklemiyor :)* *Ayrıca DigitalOcean VPS +1*

Evet, kaldığımız yerden devam edelim.
	
- **Linux kullanıcıları için**

`export EDITOR=vim`
:ile crontab dosyamızı açacağımız editörümüzü belirleyebiliriz. Tabiki unutmadan **'vim rocks! :)'**
    
`crontab -e `
: Crontab dosyamızı düzenleyebiliriz. Eğer crontab dosyamız yoksa crontab dosyamızı yaratır.

`crontab -l`
: Crontab dosyamızı gösterir.

crontab -r
: Crontab dosyamızı silmemize yarar.

   ` crontab -v`
: Crontab dosyamızın son düzenlenmiş zamanını gösterir.

**Crontab Örneği**

Ben okula gitmek için 5.30 da uyanıyorum. Onun için aşağıdaki gibi bir satırım var.


    20 5 * * * /calıstıracagınız/dosyanın/relative/pathi.py
 Yani her sabah 5.20 de Twitter bildirimi gelmiş oluyor.

Yukarıda **sysadmin**ler tarafından **/tmp/ dizini**nin temizlendiğinden bahsetmiştim. (Bunlaarrrr tmp dizinini temizledileerrr :) ) Buna da örnek vererek crontab yazmayı pekiştirelim.

    59 23 28 * 1 rm /home/someuser/tmp/*

*"Her ayın pazartesi günlerinde ve 28'inde tmp dosyalarını silmektedir.*



**Gelelim şu an ki kullanımlarımdan birine :)**

[![İnceMemed](http://i.hizliresim.com/0D0q5R.png)](http://hizliresim.com/0D0q5R)



 

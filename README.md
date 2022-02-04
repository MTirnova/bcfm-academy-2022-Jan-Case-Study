# bcfm-academy-2022-Jan-Case-Study
## Dockerfile Dosyası Oluşturumu ve Açıklaması
Geliştirmiş olduğum uygulamayı containerize etmek için ilk olarak Dockerfile dosyası oluşturdum. Bu dosyayı oluştururken 6 farklı talimat kullandım. İlk kullandığım talimat "FROM" talimatıdır. Bu talimat sayesinde uygulamamın çalışacağı ortamın offical image dosyasını DockerHub üzerinden çekiyorum. Akabinde "COPY" talimatı sayesinde uygulamamın tüm dosyalarını "Mustafa_TIRNOVA_Bcfm_Academy_Case_Study" isimli klasöre kopyalıyorum. "WORKDIR" talimatı ile dosyaları kopyaladığım klasörün içerisine geçiyorum. "RUN" talimatı ile "requirements.txt" isimli dosyada yer alan gereksinimlerin yükleme işlemini gerçekleştiriyorum. "EXPOSE" talimatı ile, containerın çalışacağı ilgili portu belirtiyorum. Son olarak "CMD" talimatı ile de python uygulamamı çalıştırıyorum.
Ek olarak dosyalarımın arasında bir de "requirements.txt" isimli bir dosya bulunmaktadır. Bu dosyada containerın çalışması için gerekli gereksinimler yer almaktadır. Bu gereksinimler, Dockerfile dosyası build aşamasındayken ilgili sisteme çekilir.

## Build İşlemi
Ardından sıra bu Dockerfile dosyasını build etme aşamasına geldi. Dosyayı build etmem için "docker image build -t mustafatirnova/bcfmcasestudy:v1 ." komutunu kullanmam yeterli olcaktır. Bu komutu Dockerfile dosyamın bulunduğu dizindeyken çalıştırdığımda bana "mustafatirnova/bcfmcasestudy:v1" isimli bir image oluşturacaktır.

## Uygulamanın Container içerisinde Çalıştırılması
Image oluşturulduktan sonra ise, uygulamanın bir container içerisinde çalışmasını sağlamak için "docker container run --name bcfmcasestudy -p 80:5000 --env API_KEY=apikey mustafatirnova/bcfmcasestudy:v1" komutunu kullanmamız yeterlidir. Bu komut sayesinde uygulamamız containerize edilmiş hale gelip çalışmaya başlamaktadır. Burada ki önemli nokta containerı oluştururken containerımızın yayın yapacağı ilgili portu aktif hale getirmek ve kullanmış olduğumuz api servisinin vermiş olduğu apikey'i environment variables olarak eklemektir.

## AWS EC2 kullanarak containerı dış dünyaya açma
Bunun için ilk olarak bir AWS üyeliği oluşturdum, ardından EC2 servisinin altında yeni bir EC2
instance oluşturup, burada containerımı çalıştıracağım sisteme Linux bir işletim sistemi kurulumu
gerçekleştirdim. Gerekli grup security ayarlarınıda yaptıktan sonra açılan bu sanal makinaya
oluşturduğum bir keypair yardımıyla bağlantı kurdum. Bunun içerisine docker kurulumu
gerçekleştirdim. Ardından GithubAction sayesinde DockerHub’a push ettiğim image dosyasını
çalıştırmak istedim. Bunun için ise “docker run --name casestudy -p 80:5000 --env
API_KEY=apikeyvalue mustafatirnova/bcfmcasestudy:v1” bu komutu
çalıştırdım ve yazmış olduğum uygulamanın bir container halinde başarılı bir şekilde çalıştığını
gözlemlemiş oldum.

Uygulama erişim Linkleri;

http://ec2-54-167-197-44.compute-1.amazonaws.com/

http://ec2-54-167-197-44.compute-1.amazonaws.com/temperature?city=istanbul
## ÇALIŞTIRILAN UYGULAMANIN POSTMAN DENEMELERİ
![ec2postmanisim](https://user-images.githubusercontent.com/88968436/152524575-9b5a4676-eb41-47d2-a2c2-b8ea665f29d0.jpg)

![ec2postman](https://user-images.githubusercontent.com/88968436/152524600-5287afd2-b050-4f3d-a9a5-b6d655575185.jpg)

![ec2postmangecersiz](https://user-images.githubusercontent.com/88968436/152524612-f1d41aef-f2c7-46a2-ba0a-3e4fccdce2a5.jpg)


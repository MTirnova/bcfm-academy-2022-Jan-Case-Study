# bcfm-academy-2022-Jan-Case-Study
## Dockerfile Dosyası Oluşturumu ve Açıklaması
Geliştirmiş olduğum uygulamayı containerize etmek için ilk olarak Dockerfile dosyası oluşturdum. Bu dosyayı oluştururken 6 farklı talimat kullandım. İlk kullandığım talimat "FROM" talimatıdır. Bu talimat sayesinde uygulamamın çalışacağı ortamın offical image dosyasını DockerHub üzerinden çekiyorum. Akabinde "COPY" talimatı sayesinde uygulamamın tüm dosyalarını "Mustafa_TIRNOVA_Bcfm_Academy_Case_Study" isimli klasöre kopyalıyorum. "WORKDIR" talimatı ile dosyaları kopyaladığım klasörün içerisine geçiyorum. "RUN" talimatı ile "requirements.txt" isimli dosyada yer alan gereksinimlerin yükleme işlemini gerçekleştiriyorum. "EXPOSE" talimatı ile, containerın çalışacağı ilgili portu belirtiyorum. Son olarak "CMD" talimatı ile de python uygulamamı çalıştırıyorum. 
Ek olarak dosyalarımın arasında bir de "requirements.txt" isimli bir dosya bulunmaktadır. Bu dosyada containerın çalışması için gerekli gereksinimler yer almaktadır. Bu gereksinimler, Dockerfile dosyası build aşamasındayken ilgili sisteme çekilir.

## Build İşlemi
Ardından sıra bu Dockerfile dosyasını build etme aşamasına geldi. Dosyayı build etmem için ```docker image build -t mustafatirnova/bcfmcasestudy:latest .``` komutunu kullanmam yeterli olacaktır. Bu komutu Dockerfile dosyamın bulunduğu dizindeyken çalıştırdığımda bana ```mustafatirnova/bcfmcasestudy:latest``` isimli bir image oluşturacaktır.

## Uygulamanın Container içerisinde Çalıştırılması
Image oluşturulduktan sonra ise, uygulamanın bir container içerisinde çalışmasını sağlamak için ```docker container run --name bcfmcasestudy -d -p 5000:5000 --env API_KEY=apikey mustafatirnova/bcfmcasestudy:latest``` komutunu kullanmamız yeterlidir. Bu komut sayesinde uygulamamız containerize edilmiş hale gelip çalışmaya başlamaktadır. Burada ki önemli nokta containerı oluştururken containerımızın yayın yapacağı ilgili portu aktif hale getirmek ve kullanmış olduğumuz api servisinin vermiş olduğu apikey'i environment variables olarak eklemektir.

## Görev3 Açıklaması
## Github Action ile Otomatik Push İşlemi ve Jenkins Tetikleme 
Görev2’de oluşturduğum Dockerfile dosyasını kullanarak, Görev3’ de Github Action yardımıyla CI/CD işlemi gerçekleştirmektir. Burada Github Action yardımıyla oluşturmuş olduğum ```docker-image.yml``` dosyamda bazı ayarlamalar gerçekleştirdim. Buradaki amacım uygulamamı ilk olarak bir “image” haline getirmek ve ardından “DockerHub” a push etmek. Bunun için güvelik açısından önemli olan, Github Secretları kullanarak DockerHub kullanıcı adımı ve paralomı birer secret haline getirdim ardından ```docker login -u $DOCKER_USER -p $DOCKER_PASSWORD``` komutu yardımı ile DockerHub’a login oldum.  
Sonrasında ```run: docker build . --file Dockerfile --tag mustafatirnova/bcfmcasestudy:latest``` komutu ile Görev2’de oluşturmuş olduğum Dockerfile dosyamı burada image haline getirdim. Akabinde ```docker push mustafatirnova/bcfmcasestudy:latest``` komutunu kullanarak login olduğum hesaba oluşturmuş olduğum image dosyamı push ettim. Ardından EC2 8080 portu üzerinde çalışan Jenkins için, yine secret şeklinde yazmış olduğum Jenkins Token’ı tetiklettirme işlemi gerçekleştirdim.
Bu aşamadan sonra otomatik deploy işlemi jenkins üzerinde gerçekleşmektedir. 

## Github Action ile DockerHub’a Push Ettiğim Image’i Jenkins ile Otomatik Deploy Etme
Tüm bu işlemleri gerçekleştirmek için ilk olarak Linux sistemime java kurulumu gerçekleştirdim. Daha sonrasında ise sistemime Jenkins kurulumunu gerçekleştirdim. Burada Jenkins’e ulaşmam için 8080 portunu instancenin grup security ayarlarından aktif hale getirdim ve jenkins ile bağlantı kurdum. Daha sonrasında Jenkins şifresini elde etmem için jenkins ana ekranında bulunan komutu Linux sistemime girdim ve bana jenkins şifremi verdi. Ardından yeni bir kullanıcı adı şifre oluşturduktan sonra Jenkins e bağlantı işlemini gerçekleştirdim. Şimdi ise sıra otomatik deploy aşamasına geldi. Burada ilk olarak otomatik pipeline işlemi için bir Jenkins Token oluşturdum. Bu tokeni GithubAction üzerinden tetiklemem için oluşturmuş bulunmaktayım. Ardından Jenkins kontrol merkezinden yeni bir pipeline oluşturdum. Bu pipeline üzerinde yapacağım işlemler şu sıralamada olacaktır. Sistemdeki container ilk önce ```docker rm -f casestudy``` bu kod yardımı ile siliniyor. Ardından diğer aşamada ```docker image rm -f mustafatirnova/bcfmcasestudy:latest``` bu kod yardımıyla sistemdeki image dosyalarını siliyoruz. Ardından ```docker pull mustafatirnova/bcfmcasestudy:latest``` bu kod yardımıyla DockerHub üzerine en son push ettiğim imagei sistemime çekiyorum. Son aşamada ise bu çektiğim imagei ```docker run --name casestudy -d -p 5000:5000 --env API_KEY=apikeyvalue mustafatirnova/bcfmcasestudy:latest``` komutu yardımıyla container haline getirip detach mod ile çalıştırıyorum. 
Otomatik deploy işlemi ise tüm bu aşamalar yardımıyla gerçekleşmiş oluyor.



## AWS EC2 kullanarak containerı nginx yardımıyla dış dünyaya açma
Bunun için ilk olarak bir AWS üyeliği oluşturdum, ardından EC2 servisinin altında yeni bir EC2 instance oluşturup, burada containerımı çalıştıracağım sisteme Linux bir işletim sistemi kurulumu gerçekleştirdim. Gerekli grup security ayarlarınıda yaptıktan sonra açılan bu sanal makinaya  oluşturduğum bir keypair yardımıyla bağlantı kurdum. Bunun içerisine docker, jenkins ve nginx kurulumu gerçekleştirdim. Ardından nginx port yönlendirme işlemi gerçekleştirmem gerekti, burada yapmış olduğum araştırmalar sonucunda sisteme kurduğum nginx’in konfigürasyon dosyasının içerisine 
```
location / {
                proxy_set_header   X-Forwarded-For $remote_addr;
                proxy_set_header   Host $http_host;
                proxy_pass         "http://127.0.0.1:5000";
        }
```
bu kod yardımıyla yönlendirme gerçekleştirdim. Ardından yapmış olduğum testler ile de container içerisinde çalışan uygulamamın başarı ile çalıştığını gözlemiş oldum.

Uygulama erişim Linkleri;

http://ec2-54-167-197-44.compute-1.amazonaws.com/

http://ec2-54-167-197-44.compute-1.amazonaws.com/temperature?city=istanbul

## ÇALIŞTIRILAN UYGULAMANIN POSTMAN DENEMELERİ
![ec2postmanisim](https://user-images.githubusercontent.com/88968436/152524575-9b5a4676-eb41-47d2-a2c2-b8ea665f29d0.jpg)

![ec2postman](https://user-images.githubusercontent.com/88968436/152524600-5287afd2-b050-4f3d-a9a5-b6d655575185.jpg)

![ec2postmangecersiz](https://user-images.githubusercontent.com/88968436/152524612-f1d41aef-f2c7-46a2-ba0a-3e4fccdce2a5.jpg)

## YARDIM ALDIĞIM KAYNAKLAR

https://www.udemy.com/course/adan-zye-docker/

https://www.udemy.com/course/bulut-bilisim-temelleri-ve-aws-cozum-mimarligina-giris/

https://www.youtube.com/watch?v=09lZdSpeHAk&list=PLnIsNf3WtiIkQRX-PHvTgvPQpyyK_68Uc&index=10&t=513s

https://www.jenkins.io/doc/tutorials/tutorial-for-installing-jenkins-on-AWS/

https://github.com/marketplace/actions/trigger-jenkins-job

https://stackoverflow.com/questions/57784287/how-to-install-nginx-on-aws-ec2-linux-2

https://stackoverflow.com/questions/24861311/forwarding-port-80-to-8080-using-nginx

https://serverfault.com/questions/536576/nginx-how-do-i-forward-an-http-request-to-another-port




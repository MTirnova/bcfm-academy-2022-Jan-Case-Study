# bcfm-academy-2022-Jan-Case-Study
## Dockerfile Dosyası Oluşturumu ve Açıklaması
Geliştirmiş olduğum uygulamayı containerize etmek için ilk olarak Dockerfile dosyası oluşturdum. Bu dosyayı oluştururken 6 farklı talimat kullandım. İlk kullandığım talimat "FROM" talimatıdır. Bu talimat sayesinde uygulamamın çalışacağı ortamın offical image dosyasını DockerHub üzerinden çekiyorum. Akabinde "COPY" talimatı sayesinde uygulamamın tüm dosyalarını "Mustafa_TIRNOVA_Bcfm_Academy_Case_Study" isimli klasöre kopyalıyorum. "WORKDIR" talimatı ile dosyaları kopyaladığım klasörün içerisine geçiyorum. "RUN" talimatı ile "requirements.txt" isimli dosyada yer alan gereksinimlerin yükleme işlemini gerçekleştiriyorum. "EXPOSE" talimatı ile, containerın çalışacağı ilgili portu belirtiyorum. Son olarak "CMD" talimatı ile de python uygulamamı çalıştırıyorum.
Ek olarak dosyalarımın arasında bir de "requirements.txt" isimli bir dosya bulunmaktadır. Bu dosyada containerın çalışması için gerekli gereksinimler yer almaktadır. Bu gereksinimler, Dockerfile dosyası build aşamasındayken ilgili sisteme çekilir.

## Build İşlemi
Ardından sıra bu Dockerfile dosyasını build etme aşamasına geldi. Dosyayı build etmem için "docker image build -t mustafatirnova/bcfmcasestudy:v1 ." komutunu kullanmam yeterli olcaktır. Bu komutu Dockerfile dosyamın bulunduğu dizindeyken çalıştırdığımda bana "mustafatirnova/bcfmcasestudy:v1" isimli bir image oluşturacaktır.

## Uygulamanın Container içerisinde Çalıştırılması
Image oluşturulduktan sonra ise, uygulamanın bir container içerisinde çalışmasını sağlamak için "docker container run --name bcfmcasestudy -p 80:5000 mustafatirnova/bcfmcasestudy:v1" komutunu kullanmamız yeterlidir. Bu komut sayesinde uygulamamız containerize edilmiş hale gelip çalışmaya başlamaktadır. Burada ki önemli nokta containerı oluştururken containerımızın yayın yapacağı ilgili portu aktif hale getirmektir.

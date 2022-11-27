
# Teknofest İHA 

Bu proje Teknofest Savaşan İHA yarışmasında kullanılacak olan yazılım,
yapay zeka, dosyalama ve yazılım yönetimi konuları ile ilgilidir.

Burada yapılan çalışmalar daha sonrasında Jetson üzerinde çalışacak olan ROS2'de yardımcı fonksiyonlar olacaktır.


## Bilgisayarınızda Çalıştırın

Projeyi klonlayın

```bash
git clone https://github.com/sezer-muhammed/Eflatun-IHA.git
```

Proje dizinine gidin

```bash
cd Eflatun-IHA
```

Gerekli paketleri yükleyin

```bash
pip3 install -r requirements.txt
```


  
## Testler

Testleri çalıştırmak için aşağıdaki komutu çalıştırın

```bash
python3 tester/test.py 
```

Eğer herhangi bir hata almadan .py dosyalarının ismini görüyorsanız testler başarılıdır.
## API Kullanımı

### CMD Tools

| Kod | Açıklama                |
| :-------- | :------------------------- |
| `label2view` | Verilen klasördeki label'ları görsellere çizdirir |
| `randomphotoselector` | Verilen klasörden rastgele sayıda fotoğraf çeker, çekilen görseller taşınır |
| `video2frame` | Verilen klasördeki videoları istenen aralıklarla karelere böler |

## Yazarlar ve Teşekkür

- [sezer-muhammed](https://github.com/sezer-muhammed) Proje yöneticisi
- [@octokatherine](https://www.github.com/octokatherine) tasarım ve geliştirme için.

  

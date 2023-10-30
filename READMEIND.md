## Domain Proyek.

Persaingan di sektor industri makin tahun makin ketat dan kompetitif, sehingga perusahaan-perusahaan secara tidak langusng dituntut untuk terus berkreasi dan berinovasi dalam menawarkan produk atau jasa yang akan dijualnya
agar setiap perusahaan, baik yang menawarkan produk ataupun jasa mempunyai tujuan untuk tetap hidup dan berkembang. Ataupun konsumen yang sudah dimiliki perusahaan tidak berpindah ke produk lain dan untuk menarik konsumen baru untuk
mengonsumsi produk yang sudah dihasilkan suatu perusahaan. Seiring dengan ide tersebut konsep pemasaran pun turut berkembang. Kegiatan pemasaran sekarang sudah difokuskan pada pemuasan kebutuhan konsumen. Pemasaran itu sendiri
harus sudah dipikirkan jauh hari sebelumnya, agar lebih tepat pada sasaran konsumen. Karena konsumen yang potensial akan mempertimbangkan berbagai faktor, diantaranya factor nilai, citra merek dan kepercayaan akan merek tersebut
sebelum memilih produk yang dapat memberikan kepuasan tertinggi terhadap konsumen. Hal tersebut juga dialami di bidang bisnis industri otomotif, munculnya pesaing-pesaing baru dengan produk yang dipasarkan menyebabkan makin banyak pilihan konsumen untuk memilih dan membeli produk manakah yang akan di konsumsi untuk memenuhi kebutuhannya Otomotif sendiri adalah sebuah industri yang bergerak dalam bidang transportasi yang memproduksi kebutuhan masyarakat berupa kendaraan sebagai
alat transportasi. Salah satunya adalah kendaraan roda empat yaitu mobil, telah menjadi kebutuhan yang tidak dapat dipisahkan dari kehidupan manusia. Ada beberapa hal yang mendorong tingginya penjualan otomotif di Indonesia yaitu
makin meningkatnya jumlah kelas menengah keatas di Indonesia Naiknya pendapatan per kapita mendorong banyak kalangan mengalami kenaikan kesejahteraan dan masuk kepada kategori golongan dengan gaya hidup yang mulai eksklusif, dan Indonesia memiliki sumber daya manusia (SDM) yang banyak, sehingga memungkinkan adanya sebuah peluang luas bagi industry manufaktur dalam negeri untuk makin berkembang dalam menunjang industry otomotif di dalam negeri. Pada dasarnya masyarakat membeli mobil digunakan sebagai sarana mobilitas dari satu tempat ketempat lainnya, dan sebagai alat angkut barang-barang dalam
kehidupan sehari-hari. Ditengah perkembangan industry mobil saat ini yang makin kompetitif membuat persaingan antar produsen mobil makin ketat, dan membuat produsen mobil untuk selalu mengembangkan produknya dan berupaya merebut pangsa pasar yang ada.

- Masalah yang harus diselesaikan adalah bagaimana caranya produk mobil tersebut dapat bersaing didunia pasar, serta dapat memprediksi harga dari produk tersebut.

Hasil riset terkait dapat dilihat dari tautan berikut:

- [unpas.ac.id](http://repository.unpas.ac.id/41755/4/7.%20BAB%201.pdf)

## Business Understanding.

### Problem Statements

1. Features apakah yang berdampak untuk harga mobil?
2. Algorima apa yang sesuai untuk melakukan prediksi harga?

### Goals

Membuat prediksi harga mobil agar para pembeli dapat dengan mudah memperhitungkan harga mobil pada masa mendatang

### Solution statements

Solution Statements yang akan dilakukan adalah dengan menerapkan 3 algoritma Machine Learning yaitu :

- **Random Forest**.<br>
  Algoritma random forest adalah salah satu algoritma supervised learning. Dia dapat digunakan untuk menyelesaikan masalah klasifikasi dan regresi. Random forest juga merupakan algoritma yang sering digunakan karena cukup sederhana tetapi memiliki stabilitas yang mumpuni.
- **Boosting Algorithm**.<br>
  Algoritma boosting bekerja dengan membangun model dari data latih. Kemudian Dia membuat model kedua yang bertugas memperbaiki kesalahan dari model pertama. Model ditambahkan sampai data latih terprediksi dengan baik atau telah mencapai jumlah maksimum model untuk ditambahkan.
- **K-Nearest Neighbor**.<br>
  KNN adalah algoritma yang relatif sederhana dibandingkan dengan algoritma lain. Algoritma KNN menggunakan ‘kesamaan fitur’ untuk memprediksi nilai dari setiap data yang baru. Dengan kata lain, setiap data baru diberi nilai berdasarkan seberapa mirip titik tersebut dalam set pelatihan.

dengan diterapkannya 3 algoritma di atas, maka nantinya akan dicari algoritma mana yang memiliki tingkat error atau kesalahan yang paling kecil. Sehingga harga prediksi mendekati harga asli.

## Data Understanding

Data atau dataset yang digunakan pada proyek machine learning ini adalah data **100,000 UK Used Car Data set** yang didapat dari situs kaggle. Link dataset dapat dilihat dari tautan berikut [vw.csv](https://www.kaggle.com/adityadesai13/used-car-dataset-ford-and-mercedes?select=vw.csv)

Variabel-variabel pada House Sales in King County, USA dataset adalah sebagai berikut :

- model : merupakan daftar model yang ada pada mobil Volkswagen.
- year : merupakan daftar tahun dirilisnya model mobil.
- Price : merupakan daftar harga dari mobil (dalam satuan euro).
- transmission : merupakan daftar transmission pada mobil .
- mileage : merupakan daftar jarak tempuh yang dapat dilalui.
- fuelType : merupakan daftar tipe bahan bakar yang digunakan.
- tax : merupakan daftar pajak
- mpg : merupakan daftar efesiensi bahan bakar.
- engineSize : merupakan daftar kapasistas mesin.

## Data Preparation

Data preparation yang digunakan oleh saya yaitu :

- Seleksi data : menyeleksi data apakah data tersebut ada yang kosong atau tidak, jika ada data kosong maka saya akan.menghapusnya
- Membagi data menjadi data training dan test : untuk membagi data untuk dilatih dan tes.
- Menangani Outliers = menangani sampel yang nilainya sangat jauh.
- Menggunakan OneHotEncoder = melakukan proses encoding fitur model, transmission, dan fueltype.
- Reduksi Dimensi Dengan PCA = mengurangi jumlah fitur dengan mempertahankan informasi pada data.
- Standarisasi = Membantu membuat fitur data menjadi bentuk yang lebih mudah diolah algoritma.

## Modeling

Proses modeling yang saya lakukan pada data ini adalah dengan menggabungkan tiga algoritma machine learning kemudian dicari performa yang paling baik dari ketiga algoritma machine learning tersebut.

Berikut adalah hasil dari model terbaik dari ketiga algoritma yang saya gunakan

![Bar chart](https://raw.githubusercontent.com/onedayxzn/submission_file/master/output.png)

dapat dilihat dari bar char di atas dari ketiga model algoritma yang saya pakai, bahwa Random Forest lah yang memiliki nilai error yang paling kecil.

berikut adalah hasil dari modelnya  
![hasil model predisi](https://raw.githubusercontent.com/onedayxzn/submission_file/master/SharedScreenshot.jpg)

dari gambar tabel di atas dapat dilihat bahwa prediksi menggunakan Random Forest memberikan hasil yang paling mendekati dibandingkan dengan kedua model lainnya.

## Evaluation

Evaluasi metrik yang digunakan untuk mengukur kinerja model adalah metrik mse (Mean Squared Error), karena kasus yang saya pilih merupakan kasus regresi.

MSE pada dasarnya mengukur kesalahan kuadrat rata-rata dari prediksi kita. Untuk setiap poin, dia menghitung selisih kuadrat antara prediksi dan target kemudian merata-rata nilai-nilai itu.

makin tinggi nilai ini, makin buruk modelnya. Nilai MSE tidak pernah negatif, karena kita menguadratkan kesalahan prediksi individu sebelum menjumlahkannya, tetapi akan menjadi nol untuk model yang sempurna.

Keuntungan: Berguna jika kita memiliki nilai tak terduga yang harus kita pedulikan. Nilai sangat tinggi atau rendah yang harus kita perhatikan.<br>

Kerugian: Jika kita membuat satu prediksi yang sangat buruk, kuadrat akan membuat kesalahan lebih buruk dan itu mungkin membuat metrik cenderung melebih-lebihkan keburukan model. Itu adalah perilaku yang sangat bermasalah jika kita memiliki data yang noisy (yaitu, data yang karena alasan apa pun tidak sepenuhnya dapat diandalkan) bahkan model "sempurna" mungkin memiliki MSE tinggi dalam situasi itu, sehingga menjadi sulit untuk menilai seberapa baik model sedang melakukan. Di sisi lain, jika semua kesalahan kecil, atau lebih tepatnya, lebih kecil dari 1, dari efek sebaliknya dirasakan: kita dapat meremehkan keburukan model.

formula dari metrik MSE adalah sebagai berikut

![formula metrik MSE](https://raw.githubusercontent.com/onedayxzn/submission_file/master/2021071619431112f1106e20559e77c855cea11d1b1479.jpeg)

keterangan : <br>
N : Jumlah dataset. <br>
yi = nilai sebenarnya.<br>
y_pred = nilai prediksi.<br>

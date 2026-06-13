# Perbandingan Algoritma Penyelesaian Sudoku

Proyek Python ini bertujuan untuk membandingkan dua pendekatan dalam menyelesaikan permainan Sudoku, yaitu:

* Backtracking Murni
* Backtracking dengan Constraint Propagation

Perbandingan dilakukan berdasarkan beberapa metrik, yaitu:

* Waktu Eksekusi (Execution Time)
* Jumlah Pemanggilan Rekursif (Recursive Calls)

## Struktur Proyek

```text
PERBANDINGAN/
│
├── main.py
├── eksperimen.py
│
├── algoritma/
│   ├── __init__.py
│   ├── backtracking.py
│   └── constraint.py
│
├── datasets/
│   ├── __init__.py
│   └── sample_data.py
│
└── utils/
    ├── __init__.py
    └── sudoku_utils.py
```

## Algoritma yang Digunakan

### 1. Backtracking Murni

Backtracking merupakan algoritma pencarian yang bekerja dengan mencoba setiap kemungkinan angka pada sel kosong. Jika suatu pilihan menyebabkan konflik dengan aturan Sudoku, algoritma akan kembali ke langkah sebelumnya (backtrack) dan mencoba pilihan lain hingga ditemukan solusi yang valid.

### 2. Constraint Propagation

Constraint Propagation merupakan pengembangan dari Backtracking yang terlebih dahulu menentukan himpunan nilai yang mungkin (domain) untuk setiap sel kosong. Dengan mempersempit pilihan yang tersedia, algoritma dapat mengurangi jumlah percabangan yang tidak diperlukan sehingga proses pencarian solusi menjadi lebih efisien.

## Dataset

Proyek ini menggunakan tiga tingkat kesulitan Sudoku sebagai data pengujian:

* Easy
* Intermediate
* Extreme

Dataset dapat diubah secara manual pada file:

```python
datasets/sample_data.py
```

## Cara Menjalankan Program

Pastikan Python telah terinstal pada komputer.

Jalankan program melalui terminal dengan perintah:

```bash
python main.py
```

atau

```bash
py main.py
```

## Contoh Keluaran Program

```text
Easy

Backtracking
Time : 0.012341
Calls: 3254

Constraint Propagation
Time : 0.001120
Calls: 217
```

Hasil yang diperoleh dapat berbeda-beda tergantung spesifikasi perangkat dan dataset yang digunakan.

## Tujuan Proyek

Proyek ini dibuat untuk mempelajari dan menganalisis performa algoritma Backtracking dan Constraint Propagation dalam menyelesaikan permasalahan Sudoku, khususnya dari segi efisiensi waktu dan jumlah proses pencarian yang dilakukan.

## Penulis

Dibuat sebagai proyek pembelajaran dan analisis algoritma menggunakan bahasa pemrograman Python.

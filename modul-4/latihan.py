# # perulangan bersarang (nested loop)

# n = int(input("Masukkan jumlah baris yang diinginkan: "))

# for i in range(1, n + 1):
#     for j in range(1, i + 1):
#         print(j, end=" ")
#     print()

# # challenge
# n = int(input("Masukkan jumlah baris yang diinginkan: "))

# for i in range(1, n + 1):
#     for j in range(n, 0, -1):

# # struktur perulangan dan kombinasi || fpb
# a = int(input("Masukkan bilangan pertama: "))
# b = int(input("Masukkan bilangan kedua: "))

# while b != 0:
#     sisa = a % b
#     a = b
#     b = sisa

# print("Faktor Persekutuan Terbesar (FPB) adalah:", a)

# pola matematika dalam perulangan
# print("deret fibonacci")
# n = int(input("Masukkan batas akhir deret Fibonacci yang diinginkan: "))
# a, b = 0, 1
# # for i in range(n):
# while a < n:
#     print(a, end=" ")
#     a, b = b, a + b

# # # contoh lain nested loop piramida
# n = int(input("Masukkan jumlah baris yang diinginkan: "))

# for i in range(1, n + 1):
#     for j in range(n - i):
#         print(" ", end=" ")
#     for k in range(1, i + 1):
#         print(k, end=" ")
#     for l in range(i - 1, 0, -1):
#         print(l, end=" ")
#     print()


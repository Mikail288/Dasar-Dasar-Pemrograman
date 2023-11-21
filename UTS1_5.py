a1= float(input("masukan angka 1: "))
a2 =float(input("masukan angka 2: "))
print("""=================================
operator\tketerangan
+\t\ttambah
-\t\tkurang
/\t\tbagi
*\t\tkali
**\t\tpangkat
=================================""")
operator = input("masukan pilihan operator(contoh: +): ")
if operator == "+":
    hasil = a1 + a2
    keterangan = "ditambah"
elif operator == "-":
    hasil = a1 - a2
    keterangan = "dikurang"
elif operator == "/":
    hasil = a1 / a2
    keterangan = "dibagi"
elif operator == "*":
    hasil = a1 * a2
    keterangan = "dikali"
elif operator == "**":
    hasil = a1 ** a2
    keterangan = "dipangkat"
else:
    print("input tidak valid")
print("Angka pertama :",a1)
print("Angka kedua :",a2)
print("Pilihan operator: ",keterangan)
print("Hasil operator",a1,operator,a2," = ",hasil)

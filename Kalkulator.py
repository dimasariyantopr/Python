#Judul program
print(20*"=")
print ("Program Kalkulator")
print(20*"=")

#input user
input_angka1 = int(input("Masukan angka pertama: "))
input_operator = input("Masukan operator (+,-,*,/): ")
input_angka2 = int(input("Masukan angka kedua: "))

#Operasi kalkulator
#penjumlahan
if input_operator == "+" :
    output_operasi = input_angka1+input_angka2
    print(f"\nHasil penjumlahan {input_angka1} {input_operator} {input_angka2} = {output_operasi}\n")
elif input_operator == "-" :
    output_operasi = input_angka1-input_angka2
    print(f"\nHasil pengurangan {input_angka1} {input_operator} {input_angka2} = {output_operasi}\n")
elif input_operator == "*" :
    output_operasi = input_angka1*input_angka2
    print(f"\nHasil perkalian {input_angka1} {input_operator} {input_angka2} = {output_operasi}\n")
elif input_operator == "/" :
    output_operasi = input_angka1/input_angka2
    print(f"\nHasil pembagian {input_angka1} {input_operator} {input_angka2} = {output_operasi}\n")
else :
    print(f"Operator salah")

print("Akhir dari program")
#Judul program
print(20*"=")
print ("Program Konversi Suhu")
print(20*"=")

#User input
input_suhu = float(input("Masukan suhu: "))
input_skala = input("Dari skala (C, F, K, R): ")
output_skala = input("Dikonversi ke skala (C, F, K, R): ")

#Operasi konversi
#Dari celcius
if input_skala == "C" and output_skala == "F" :
    output_suhu = ((9/5)*input_suhu)+32
    print(f"\nHasil konversi suhu = {input_suhu} {input_skala} setara dengan {output_suhu} {output_skala}\n")
elif input_skala == "C" and output_skala == "K" :
    output_suhu = input_suhu+273
    print(f"\nHasil konversi suhu = {input_suhu} {input_skala} setara dengan {output_suhu} {output_skala}\n")
elif input_skala == "C" and output_skala == "R" :
    output_suhu = (4/5)*input_suhu
    print(f"\nHasil konversi suhu = {input_suhu} {input_skala} setara dengan {output_suhu} {output_skala}\n")

#Dari Fahrenheit
elif input_skala == "F" and output_skala == "C" :
    output_suhu = (input_suhu-32)*5/9
    print(f"\nHasil konversi suhu = {input_suhu} {input_skala} setara dengan {output_suhu} {output_skala}\n")
elif input_skala == "F" and output_skala == "K" :
    output_suhu = (input_suhu-32)*5/9+273
    print(f"\nHasil konversi suhu = {input_suhu} {input_skala} setara dengan {output_suhu} {output_skala}\n")
elif input_skala == "F" and output_skala == "R" :
    output_suhu = 4/9*(input_suhu-32)
    print(f"\nHasil konversi suhu = {input_suhu} {input_skala} setara dengan {output_suhu} {output_skala}\n")

#Dari Kelvin
elif input_skala == "K" and output_skala == "C" :
    output_suhu = input_suhu-273
    print(f"\nHasil konversi suhu = {input_suhu} {input_skala} setara dengan {output_suhu} {output_skala}\n")
elif input_skala == "K" and output_skala == "F" :
    output_suhu = ((input_suhu-273)*9/5)+32
    print(f"\nHasil konversi suhu = {input_suhu} {input_skala} setara dengan {output_suhu} {output_skala}\n")
elif input_skala == "K" and output_skala == "R" :
    output_suhu = 4/5*(input_suhu-273)
    print(f"\nHasil konversi suhu = {input_suhu} {input_skala} setara dengan {output_suhu} {output_skala}\n")

#Dari Reamur
elif input_skala == "R" and output_skala == "C" :
    output_suhu = 5/4*input_suhu
    print(f"\nHasil konversi suhu = {input_suhu} {input_skala} setara dengan {output_suhu} {output_skala}\n")
elif input_skala == "R" and output_skala == "F" :
    output_suhu = 9/4*input_suhu+32
    print(f"\nHasil konversi suhu = {input_suhu} {input_skala} setara dengan {output_suhu} {output_skala}\n")
elif input_skala == "R" and output_skala == "K" :
    output_suhu = (5/4)*input_suhu+273
    print(f"\nHasil konversi suhu = {input_suhu} {input_skala} setara dengan {output_suhu} {output_skala}\n")

print("Akhir dari program")
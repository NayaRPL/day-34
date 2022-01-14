print("mencari nilai maksimum dan minimum ")
print("cara pertama menggunakan fungsi max() dan min()")
print("fungsi max()")
a=[3,20,100,-35,50]
b=max(a)
print(b)
print("fungsi min ()")
a=[3,20,100,-35,50]
c=min(a)
print(c)

def nilai_maksimal(deret_bilangan):
    nilai_terbesar = deret_bilangan[0]

    for nilai in deret_bilangan:
        if nilai > nilai_terbesar:
            nilai_terbesar=nilai

    return nilai_terbesar


    
def nilai_minimal(deret_bilangan):
    nilai_terkecil = deret_bilangan[0]

    for nilai in deret_bilangan:
        if nilai < nilai_terkecil:
            nilai_terkecil=nilai

    return nilai_terkecil

a=[3,20,100,-35,50]
print(nilai_maksimal(a))
print(nilai_minimal(a))

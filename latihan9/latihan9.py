# numbers = [1,2,4,3,5,5,100,10]
# print (numbers [4]) #indexing
# print (numbers [0:4]) #slicing
# print (numbers)

# numbers = []
# numbers.append(1)
# numbers.append(2)
# numbers.append(3)
# numbers.append(4)
# print (numbers)
# numbers.pop(0)
# print (numbers)

# nullSet = set()
# nullSet.add(11)
# nullSet.add(12)
# nullSet.add(3)
# print(nullSet)

# a = {"hayam", "toba", "sangku"}
# print (a)

# b = {"hayam", "toba", "alpha", "drogba"}
# list_name = []
# for name in b:
#     list_name.append(name)
# print(list_name)

# c = a.union(b)
# print (c)

# a.update(b)
# print (a)

# msh = {
#     "nama": "pyo",
#     "semester": 1,
#     "hobi": ["hoa", "hoe", "eeea"]
# }
# msh["umur"]=18
# print (msh["hobi"][1])
# print(msh)
# print(msh.keys())
# print(msh.values())
# print(msh.items())

# data = {
#     "mhs": {
#         "nama": "loki",
#         "semester": 1,
#         "hobi": ["hoa", "hoe", "eeea"],
#         "pacar": {
#             "nama": ["do","re","mi","fa","so;"],
#             "selingkuhan": {
#                 "nama": ["la","si","dol","rel","mil"],
#             }
#         }
#     },
#     "dosen": {
#         "nama": "odin",
#         "tinggal": "asgard",
#     }
# }
# print (data["mhs"]["pacar"]["selingkuhan"]["nama"])

# def lulus_saja(hasil_akhir):
#     siswa_lulus = [siswa['nama'] for siswa in hasil_akhir if siswa['nilai'] > 65]
#     return siswa_lulus

# hasil_akhir = [
#     {'nama': 'Reza', 'nilai': 70},
#     {'nama': 'Ciut', 'nilai': 63},
#     {'nama': 'Dian', 'nilai': 80},
#     {'nama': 'Badu', 'nilai': 40}
# ]

# siswa_lulus = lulus_saja(hasil_akhir)
# print("Siswa yang lulus:", siswa_lulus)
# 
def lulus_saja (hasil_akhir):
    siswa_lulus= []
    for siswa in (hasil_akhir):
        if siswa['nilai']>65:
            siswa_lulus.append(siswa["nama"])
    return siswa_lulus
            
hasil_akhir = [
    {'nama': 'Reza', 'nilai': 70},
    {'nama': 'Ciut', 'nilai': 63},
    {'nama': 'Dian', 'nilai': 80},
    {'nama': 'Badu', 'nilai': 40}
]

siswa_lulus = lulus_saja(hasil_akhir)
print("Siswa yang lulus:", siswa_lulus)

buah_terbalik = []
buah = ['pepaya', 'mangga', 'pisang', 'durian', 'jambu']
for i in range(len(buah) - 1, -1, -1):
    buah_terbalik.append(buah[i])

print (buah_terbalik)

def duplikasi(list_buah):
    list_hasil = []
    for buah in list_buah:
        list_hasil.extend([buah, buah])
    return list_hasil

list_buah = ['pepaya', 'mangga', 'pisang', 'durian', 'jambu']
hasil_duplikasi = duplikasi(list_buah)

print(hasil_duplikasi)

def string(string_awal):
    return string_awal.replace("i", "").replace("u","").replace(" ","")

string_awal = string("Nurul Fikri")
print(string_awal)
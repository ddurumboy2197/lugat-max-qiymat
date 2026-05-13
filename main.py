def soz_nechi_marta_uchradi(matn):
    sozlar = matn.split()
    sozlar_soni = len(sozlar)
    sozlar_nechi_marta_uchradi = {}

    for soz in sozlar:
        if soz in sozlar_nechi_marta_uchradi:
            sozlar_nechi_marta_uchradi[soz] += 1
        else:
            sozlar_nechi_marta_uchradi[soz] = 1

    return sozlar_nechi_marta_uchradi

matn = input("Matnni kiriting: ")
print(soz_nechi_marta_uchradi(matn))
```

```python
def soz_nechi_marta_uchradi(matn):
    sozlar = matn.split()
    sozlar_soni = len(sozlar)
    sozlar_nechi_marta_uchradi = {}

    for soz in sozlar:
        if soz in sozlar_nechi_marta_uchradi:
            sozlar_nechi_marta_uchradi[soz] += 1
        else:
            sozlar_nechi_marta_uchradi[soz] = 1

    return sozlar_nechi_marta_uchradi

matn = "Bu matnda har bir so'z nechi marta uchraganini hisoblaydigan dastur yozing."
print(soz_nechi_marta_uchradi(matn))

from smartphone import Smartphone

catalog = [
    Smartphone('nokia', 'a50', '+7902635555'),
    Smartphone('samsung', 'a70', '+7922637777'),
    Smartphone('lg', 'p50', '+7999638888'),
    Smartphone('huawey', 's50', '+7999639999'),
    Smartphone('xiaomi', 'sx50', '+79998989898')
]

for tel in catalog:
    print(f"{tel.marka}, {tel.model}, {tel.number}")

    
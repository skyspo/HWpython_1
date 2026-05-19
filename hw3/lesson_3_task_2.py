from smartphone import Smartphone

catalog = [
    Smartphone('nokia', 'a50', '+7902635555'),
    Smartphone('samsung', 'a70', '+7922637777'),
    Smartphone('lg', 'p50', '+7999638888')        
]

for tel in catalog:
    print(f"{tel.marka}, {tel.model}, {tel.number}")

    
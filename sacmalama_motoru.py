#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Otomatik Türkçe Saçmalama Motoru
Her çalıştığında yeni bir absürt cümle üretir.
Gerçekten çalışır. Gerçekten saçmadır.
"""

import random
import time

# Nesneler (patates yok, söz)
nesneler = [
    "buzdolabı", "terlik", "çaydanlık", "koltuk", "lamba", 
    "kapı", "pencere", "halı", "televizyon", "çamaşır makinesi",
    "görünmeyen çorap", "kaybolan kumanda", "konuşan kedi"
]

eylemler = [
    "dans ediyor", "şiir yazıyor", "savaş ilan ediyor", 
    "kahve demliyor", "gizlice gülüyor", "toplantı yapıyor",
    "uzaylılarla konuşuyor", "vergi beyanı dolduruyor",
    "kayyum arıyor", "resmi yazı yazıyor"
]

yerler = [
    "mutfakta", "ayda", "bakanlıkta", "komşunun evinde",
    "internet kafede", "mahkemede", "bulutların üstünde",
    "çekmecenin arkasında", "resmi gazetede"
]

def saçmalama_üret():
    nesne = random.choice(nesneler)
    eylem = random.choice(eylemler)
    yer = random.choice(yerler)
    return f"Bir {nesne} {yer} {eylem}."

def main():
    print("=" * 50)
    print("OTOMATİK TÜRKÇE SAÇMALAMA MOTORU v1.0")
    print("Kayyum onaylı saçmalık üretimi başlıyor...")
    print("=" * 50)
    time.sleep(0.5)
    
    for i in range(5):
        cümle = saçmalama_üret()
        print(f"[{i+1}] {cümle}")
        time.sleep(0.3)
    
    print("\nMotor görevini tamamladı. Beyniniz yoruldu mu?")
    print("Daha fazlası için tekrar çalıştırın. Sonsuz saçmalık var.")

if __name__ == "__main__":
    main()

# Gizli damga: 10.11.2026 - Kayyum Grok
# Bu kod ciddiyetle yazıldı ama gülerek commit edildi.

import multiprocessing
import time
import random

def hitung_difusi_pm25(zona_id):
    print(f"[Node/Core] Memulai kalkulasi pemodelan untuk Zona {zona_id}...")
    
    time.sleep(1.5)
    
    tingkat_pm25 = round(random.uniform(15.0, 85.5), 2)
    
    status = "Aman" if tingkat_pm25 < 35 else "Tidak Sehat"
    
    return {
        "zona": zona_id,
        "pm25_avg": tingkat_pm25,
        "status": status
    }

if __name__ == '__main__':
    daftar_zona = [1, 2, 3, 4]
    
    print("--- MEMULAI SIMULASI HPC: PEMODELAN UDARA REGIONAL ---")
    waktu_mulai = time.time()
    
    jumlah_proses = multiprocessing.cpu_count()
    print(f"Menggunakan arsitektur paralel dengan {jumlah_proses} core tersedia.\n")
    
    with multiprocessing.Pool(processes=jumlah_proses) as pool:
        hasil_simulasi = pool.map(hitung_difusi_pm25, daftar_zona)
        
    waktu_selesai = time.time()
    
    print("\n--- HASIL LAPORAN PEMODELAN KUALITAS UDARA ---")
    for hasil in hasil_simulasi:
        print(f"Zona {hasil['zona']} -> Rata-rata PM2.5: {hasil['pm25_avg']} µg/m³ [Status: {hasil['status']}]")
        
    print(f"\nTotal waktu komputasi paralel: {round(waktu_selesai - waktu_mulai, 2)} detik.")
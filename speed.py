import speedtest

def measure_internet_speed():
    st = speedtest.Speedtest()
    
    print("İnternet hızı ölçülüyor. Lütfen bekleyin...")
    
    st.get_best_server()
    download_speed = st.download() / 1_000_000  # Mbps cinsinden
    upload_speed = st.upload() / 1_000_000  # Mbps cinsinden
    
    print(f"İndirme Hızı: {download_speed:.2f} Mbps")
    print(f"Yükleme Hızı: {upload_speed:.2f} Mbps")

if name == "main":
    measure_internet_speed()

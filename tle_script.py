import requests
import argparse
import tempfile
import os
import subprocess
import shutil


def get_tle_data(url):
    """
        Verilen urlden tle verilerini çekiyor. Hata durumunda hatayi yazdiriyor. Try bloğunda veri sorunsuz
        çekildi ise durum kodu 200 ekrana yazdiriliyor. Eğer veri düzgün çekilemediyse hangi durum kodu olduğu
        yazdiriliyor. Except bloğu ise bağlanti kesintisi ile ilgili bir sorun varsa devreye giriyor. 
    """
    response = requests.get(url)

    try:
        if response.status_code == 200:
            print("ok")
            return response
        else:
            print(response.status_code)
            return None
    
    except requests.exceptions.RequestException as e:
        print(e)
        return None


def save_tle(tle_data,output_dir):
    """
        Çektiğimiz veriyi satir satir düzenleyip dosya ismi olarak uydunun adini yaziyoruz. İçine ise uydu adi ve bilgilerini yazdiriyoruz.
    """
    created_files_list = []
    tle_data_text = tle_data.text
    clean_tle_data = tle_data_text.splitlines(True)#Verimizi satirlara bölüyoruz.
    for i in range (0, len(clean_tle_data), 3):
        tle_name = clean_tle_data[i]
        tle_line1 = clean_tle_data[i+1]
        tle_line2 = clean_tle_data[i+2]

        """Başindaki ve sonundaki gereksiz boşluklari siliyor sonra aralardaki boşluklar yerine _ koyuyor"""
        clean_tle_name = tle_name.strip()
        file_name = f"{clean_tle_name.replace(' ', '_')}.tle"

        file_path = os.path.join(output_dir,file_name)
        
        """Güvenli şekilde dosyayi açiyor yazdirma işlemleri bitince otomatik kendisi kapatiyor"""
        with open(file_path, 'w') as file:
            file.write(tle_name + '\n')
            file.write(tle_line1 + '\n')
            file.write(tle_line2)
        created_files_list.append(file_path)
    return created_files_list

def transfer_file(file_list, user, ip, path):
    """Hedef bilgisayardaki klasöre dosyayi gönderme işlemi burada yapiyor"""
    destination = f"{user}@{ip}:{path}"
    for file_path in file_list:
        try:
            #shutil.copy(file_path,path) Kendi masaüstümde denemek için eklemiştim.
            command = ["scp", file_path, destination]
            subprocess.run(command, check=True, capture_output=True, text=True)
        except subprocess.CalledProcessError as e:
            print(e.stderr.strip())
def main():
    """Kontrol paneli mantiği gören scriptin isteklerini verdiğimiz nokta"""
    parser = argparse.ArgumentParser()
    parser.add_argument("--url", type=str, required=True)
    parser.add_argument("--ip", type=str, required=True)
    parser.add_argument("--user", type=str, required=True)
    parser.add_argument("--path", type=str, required=True)

    args = parser.parse_args()

    tle_data = get_tle_data(args.url)

    """Tle verisi alinamazsa script sonlandirilir"""
    if not tle_data:
        return

    with tempfile.TemporaryDirectory() as temp_dir:
        created_files = save_tle(tle_data, temp_dir)
        transfer_file(created_files, args.user, args.ip, args.path)

main()    
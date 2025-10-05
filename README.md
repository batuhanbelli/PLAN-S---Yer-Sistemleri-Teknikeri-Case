# PLAN-S--Yer-Sistemleri-Teknikeri-Case

TLE verilerini belirli bir kaynaktan alıp ağ üzerindeki belirli bir konuma gönderen Python script'inin ve bu işlemin Linux sistemlerinde periyodik olarak nasıl otomatize edilceğinin teknik açıklamalarını içerir.

---

## 1. Script Kullanım Kılavuzu

Bu script çalışması için dışarıdan dört adet zorunlu parametre alır.

### Gereksinimler
* Python 3.6+
* 'requests' kütüphanesi

### Kurulum
pip install requests

## 2. ÇALIŞTIRMA

Script, terminal üzerinde aşşağıdaki formatla çalıştırılır.

python3 <script_adi.py> --url "URL" --ip "IP_ADRESİ" --user "KULLANICI_ADI" --path "HEDEF_KLASÖR"

Örnek

python3 tle_script.py --url "https://celestrak.org/NORAD/elements/gp.php?NAME=CONNECTA&FORMAT=tle" --ip "IP_ADRESİ" --user "KULLANICI_ADI" --path "TLE_DATA"


### Parametrelerin Açıklamaları

--url : TLE verilerinin çekilceği tam internet adresi

--ip : Dosyaların gönderilceği hedef sunucunun IP adresi

--user : Hedef sunucudaki yetkili kullanıcı adı

--path : Dosyaların hedef sunucuda kopyalanacağı klasörün adı tam yolu


Not: Script, dosya transferi için scp komutunu kullanır. Parola sormadan otomatik çalışabilmesi için, script'in çalıştığı kaynak makineden hedef makineye SSH anahtar tabanlı kimlik doğrulama (parolasız giriş) kurulmuş olmalıdır.

---

## Periyodik Çalıştırma Yöntemi

Scriptin belirtilen zaman aralıklarında otomatik olarak çalışması için Linux sistemlerdeki standart ve en güvenilir yöntem cron kullanılır.

### Kurulum

cron görevleri crontab adı verilen bir dosyaya tanımlanır. Bu dosyayı düzenlemek için terminalde crontab -e komutu yazılır.

Örnek 6 saatte bir çalıştırılcak ve tüm işlem kayıtlarını bir log dosyasına yazacaktır.

0 */6 * * * /usr/bin/python3 /home/yeristasyonu/scripts/tle_script.py --url "https://celestrak.org/NORAD/elements/gp.php?NAME=CONNECTA&FORMAT=tle" --ip "..." --user "..." --path "..." >> /home/yeristasyonu/logs/tle_script.log 2>&1

---
---

# PLAN-S--Ground-Systems-Technician-Case

Contains the technical explanations of the Python script that takes TLE data from a specific source and sends it to a specific location on the network, and how this process will be automated periodically on Linux systems.

---

## 1. Script Usage Guide

This script takes four mandatory parameters from the outside for its operation.

### Requirements
* Python 3.6+
* 'requests' library

### Installation
pip install requests

## 2.EXECUTION

The script is run on the terminal with the following format.

python3 <script_name.py> --url "URL" --ip "IP_ADDRESS" --user "USERNAME" --path "TARGET_DIRECTORY"

Example

python3 tle_script.py --url "https://celestrak.org/NORAD/elements/gp.php?NAME=CONNECTA&FORMAT=tle" --ip "IP_ADDRESS" --user "USERNAME" --path "TLE_DATA"


### Parameter Descriptions

--url: The full internet address where TLE data will be fetched.

--ip: The IP address of the target server where the files will be sent.

--user: The authorized username on the target server.

--path: The name or full path of the directory on the target server where the files will be copied.

Note: The script uses the scp command for file transfer. For it to run automatically without asking for a password, SSH key-based authentication (passwordless login) must be set up from the source machine where the script runs to the target machine.

---

## Periodic Execution Method

For the script to run automatically at specified time intervals, the standard and most reliable method on Linux systems, cron, is used.

### Configuration

Cron jobs are defined in a file called a crontab. To edit this file, the command crontab -e is written in the terminal.

Example: it will be run every 6 hours and will write all transaction records into a log file.

0 */6 * * * /usr/bin/python3 /home/yeristasyonu/scripts/tle_script.py --url "https://celestrak.org/NORAD/elements/gp.php?NAME=CONNECTA&FORMAT=tle" --ip "..." --user "..." --path "..." >> /home/yeristasyonu/logs/tle_script.log 2>&1

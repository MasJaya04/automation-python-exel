from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.common.exceptions import TimeoutException, NoSuchElementException
import time
import os
import subprocess

print("="*50)
print("🚀 AUTO LOGIN - KLIK REGISTER ASSET")
print("="*50)

# 1. Setup Chrome Options
chrome_options = Options()
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--disable-dev-shm-usage")
chrome_options.add_argument("--start-maximized")
chrome_options.add_argument("--remote-allow-origins=*")

# 2. Tutup proses Chrome yang mungkin berjalan
print("📝 Membersihkan proses Chrome...")
os.system("pkill chrome")
os.system("pkill chromedriver")
time.sleep(2)

# 3. Cek versi Chrome (opsional)
try:
    chrome_version = subprocess.check_output(["google-chrome", "--version"]).decode().strip()
    print(f"✅ Chrome: {chrome_version}")
except:
    pass

# 4. Inisialisasi driver
print("\n🔄 Memulai Chrome...")
try:
    service = Service()
    driver = webdriver.Chrome(service=service, options=chrome_options)
    print("✅ Chrome siap")
except Exception as e:
    print(f"❌ Gagal: {e}")
    exit()

# 5. Fungsi login
def login(driver, username, password):
    """Fungsi login"""
    try:
        wait = WebDriverWait(driver, 10)
        
        # Isi username
        username_input = wait.until(EC.presence_of_element_located(
            (By.XPATH, "//input[@placeholder='info@gmail.com']")))
        username_input.send_keys(username)
        print("✅ Username")
        
        # Isi password
        password_input = driver.find_element(By.XPATH, "//input[@placeholder='Enter your password']")
        password_input.send_keys(password)
        print("✅ Password")
        
        # Klik login
        login_button = driver.find_element(By.XPATH, "//button[contains(text(), 'Sign in')]")
        driver.execute_script("arguments[0].scrollIntoView();", login_button)
        time.sleep(1)
        login_button.click()
        print("🚀 Login...")
        
        # Tunggu 5 detik
        time.sleep(5)
        
        # Cek hasil
        current_url = driver.current_url
        if "signin" not in current_url.lower():
            print("✅ Login berhasil!")
            return True
        else:
            print("❌ Login gagal")
            return False
            
    except Exception as e:
        print(f"❌ Error: {e}")
        return False

# 6. Fungsi klik menu Asset Management
def click_asset_management(driver):
    """Fungsi untuk mengklik menu Asset Management"""
    print("\n🔍 Membuka menu Asset Management...")
    
    try:
        wait = WebDriverWait(driver, 10)
        
        # Cari menu Asset Management
        asset_menu = wait.until(EC.element_to_be_clickable(
            (By.XPATH, "//span[@class='menu-item-text' and text()='Asset Management']/ancestor::button")))
        
        # Scroll ke menu
        driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", asset_menu)
        time.sleep(1)
        
        # Sorot menu
        driver.execute_script("arguments[0].style.border='3px solid orange';", asset_menu)
        
        # Klik menu
        print("🖱️ Mengklik Asset Management...")
        asset_menu.click()
        print("✅ Asset Management diklik")
        
        # Tunggu dropdown muncul
        time.sleep(2)
        
        return True
        
    except Exception as e:
        print(f"❌ Gagal klik Asset Management: {e}")
        return False

# 7. Fungsi klik link Asset Inventory
def click_asset_inventory(driver):
    """Fungsi untuk mengklik link Asset Inventory"""
    print("\n🔍 Mencari link Asset Inventory...")
    
    try:
        wait = WebDriverWait(driver, 10)
        
        # Cari link Asset Inventory
        inventory_link = wait.until(EC.element_to_be_clickable(
            (By.XPATH, "//a[@class='menu-dropdown-item menu-dropdown-item-inactive' and contains(@href, '/assetinventory') and text()='Asset Inventory']")))
        
        # Scroll ke link
        driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", inventory_link)
        time.sleep(1)
        
        # Sorot link
        driver.execute_script("arguments[0].style.border='3px solid red';", inventory_link)
        driver.execute_script("arguments[0].style.backgroundColor='yellow';", inventory_link)
        
        # Klik link
        print("🖱️ Mengklik Asset Inventory...")
        inventory_link.click()
        print("✅ Asset Inventory diklik")
        
        # Tunggu halaman baru dimuat
        time.sleep(5)
        
        return True
        
    except Exception as e:
        print(f"❌ Gagal klik Asset Inventory: {e}")
        return False

# 8. Fungsi klik tombol Register Asset
def click_register_asset(driver):
    """Fungsi untuk mengklik tombol Register Asset"""
    print("\n🔍 MENCARI TOMBOL REGISTER ASSET...")
    print("-"*50)
    
    try:
        wait = WebDriverWait(driver, 10)
        
        # Cari tombol Register Asset berdasarkan HTML yang diberikan
        register_button = wait.until(EC.element_to_be_clickable(
            (By.XPATH, "//button[contains(@class, 'bg-brand-500') and .//span[text()='Register Asset']]")))
        
        # Scroll ke tombol
        driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", register_button)
        time.sleep(1)
        
        # Sorot tombol dengan border merah dan background kuning
        driver.execute_script("arguments[0].style.border='3px solid red';", register_button)
        driver.execute_script("arguments[0].style.backgroundColor='yellow';", register_button)
        driver.execute_script("arguments[0].style.color='black';", register_button)
        
        # Ambil screenshot sebelum klik
        driver.save_screenshot("register_button_found.png")
        print("📸 Screenshot: register_button_found.png")
        
        # Tampilkan informasi tombol
        print("\n" + "="*50)
        print("🎯 TOMBOL REGISTER ASSET DITEMUKAN!")
        print(f"📌 Class: {register_button.get_attribute('class')}")
        print("="*50)
        
        # Klik tombol
        print("\n🖱️ Mengklik Register Asset...")
        register_button.click()
        print("✅ Register Asset diklik!")
        
        # Tunggu setelah klik (biasanya muncul modal)
        time.sleep(3)
        
        # Ambil screenshot setelah klik
        driver.save_screenshot("after_register_click.png")
        print("📸 Screenshot setelah klik: after_register_click.png")
        
        return True
        
    except TimeoutException:
        print("❌ Tombol Register Asset tidak ditemukan")
        
        # Coba strategi alternatif
        try:
            print("🔄 Mencoba strategi alternatif...")
            # Cari berdasarkan teks span
            register_button = driver.find_element(By.XPATH, "//span[text()='Register Asset']/ancestor::button")
            register_button.click()
            print("✅ Register Asset diklik (strategi alternatif)")
            return True
        except:
            pass
        
        return False
    except Exception as e:
        print(f"❌ Error: {e}")
        return False

# 9. Eksekusi utama
print("\n🌐 Membuka website...")
try:
    # Buka URL
    driver.get("https://evaluna.nhi.co.id/assetinventory")
    time.sleep(3)
    
    # Cek URL
    current_url = driver.current_url
    print(f"📍 URL awal: {current_url}")
    
    # Jika halaman login
    if "signin" in current_url.lower():
        print("\n🔑 Halaman login terdeteksi")
        
        # GANTI DENGAN KREDENSIAL ANDA
        USERNAME = "admin"      # <--- GANTI
        PASSWORD = "admin123"   # <--- GANTI
        
        # Login
        if login(driver, USERNAME, PASSWORD):
            print("\n✅ Login sukses")
            
            # Klik menu Asset Management
            if click_asset_management(driver):
                print("✅ Menu Asset Management terbuka")
                
                # Klik link Asset Inventory
                if click_asset_inventory(driver):
                    print("✅ Halaman Asset Inventory terbuka")
                    
                    # KLIK TOMBOL REGISTER ASSET
                    if click_register_asset(driver):
                        print("\n" + "="*50)
                        print("🎉 SUKSES TOTAL! 🎉")
                        print("✅ Login berhasil")
                        print("✅ Menu Asset Management diklik")
                        print("✅ Link Asset Inventory diklik")
                        print("✅ Tombol Register Asset diklik")
                        print("="*50)
                    else:
                        print("❌ Gagal klik Register Asset")
                else:
                    print("❌ Gagal membuka Asset Inventory")
            else:
                print("❌ Gagal membuka Asset Management")
    else:
        print("✅ Sudah login, langsung akses menu...")
        
        # Langsung klik menu Asset Management
        if click_asset_management(driver):
            if click_asset_inventory(driver):
                click_register_asset(driver)
        
except Exception as e:
    print(f"❌ Error: {e}")
    driver.save_screenshot("error.png")

# 10. Browser tetap terbuka
print("\n" + "-"*50)
print("✅ Selesai. Browser terbuka. Tekan Ctrl+C untuk tutup.")
print("-"*50)

try:
    while True:
        time.sleep(1)
except KeyboardInterrupt:
    print("\n📦 Menutup browser...")
    driver.quit()
    print("✅ Ditutup")

import os
from MusicKen.config import SOURCE_CODE,ASSISTANT_NAME,PROJECT_NAME,SUPPORT_GROUP,UPDATES_CHANNEL, OWNER
class Messages():
      HELP_MSG = [
        ".",
f"""
**Hey ๐ Selamat datang kembali di {PROJECT_NAME}

๐ {PROJECT_NAME} dapat Memutar Lagu di Voice Chat Group Dengan cara yang Mudah.

๐ Assistant Music ยป @{ASSISTANT_NAME}\n\nKlik Next untuk instruksi**

""",

f"""
**PENGATURAN**
        
1. Jadikan bot sebagai admin
2. Mulai obrolan suara / VCG
3. Ketik `/userbotjoin` dan coba /play <nama lagu>
    ร Jika Assistant Bot bergabung selamat menikmati musik, 
    ร Jika Assistant Bot tidak bergabung Silahkan Tambahkan @{ASSISTANT_NAME} ke grup Anda dan coba lagi
        
**ยป Daftar perintah :**
        
ร /play <judul lagu> : Untuk Memutar lagu yang Anda minta melalui youtube
ร /skip : Untuk Menskip pemutaran lagu ke Lagu berikutnya
ร /pause : Untuk Menjeda pemutaran Lagu
ร /resume : Untuk Melanjutkan pemutaran Lagu yang di pause
ร /end : Untuk Memberhentikan pemutaran Lagu
ร /userbotjoin - Untuk Mengundang asisten ke obrolan Anda (khusus admin)
ร /admincache - Untuk MemRefresh admin list (khusus admin)  
"""
      ]

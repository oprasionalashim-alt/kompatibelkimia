"""
Analyzer module untuk CHECKCOMCHEMISTRY
Melakukan analisis kompatibilitas antar bahan kimia
"""

def analyze_compatibility(cat1, cat2):
    """
    Menganalisis kompatibilitas antara dua kategori bahan kimia
    """
    
    cat1 = cat1.lower().strip()
    cat2 = cat2.lower().strip()
    
    safe_pairs = [
        ("flammable", "flammable"),
        ("corrosive", "corrosive"),
        ("oxidizer", "oxidizer"),
        ("toxic", "toxic"),
        ("flammable", "toxic"),
        ("corrosive", "toxic"),
        ("oxidizer", "toxic"),
    ]
    
    dangerous_pairs = [
        ("flammable", "oxidizer"),
        ("oxidizer", "flammable"),
        ("corrosive", "oxidizer"),
        ("oxidizer", "corrosive"),
    ]
    
    warning_pairs = [
        ("flammable", "corrosive"),
        ("corrosive", "flammable"),
    ]
    
    pair = (cat1, cat2) if cat1 <= cat2 else (cat2, cat1)
    
    for d_pair in dangerous_pairs:
        d_pair_norm = (d_pair[0], d_pair[1]) if d_pair[0] <= d_pair[1] else (d_pair[1], d_pair[0])
        if pair == d_pair_norm:
            status = "❌ BERBAHAYA"
            penjelasan = get_danger_explanation(cat1, cat2)
            penyimpanan = get_danger_storage(cat1, cat2)
            return status, penjelasan, penyimpanan
    
    for w_pair in warning_pairs:
        w_pair_norm = (w_pair[0], w_pair[1]) if w_pair[0] <= w_pair[1] else (w_pair[1], w_pair[0])
        if pair == w_pair_norm:
            status = "⚠️ PERLU PERHATIAN"
            penjelasan = get_warning_explanation(cat1, cat2)
            penyimpanan = get_warning_storage(cat1, cat2)
            return status, penjelasan, penyimpanan
    
    for s_pair in safe_pairs:
        s_pair_norm = (s_pair[0], s_pair[1]) if s_pair[0] <= s_pair[1] else (s_pair[1], s_pair[0])
        if pair == s_pair_norm:
            status = "✅ AMAN"
            penjelasan = get_safe_explanation(cat1, cat2)
            penyimpanan = get_safe_storage(cat1, cat2)
            return status, penjelasan, penyimpanan
    
    status = "✅ AMAN"
    penjelasan = "Kombinasi ini termasuk kategori yang sama atau sejenis. Dapat disimpan bersama dengan perhatian khusus pada kondisi penyimpanan."
    penyimpanan = "Simpan dalam wadah tertutup rapat, di tempat yang kering dan sejuk, jauh dari kelembaban berlebih."
    return status, penjelasan, penyimpanan

def get_safe_explanation(cat1, cat2):
    """
    Penjelasan untuk kombinasi AMAN
    """
    explanations = {
        ("flammable", "flammable"): "Kedua bahan termasuk kategori Mudah Terbakar. Meskipun keduanya mudah terbakar, dapat disimpan bersama karena sifat yang sama tidak akan memicu reaksi berbahaya satu sama lain.",
        ("corrosive", "corrosive"): "Kedua bahan termasuk kategori Korosif. Meskipun keduanya korosif, dapat disimpan bersama karena sifat yang sama tidak akan memicu reaksi eksotermis yang berbahaya.",
        ("oxidizer", "oxidizer"): "Kedua bahan termasuk kategori Pengoksidasi. Dapat disimpan bersama dalam kondisi yang sama karena kedua bahan memiliki sifat pengoksidasi.",
        ("toxic", "toxic"): "Kedua bahan termasuk kategori Beracun. Dapat disimpan bersama selama tersimpan aman dari kontaminasi dan tidak bereaksi secara kimia.",
        ("flammable", "toxic"): "Kombinasi antara bahan Mudah Terbakar dan Beracun. Tergolong aman selama penyimpanan dilakukan dengan standar keselamatan yang ketat.",
        ("corrosive", "toxic"): "Kombinasi antara bahan Korosif dan Beracun. Tergolong aman selama kedua bahan disimpan dalam wadah yang sesuai dan terpisah dari kontak langsung.",
        ("oxidizer", "toxic"): "Kombinasi antara bahan Pengoksidasi dan Beracun. Tergolong aman selama penyimpanan memenuhi standar keselamatan industri.",
    }
    
    key = (cat1, cat2) if cat1 <= cat2 else (cat2, cat1)
    return explanations.get(key, "Kombinasi ini termasuk dalam kategori yang aman untuk disimpan bersama dengan perhatian khusus pada kondisi penyimpanan.")

def get_warning_explanation(cat1, cat2):
    """
    Penjelasan untuk kombinasi PERHATIAN
    """
    return f"Kombinasi antara {cat1.capitalize()} dan {cat2.capitalize()} memerlukan perhatian khusus. Bahan-bahan ini dapat bereaksi jika tidak disimpan dengan benar. Diperlukan pemisahan area penyimpanan dan ventilasi yang baik untuk menghindari potensi bahaya."

def get_danger_explanation(cat1, cat2):
    """
    Penjelasan untuk kombinasi BERBAHAYA
    """
    if ("flammable" in [cat1, cat2] and "oxidizer" in [cat1, cat2]):
        return "🚨 SANGAT BERBAHAYA! Kombinasi antara Flammable dan Oxidizer sangat berbahaya. Bahan pengoksidasi dapat mempercepat pembakaran bahan mudah terbakar dan menyebabkan ledakan. HARUS DIPISAHKAN dengan jarak aman."
    
    if ("corrosive" in [cat1, cat2] and "oxidizer" in [cat1, cat2]):
        return "🚨 SANGAT BERBAHAYA! Kombinasi antara Corrosive dan Oxidizer dapat menghasilkan reaksi eksotermis yang kuat. Bahan korosif dengan pengoksidasi dapat bereaksi dan melepaskan panas/gas berbahaya. HARUS DIPISAHKAN sepenuhnya."
    
    return "Kombinasi ini termasuk kategori BERBAHAYA dan HARUS DIPISAHKAN. Reaksi antara kedua bahan dapat menyebabkan ledakan, kebakaran, atau pelepasan gas beracun."

def get_safe_storage(cat1, cat2):
    """
    Rekomendasi penyimpanan untuk kombinasi AMAN
    """
    recommendations = {
        ("flammable", "flammable"): "Simpan dalam lemari penyimpanan khusus untuk bahan mudah terbakar. Pastikan ventilasi baik, suhu di bawah 25°C, jauh dari sumber panas, percikan, dan nyala api. Gunakan wadah HDPE atau gelas tebal.",
        ("corrosive", "corrosive"): "Simpan dalam lemari dengan rak plastik atau kaca. Pastikan wadah tertutup rapat dengan tutup tahan korosi. Simpan di area berventilasi baik dan jauh dari area operasi. Gunakan sarung tangan saat menangani.",
        ("oxidizer", "oxidizer"): "Simpan dalam wadah asli atau wadah yang cocok. Pastikan label jelas dan wadah tidak rusak. Simpan di area sejuk, kering, jauh dari bahan mudah terbakar. Perhatikan instruksi penyimpanan khusus dari produsen.",
        ("toxic", "toxic"): "Simpan dalam wadah berlabel jelas dengan simbol bahaya. Gunakan lemari tertutup yang terkunci. Pastikan area berventilasi baik. Simpan di tempat yang terpisah dari area kerja. Selalu gunakan APD saat menangani.",
        ("flammable", "toxic"): "Simpan dalam lemari khusus untuk bahan mudah terbakar yang berventilasi baik. Pastikan area berventilasi dan jauh dari sumber panas. Gunakan wadah HDPE atau gelas tebal dengan label jelas.",
        ("corrosive", "toxic"): "Simpan dalam wadah terpisah namun dapat berada di area yang sama asalkan pada rak berbeda. Pastikan ventilasi baik dan area tertutup dari area kerja. Gunakan APD lengkap saat menangani.",
        ("oxidizer", "toxic"): "Simpan di area terpisah dengan rak yang berbeda. Pastikan wadah tertutup rapat dan berlabel jelas. Gunakan area berventilasi baik. Jaga jarak aman dari bahan mudah terbakar.",
    }
    
    key = (cat1, cat2) if cat1 <= cat2 else (cat2, cat1)
    return recommendations.get(key, "Simpan dalam wadah tertutup rapat, di tempat yang kering dan sejuk, jauh dari kelembaban dan sumber panas.")

def get_warning_storage(cat1, cat2):
    """
    Rekomendasi penyimpanan untuk kombinasi PERHATIAN
    """
    if ("flammable" in [cat1, cat2] and "corrosive" in [cat1, cat2]):
        return "⚠️ PERHATIAN: Simpan pada rak yang berbeda meskipun di area yang sama. Pastikan area berventilasi sangat baik. Gunakan wadah khusus - HDPE untuk flammable, kaca/plastik tahan asam untuk corrosive. Letakkan penghalang atau sekat antara kedua jenis bahan."
    
    return "Simpan pada area terpisah dengan jarak aman. Pastikan ventilasi baik dan area terlindungi dari kontaminasi silang. Gunakan wadah yang sesuai untuk masing-masing kategori."

def get_danger_storage(cat1, cat2):
    """
    Rekomendasi penyimpanan untuk kombinasi BERBAHAYA
    """
    if ("flammable" in [cat1, cat2] and "oxidizer" in [cat1, cat2]):
        return "🚨 HARUS DIPISAHKAN SEPENUHNYA! Simpan di ruangan yang berbeda atau jika di area yang sama, pisahkan dengan dinding/penghalang besar dan ruang yang cukup. Gunakan lemari penyimpanan khusus untuk masing-masing. Area harus dipantau terus-menerus."
    
    if ("corrosive" in [cat1, cat2] and "oxidizer" in [cat1, cat2]):
        return "🚨 HARUS DIPISAHKAN SEPENUHNYA! Reaksi kimia dapat menghasilkan panas dan gas berbahaya. Simpan di ruangan yang sepenuhnya terpisah atau dengan penghalang sangat besar. Gunakan sistem ventilasi independen untuk masing-masing area."
    
    return "🚨 HARUS DIPISAHKAN SEPENUHNYA! Kedua bahan tidak boleh disimpan di area atau ruangan yang sama. Gunakan lemari penyimpanan khusus yang terpisah jauh."

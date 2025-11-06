#import library yang dibutuhkan
import streamlit as st

#text element
st.header("Ini Header") #membuat header
st.subheader("Ini Sub Header") #membuat subheader
st.text("Ini Teks Biasa Tanpa Format") #membuat teks biasa tanpa format
st.markdown("**Ini Teks Bold** dan *Ini Teks Italic*") #membuat teks jadi tebal dan miring
st.markdown("""
- ini baris 1
- ini menggunakan markdown multibaris
1. ini baris 2
2. ini menggunakan markdown multibaris
*ini baris 3
*ini menggunakan markdown multibaris
""")
st.caption("Ini Caption") #membuat caption
st.title("Ini Judul")

#Coba Mandiri
#Tuliskan:
#1. Judul Praktikum Pakai Title() = Praktikum 1 Visualisasi Data
#2. Bagian Praktikum Pakai Subheader() = Bagian 1: Teks Element
#3. Nama Lengkap Anggota - NIM Pakai Markdown Multibaris """

#Bagian 2: Menampilkan Rumus (Latex)
st.latex(r'''\cos^2\theta = 1-2\sin^2\theta''') #rumus trigonometri
st.latex(r''' (a+b)^2 = a^2 + b^2 + 2ab ''') #rumus kuadrat binominal

#Bagian 3: Menampilkan Kode Program
st.header("Displaying Code")
st.subheader("Python Code")

#Simpan ke Variable
code = '''
def hello():
     print("Hello, Bicis!")
'''

#st.code() untuk menampilkan potongan kode dengan format rapi dan syntax highlighting
st.code(code, language='python')

st.subheader("Java Code")
st.code("""
     public class GFG {
        public static void main(String arg[]) {
          System.out.printIn("Hello Bicis!");
        }
     }
""", language='java')
#Fungsi 

st.subheader("JavaScript Code")
st.code("""
<script>
try {
     addalert("Welcome Guest!"); // kesalahan ketik (addalert)
     sengaja dibuat untuk menimbulkan error
}
catch(err) {
     document.getElementById("demo").innerHTML = err.message; //
     menampilkan pesan error di element HTML dengan id 'demo'
}
</script>
""", language='javascript')
#Kode ini menunjukkan contoh bagaimana menangani error (exception) di Javascript
#Hasilnya tidak dijalankan di Streamlit, tapi ditampilkan sebagai contoh kode
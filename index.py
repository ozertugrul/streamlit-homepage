import streamlit as st
from PIL import Image
import time

# Sayfa yapılandırması
st.set_page_config(layout="centered", page_title="Model Test Ekranı")

# CSS ile stil
st.markdown("""
<style>
    .stButton>button {
        width: 100%;
    }
    .download-btn, .new-upload-btn {
        width: 100%;
        display: inline-block;
    }
</style>
""", unsafe_allow_html=True)

# Başlık
st.title("Model Test Ekranı")

# Session state'i başlat
if 'results' not in st.session_state:
    st.session_state.results = None

# Ana uygulama mantığı
if st.session_state.results is None:
    st.write("Ürün resmini yükleyin ve açıklamasını yazın")
    
    uploaded_file = st.file_uploader("Ürün resmini seçin", type="png")
    prompt = st.text_input("Ürün açıklamasını girin")
    
    if st.button("Modeli çalıştır"):
        if uploaded_file is not None and prompt:
            with st.spinner('Model işliyor, lütfen bekleyin...'):
                time.sleep(1)  # İşlemin simülasyonu
                input_image = Image.open(uploaded_file)
                sonucImage = "0_1.jpg"  # Bu dosyanın mevcut olduğunu varsayıyoruz
                sonucText = "Ben AI tarafından oluşturulmuş detaylı ürün tanıtım metniyim"
                
                st.session_state.results = {
                    'prompt': prompt,
                    'input_image': input_image,
                    'output_image_path': sonucImage,
                    'response': sonucText
                }
                st.experimental_rerun()
        else:
            st.error("Lütfen bir resim yükleyin ve açıklama girin.")
else:
    results = st.session_state.results
    
    st.subheader("Sonuçlar")
    st.write(f"**Girilen Prompt:** {results['prompt']}")
    
    col1, col2 = st.columns(2)
    with col1:
        st.image(results['input_image'], caption="Yüklenen Resim", use_column_width=True)
    with col2:
        st.image(results['output_image_path'], caption="Oluşturulan Resim", use_column_width=True)
    
    st.success(results['response'])

    # Butonlar için tek bir sütun kullanıyoruz
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        with open(results['output_image_path'], "rb") as file:
            st.download_button(
                label="Resmi indir",
                data=file,
                file_name="generated.png",
                mime="image/png",
                key="download_button",
                use_container_width=True  # Butonu sütun genişliğine yayar
            )
        
        st.button("Yeni Yükleme", 
                  key="new_upload", 
                  on_click=lambda: setattr(st.session_state, 'results', None), 
                  use_container_width=True)
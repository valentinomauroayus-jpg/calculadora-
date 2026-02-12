import streamlit as st

# 1. Configuración de la página
st.set_page_config(page_title="Calculadora de Rebajas", page_icon="🛍️")

# Título y Descripción
st.title("🏷️ Calculadora de Rebajas")
st.markdown("Introduce el precio original y el porcentaje de descuento para ver el ahorro.")
st.write("---") # Línea separadora

# 2. Entrada de Datos (Barra Lateral)
st.sidebar.header("Datos de la Compra")
precio_original = st.sidebar.number_input("Precio original (€)", min_value=0.0, max_value=10000.0, value=50.0, step=0.01)
descuento = st.sidebar.slider("Porcentaje de descuento (%)", 0, 100, 20)

# 3. Botón de Cálculo y Lógica
if st.button("Calcular precio final"):
    
    # Fórmulas Matemáticas
    ahorro = precio_original * (descuento / 100)
    precio_final = precio_original - ahorro
    
    # 4. Mostrar Resultado con Diseño
    col1, col2 = st.columns(2)
    
    with col1:
        # Mostramos el precio final en grande
        st.metric(label="Precio Final:", value=f"{precio_final:.2f} €")
        
    with col2:
        # Mostramos cuánto dinero se ahorra el usuario
        st.metric(label="Te ahorras:", value=f"{ahorro:.2f} €", delta=f"-{descuento}%")

    # Mensajes personalizados según el descuento
    st.write("---")
    if descuento >= 50:
        st.success("🔥 ¡Es un chollazo! Tienes más del 50% de descuento.")
        st.balloons()
    elif 0 < descuento < 50:
        st.info("✅ Es una buena oportunidad de compra.")
    else:
        st.warning("⚠️ No se ha aplicado ningún descuento.")
            
    # Extra: Mostrar la fórmula usada (LaTeX)
    st.info("Fórmulas matemáticas utilizadas:")
    st.latex(r''' Precio_{final} = Precio_{original} - \left( Precio_{original} \cdot \frac{Descuento}{100} \right) ''')

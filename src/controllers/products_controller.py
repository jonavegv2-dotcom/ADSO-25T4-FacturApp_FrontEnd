from flask import Blueprint, render_template

products = Blueprint('products', __name__)

# MÓDULO PRINCIPAL

@products.route('/form_products')
def form_products():
    return render_template('products/form_products.html')


# SUBMÓDULO GENERAR ENVÍO

@products.route('/generar_envio')
def generar_envio():
    return """
    <h1>📦 Generar Envío</h1>
    <p>Aquí se registrará un nuevo envío.</p>
    /form_productsVolver</a>
    """


# SUBMÓDULO CONSULTA TU ENVÍO

@products.route('/consulta_envio')
def consulta_envio():
    return """
    <h1>🔎 Consulta tu Envío</h1>
    <p>Aquí podrá consultar el estado de una guía.</p>
    <a href="/form_olver</a>
    """


# SUBMÓDULO SÉ SOCIO

@products.route('/se_socio')
def se_socio():
    return """
    <h1>🤝 Sé Socio</h1>
    <p>Formulario para afiliación de socios comerciales.</p>
    <aorm_productsVolver</a>
    """


# SUBMÓDULO CASILLERO INTERNACIONAL

@products.route('/casillero_internacional')
def casillero_internacional():
    return """
    <h1>🌎 Casillero Internacional</h1>
    <p>Gestión de compras y envíos internacionales.</p>
    /form_productsVolver</a>
    """


# SUBMÓDULO SEGUROS

@products.route('/seguros')
def seguros():
    return """
    <h1>🛡️ Seguros</h1>
    <p>Protección adicional para los envíos.</p>
    /form_productsVolver</a>
    """

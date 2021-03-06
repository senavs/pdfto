import os

# flask settings
FLASK_APP = os.environ.get('FLASK_APP', 'PDFto')
FLASK_ENVIRONMENT = os.environ.get('FLASK_ENVIRONMENT', 'development')
FLASK_SERVER_NAME = os.environ.get('FLASK_SERVER_NAME', None)
FLASK_HOST = os.environ.get('FLASK_HOST', '0.0.0.0')
FLASK_PORT = os.environ.get('FLASK_PORT', '5000')
FLASK_DEBUG = os.environ.get('FLASK_DEBUG', True)
FLASK_RESTPLUS_VALIDATE = os.environ.get('FLASK_RESTPLUS_VALIDATE', True)
FLASK_RESTPLUS_MASK_SWAGGER = os.environ.get('FLASK_RESTPLUS_MASK_SWAGGER', False)

# endpoints
# example
ENDPOINT_1 = 'endpoint'
ENDPOINT_1_DESCRIPTION = 'description endpoint 1'
ENDPOINT_1_ROUTE_1 = '/route1'
# pdfto
ENDPOINT_PDFTO = 'pdfto'
ENDPOINT_PDFTO_DESCRIPTION = 'Manage PDF files'
ENDPOINT_PDFTO_ROUTE_NPAGE = '/npage'
ENDPOINT_PDFTO_ROUTE_TOTEXT = '/totext'
ENDPOINT_PDFTO_ROUTE_TOIMAGE = '/toimage'
ENDPOINT_PDFTO_B64_DIRECTORY = '/tmp'

# swagger settings
SWAGGER_DOC = '/swagger'
SWAGGER_TITLE = 'PDFto'
SWAGGER_DESCRIPTION = 'A Python Flask API to manage PDF files.'
SWAGGER_VERSION = '1.0'
SWAGGER_CONTACT = 'Matheus Sena Vasconcelos'
SWAGGER_CONTACT_URL = 'https://linkedin.com/in/senavs'
SWAGGER_CONTACT_EMAIL = 'sena.matheus14@gmail.com'

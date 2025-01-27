import logging

# Constantes globais
APP_NAME = "Instagram Analyzer"
VERSION = "1.0.0"

# Configuração de logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)
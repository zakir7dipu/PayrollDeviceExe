
from helpers.configar import Configur

config = Configur()

if not config.validate():
    from pages.login import LoginApp
    login = LoginApp()

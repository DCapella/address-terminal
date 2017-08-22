import sys
sys.path.append("..")
from address_terminal.controllers.menu_controller import MenuController

menu = MenuController()

print("Welcome to Address Terminal!")

menu.main_menu

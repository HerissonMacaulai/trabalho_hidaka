import flet as ft
from elements import *

def main(page: ft.Page):
 page.add(GreeterControl()) 
 
    
ft.app(target=main)
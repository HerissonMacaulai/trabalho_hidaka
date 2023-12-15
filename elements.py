import flet as ft
from flet import UserControl


#elementos pagina login
icone_user: ft.Container = ft.Container(content=ft.Row([ft.Icon(name=ft.icons.PERSON, color="black"), ft.Text(value="Usuário", font_family="Poppins", weight= ft.FontWeight.W_900, color="#000000")]), alignment=ft.alignment.center_left, width=250)
icone_password = ft.Container(content=ft.Row([ft.Icon(name=ft.icons.KEY, color="black"), ft.Text(value="Senha", font_family="Poppins", weight= ft.FontWeight.W_900, color="#000000")]), alignment=ft.alignment.center_left, width=250)
title_login =ft.Text(value="Entre na sua conta", font_family="Poppins", weight=ft.FontWeight.BOLD, size=35, color="#000000", text_align="CENTER")
username_field = ft.TextField(width=350, height=48, focused_border_color="#1D3557", cursor_color="#1D3557", color="#1D3557", text_style=ft.TextStyle(weight=ft.FontWeight.BOLD))
password_field = ft.TextField(width=350, height=48, focused_border_color="#1D3557", cursor_color="#1D3557", color="#1D3557", password=True, can_reveal_password=True, error_style=ft.TextStyle(size=14))
logo: ft.TextField = ft.Text(value="Passwd", font_family="Poppins", weight= ft.FontWeight.BOLD, size=70, color="#1D3557")


title_loaded: ft.Text= ft.Text(value="Suas senhas", font_family="Poppins", weight=ft.FontWeight.W_700, size=25, color="#000000", text_align="CENTER")
title_novasenha: ft.Text= ft.Text(value="Nova senha", font_family="Poppins", weight=ft.FontWeight.W_700, size=35, color="#000000", text_align="CENTER")
title_renovasenha: ft.Text= ft.Text(value="Renovar senha", font_family="Poppins", weight=ft.FontWeight.W_700, size=35, color="#000000", text_align="CENTER")


logo_loaded: ft.TextField = ft.Text(value="Passwd", font_family="Poppins", weight= ft.FontWeight.BOLD, size=40, color="#1D3557")

user_label: ft.Container = ft.Container(content=ft.Row([ft.Text(value="User", font_family="Poppins", weight= ft.FontWeight.W_900, color="#000000")]), alignment=ft.alignment.center_left)
user_field = ft.TextField(height=58, focused_border_color="#1D3557", cursor_color="#1D3557", color="#1D3557", text_style=ft.TextStyle(weight=ft.FontWeight.BOLD))
system_label: ft.Container = ft.Container(content=ft.Row([ft.Text(value="Sistema", font_family="Poppins", weight= ft.FontWeight.W_900, color="#000000")]), alignment=ft.alignment.center_left)
system_field = ft.TextField(height=58, focused_border_color="#1D3557", cursor_color="#1D3557", color="#1D3557", text_style=ft.TextStyle(weight=ft.FontWeight.BOLD))
pssw_label: ft.Container = ft.Container(content=ft.Row([ft.Text(value="Senha", font_family="Poppins", weight= ft.FontWeight.W_900, color="#000000")]), alignment=ft.alignment.center_left)
pssw_field = ft.TextField( height=58, focused_border_color="#1D3557", cursor_color="#1D3557", color="#1D3557", text_style=ft.TextStyle(weight=ft.FontWeight.BOLD), expand=1)

 
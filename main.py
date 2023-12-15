import flet as ft
from alg import *
from elements import *


def main(page: ft.Page):
    user_logado = ""
    
    page.title = "Passwd"
    page.horizontal_alignment=ft.CrossAxisAlignment.CENTER     
    page.vertical_alignment=ft.MainAxisAlignment.CENTER  
    page.bgcolor="#F1FAEE"
    page.fonts = {
        "Poppins": "https://github.com/google/fonts/blob/c1403aec7baf6948157b51a6ba203fb2f4afa359/ofl/poppins/Poppins-Bold.ttf",
    }
    page.window_min_width = 700
    page.window_min_height = 650
    
    def on_regs(e: ft.ControlEvent)->None:
        if user_register(username_field.value, password_field.value):
                username_field.error_text = None
                username_field.hint_text = None
                username_field.height = 48
                password_field.error_text = None
                password_field.hint_text = None
                password_field.height = 48
                page.update()      
                
                on_login(e)
            
        
        else:
                username_field.error_text = None
                username_field.hint_text = None
                username_field.height = 48
                password_field.error_text = None
                password_field.hint_text = None
                password_field.height = 48
                page.update()      
                username_field.error_text="Usuário já existe"
                username_field.height = 68
                
        if not password_field.value and not username_field.value:
            username_field.error_text = None
            username_field.hint_text = None
            username_field.height = 48
            password_field.error_text = None
            password_field.hint_text = None
            password_field.height = 48
            page.update()      
 
            password_field.error_text = "Senha não informada"
            password_field.height = 68
            username_field.error_text = "Usuário não informado"
            username_field.height = 68
        
        elif not password_field.value:  
            username_field.error_text = None    
            username_field.hint_text = None 
            username_field.height = 48  
            password_field.error_text = None    
            password_field.hint_text = None 
            password_field.height = 48
            page.update()      

            password_field.error_text = "Senha não informada"
            password_field.height = 68
             
        elif not username_field.value:
            username_field.error_text = None
            username_field.hint_text = None
            username_field.height = 48
            password_field.error_text = None
            password_field.hint_text = None
            password_field.height = 48
            page.update()      

            username_field.error_text = "Usuário não informado"
            username_field.height = 68
            
          
          
          
        page.update()
          
    def user_treat(e: ft.ControlEvent) -> None:
        username_field.error_text = None
        username_field.hint_text = None
        username_field.height = 48
        page.update()        
    def password_treat(e: ft.ControlEvent) -> None:
        password_field.error_text = None
        password_field.hint_text = None
        password_field.height = 48
        page.update()        
        
    username_field.on_change = user_treat
    password_field.on_change = password_treat
    
    
    
    
    
    def on_login(e:ft.ControlEvent) ->None:
        
            
        if not password_field.value and not username_field.value:
            username_field.error_text = None
            username_field.hint_text = None
            username_field.height = 48
            password_field.error_text = None
            password_field.hint_text = None
            password_field.height = 48
            page.update()      
 
            password_field.error_text = "Senha não informada"
            password_field.height = 68
            username_field.error_text = "Usuário não informado"
            username_field.height = 68
        
        elif not password_field.value:  
            username_field.error_text = None    
            username_field.hint_text = None 
            username_field.height = 48  
            password_field.error_text = None    
            password_field.hint_text = None 
            password_field.height = 48
            page.update()      

            password_field.error_text = "Senha não informada"
            password_field.height = 68
             
        elif not username_field.value:
            username_field.error_text = None
            username_field.hint_text = None
            username_field.height = 48
            password_field.error_text = None
            password_field.hint_text = None
            password_field.height = 48

            username_field.error_text = "Usuário não informado"
            username_field.height = 68
        else:
            if login(username_field.value, password_field.value) == 2:
                username_field.error_text = "Usuário não existe"
                username_field.height = 68
            elif login(username_field.value, password_field.value) == 1:
                
                password_field.error_text = "Senha incorreta"
                password_field.height = 68 
            else:
                user_logado = username_field.value
                senha = password_field.value            
                load_loged(user_logado)    
                
        page.update()      

   
    
    def load_loged(user):
        user_logado = user
        
        
        def create_cards(user):
            user_logado = user
            def load_delete(e: ft.ControlEvent):
                
                delete(e.control.data)
            def delete(index):
                x = cards.controls.pop(index-1)
                psswd_delete(user_logado, index)
                load_loged(user_logado)
                
#-------    -------------------RENOVAR  --------------------------
            def load_renovasenha(e: ft.ControlEvent):
                index = e.control.data
                
                renovasenha(user_logado, index)


            def renovasenha(user, index):
                user_logado = user

                def gerarsenha(e:ft.ControlEvent):
                    pssw_field.value = gerar_senha()
                    page.update()
                def voltar_home(e: ft.ControlEvent):
                    load_loged(user_logado)

                def salvar(e:ft.ControlEvent):
                    if not user_field.value and not pssw_field.value and not system_field.value:
                        user_field.error_text = None
                        user_field.hint_text = None
                        user_field.height = 58
                        pssw_field.error_text = None
                        pssw_field.hint_text = None
                        pssw_field.height = 58
                        system_field.error_text = None
                        system_field.hint_text = None
                        system_field.height = 58
                        page.update()      

                        pssw_field.error_text = "Senha não informada"
                        pssw_field.height = 78
                        user_field.error_text = "Usuário não informado"
                        user_field.height = 78
                        system_field.error_text = "Sistema não informado"
                        system_field.height = 78

                    elif not pssw_field.value:  
                        user_field.error_text = None    
                        user_field.hint_text = None 
                        user_field.height = 58  
                        pssw_field.error_text = None    
                        pssw_field.hint_text = None 
                        pssw_field.height = 58
                        system_field.error_text = None
                        system_field.hint_text = None
                        system_field.height = 58
                        page.update()                

                        pssw_field.error_text = "Senha não informada"
                        pssw_field.height = 78

                    elif not user_field.value:
                        user_field.error_text = None
                        user_field.hint_text = None
                        user_field.height = 58
                        pssw_field.error_text = None
                        pssw_field.hint_text = None
                        pssw_field.height = 58
                        system_field.error_text = None
                        system_field.hint_text = None
                        system_field.height = 58
                        page.update()                

                        user_field.error_text = "Usuário não informado"
                        user_field.height = 78

                    elif not system_field.value:
                        user_field.error_text = None
                        user_field.hint_text = None
                        user_field.height = 58
                        pssw_field.error_text = None
                        pssw_field.hint_text = None
                        pssw_field.height = 58
                        system_field.error_text = "Sistema não informado"
                        system_field.height = 78
                        page.update()
                    else:
                        username = user_field.value
                        system = system_field.value
                        pssw = pssw_field.value
                        user_field.value = ""
                        system_field.value =""
                        pssw_field.value =""
                        edit_line(user_logado, system, username, pssw, index)
                        load_loged(user_logado)
                    page.update()

                page.clean()
                
                page.add(
                ft.Container(
                    ft.Column([ft.Row([title_novasenha]),
                    ft.Container( content=ft.Row([title_loaded], alignment=ft.MainAxisAlignment.CENTER), padding=ft.padding.symmetric(horizontal=25)),

                    user_label,
                    user_field,
                    system_label,
                    system_field,
                    pssw_label,
                   ft.Row([pssw_field, ft.Container( content=ft.Text(value="Gerar senha", weight=ft.FontWeight.BOLD, size= 18),
                                             width=170, height=58, bgcolor="#1D3557",
                                             alignment=ft.alignment.center,
                                             border_radius=8,
                                             on_click = gerarsenha
                                            )
                               ]),
                   ft.Row([ft.Container( content=ft.Text(value="Salvar", weight=ft.FontWeight.BOLD, size= 28),
                                             expand=1, height=58, bgcolor="#1D3557",
                                             alignment=ft.alignment.center,
                                             border_radius=8,
                                             on_click = salvar
                                            ),
                           ft.Container( content=ft.Text(value="Cancelar", weight=ft.FontWeight.BOLD, size= 18),
                                             width=170, height=58, bgcolor="#E63946",
                                             alignment=ft.alignment.center,
                                             border_radius=8,
                                             on_click = voltar_home
                                            )
                               ])  

                     ], alignment=ft.MainAxisAlignment.START, expand=1, horizontal_alignment=ft.CrossAxisAlignment.CENTER),alignment=ft.alignment.top_center,expand=True,margin=ft.margin.symmetric(30, 30),padding=ft.padding.symmetric(horizontal=100, vertical=30),border_radius=15, bgcolor="#FFFFFF", shadow=ft.BoxShadow(blur_radius=9,blur_style=ft.ShadowBlurStyle.OUTER, color="#c0c2c1"))

                    )        






            coluna= ft.Column([], expand=1)


            for i,psswd in enumerate(list_psswd(user)):
                coluna.controls.append(
                    ft.Container( content=ft.Row([
                                 ft.Row(controls=[
                                        ft.Column([ft.Text("Sistema", font_family="Poppins", size=15),
                                                ft.Text(f"{psswd[0]}", font_family="Poppins", weight=ft.FontWeight.BOLD, size=20)]),

                                        ft.Column([ft.Text("User", font_family="Poppins",  size=15),
                                                ft.Text(f"{psswd[1]}", font_family="Poppins", weight=ft.FontWeight.BOLD, size=20)]),

                                        ft.Column([ft.Text("Senha", font_family="Poppins", size=15),
                                                ft.Text(f"{psswd[2]}", font_family="Poppins", weight=ft.FontWeight.BOLD, size=20)])

                                        ],expand=1, alignment=ft.MainAxisAlignment.SPACE_AROUND),

                                        ft.Column([
                                        
                                        ft.Container( content=ft.Text(value="Excluir", weight=ft.FontWeight.BOLD, size= 18),
                                             width=130, height=38, bgcolor="#E63946",
                                             alignment=ft.alignment.center,
                                             border_radius=8,
                                             on_click = load_delete,
                                             data = i

                                            )
                                             ,
                                        ft.Container( content=ft.Text(value="Renovar",color="#000000", weight=ft.FontWeight.BOLD, size= 18), 
                                             width=130,
                                             height=38,
                                             bgcolor="#A8DADC",
                                             alignment=ft.alignment.center,
                                             border_radius=8,
                                             on_click=load_renovasenha,
                                             data= i)])

                         ], alignment=ft.MainAxisAlignment.SPACE_BETWEEN
                                        ), bgcolor="#457B9D", padding=20, margin=ft.margin.symmetric(10, 10), border_radius=10, data=i+1

                                 )

                )

            return coluna       
        
        
        
#-----------------------NOVA SENHA------------------------        
        def load_novasenha(e: ft.ControlEvent):
            novasenha(user_logado)
            
        def novasenha(user):
            user_logado = user
            
            def gerarsenha(e:ft.ControlEvent):
                pssw_field.value = gerar_senha()
                
                page.update()
            def salvar(e:ft.ControlEvent):
                if not user_field.value and not pssw_field.value and not system_field.value:
                    user_field.error_text = None
                    user_field.hint_text = None
                    user_field.height = 58
                    pssw_field.error_text = None
                    pssw_field.hint_text = None
                    pssw_field.height = 58
                    system_field.error_text = None
                    system_field.hint_text = None
                    system_field.height = 58
                    page.update()      

                    pssw_field.error_text = "Senha não informada"
                    pssw_field.height = 78
                    user_field.error_text = "Usuário não informado"
                    user_field.height = 78
                    system_field.error_text = "Sistema não informado"
                    system_field.height = 78

                elif not pssw_field.value:  
                    user_field.error_text = None    
                    user_field.hint_text = None 
                    user_field.height = 58  
                    pssw_field.error_text = None    
                    pssw_field.hint_text = None 
                    pssw_field.height = 58
                    system_field.error_text = None
                    system_field.hint_text = None
                    system_field.height = 58
                    page.update()                

                    pssw_field.error_text = "Senha não informada"
                    pssw_field.height = 78

                elif not user_field.value:
                    user_field.error_text = None
                    user_field.hint_text = None
                    user_field.height = 58
                    pssw_field.error_text = None
                    pssw_field.hint_text = None
                    pssw_field.height = 58
                    system_field.error_text = None
                    system_field.hint_text = None
                    system_field.height = 58
                    page.update()                

                    user_field.error_text = "Usuário não informado"
                    user_field.height = 78

                elif not system_field.value:
                    user_field.error_text = None
                    user_field.hint_text = None
                    user_field.height = 58
                    pssw_field.error_text = None
                    pssw_field.hint_text = None
                    pssw_field.height = 58
                    system_field.error_text = "Sistema não informado"
                    system_field.height = 78
                    page.update()
                else:
                    username = user_field.value
                    system = system_field.value
                    pssw = pssw_field.value
                    user_field.value = ""
                    system_field.value =""
                    pssw_field.value =""
                    new_psswd(user_logado, system, username, pssw)
                    load_loged(user_logado)
                page.update()
                
            def voltar_home(e: ft.ControlEvent):
                load_loged(user_logado)



              
            page.clean()
            page.add(
            ft.Container(
                ft.Column([ft.Row([logo_loaded]),
                ft.Container( content=ft.Row([title_novasenha], alignment=ft.MainAxisAlignment.CENTER), padding=ft.padding.symmetric(horizontal=25)),

                user_label,
                user_field,
                system_label,
                system_field,
                pssw_label,
               ft.Row([pssw_field, ft.Container( content=ft.Text(value="Gerar senha", weight=ft.FontWeight.BOLD, size= 18),
                                         width=170, height=58, bgcolor="#1D3557",
                                         alignment=ft.alignment.center,
                                         border_radius=8,
                                         on_click = gerarsenha
                                        )
                           ]),
               ft.Row([ft.Container( content=ft.Text(value="Salvar", weight=ft.FontWeight.BOLD, size= 28),
                                         expand=1, height=58, bgcolor="#1D3557",
                                         alignment=ft.alignment.center,
                                         border_radius=8,
                                         on_click = salvar
                                        ),
                       ft.Container( content=ft.Text(value="Cancelar", weight=ft.FontWeight.BOLD, size= 18),
                                         width=170, height=58, bgcolor="#E63946",
                                         alignment=ft.alignment.center,
                                         border_radius=8,
                                         on_click = voltar_home
                                        )
                           ])  

                 ], alignment=ft.MainAxisAlignment.START, expand=1, horizontal_alignment=ft.CrossAxisAlignment.CENTER),alignment=ft.alignment.top_center,expand=True,margin=ft.margin.symmetric(30, 30),padding=ft.padding.symmetric(horizontal=100, vertical=30),border_radius=15, bgcolor="#FFFFFF", shadow=ft.BoxShadow(blur_radius=9,blur_style=ft.ShadowBlurStyle.OUTER, color="#c0c2c1"))

                )
                
#---------------------------------LOGADO----------------        
        page.clean()
        page.vertical_alignment = ft.MainAxisAlignment.START
        cards = create_cards(user)
        cards.scroll = ft.ScrollMode.AUTO
        page.add(
            ft.Container(ft.Column([ft.Row([logo_loaded]),
            ft.Container( content=ft.Row([title_loaded, 
                ft.Container( content=ft.Text(value="Criar senha", weight=ft.FontWeight.BOLD, size= 18),width=140, height=38, bgcolor="#1D3557",alignment=ft.alignment.center,border_radius=8, on_click=load_novasenha)
                    
                ], alignment=ft.MainAxisAlignment.SPACE_BETWEEN), padding=ft.padding.symmetric(horizontal=25)),
                    cards
                
           
                 ]), expand=True,margin=ft.margin.symmetric(30, 30),padding=20,border_radius=15, bgcolor="#FFFFFF", shadow=ft.BoxShadow(blur_radius=9,blur_style=ft.ShadowBlurStyle.OUTER, color="#c0c2c1"))
        

                     )
        
        
        
        
      
    
    
        
    
        
        
   
        
        
        
    
    
    
    
    
    
    
    
    
    
    page.add(
                    logo,
                    ft.Container(
                    content=ft.Column([
                    title_login,
                    icone_user,
                    username_field,
                    icone_password,
                    password_field,
                    ft.Row([ft.Container( content=ft.Text(value="Entrar", weight=ft.FontWeight.BOLD, size= 18),
                                         width=170, height=48, bgcolor="#1D3557",
                                         alignment=ft.alignment.center,
                                         border_radius=8,
                                         on_click = on_login
                                        )
                            ,
                            ft.Container( content=ft.Text(value="Registrar", weight=ft.FontWeight.BOLD, size= 18), 
                                         width=170,
                                         height=48,
                                         bgcolor="#1D3557",
                                         alignment=ft.alignment.center,
                                         border_radius=8,
                                         on_click= on_regs)
                            
                            ],width=350
                           ,alignment=ft.MainAxisAlignment.CENTER)
                    ], alignment=ft.MainAxisAlignment.CENTER), padding=50, bgcolor="#FFFFFF", shadow=ft.BoxShadow(blur_radius=9,blur_style=ft.ShadowBlurStyle.OUTER, color="#c0c2c1"), border_radius=10)
                
            )
        
ft.app(target=main)
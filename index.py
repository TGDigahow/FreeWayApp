import flet as ft

def main(page: ft.Page):
    page.title = "SpaceMaps"
   # page.icon
    page.vertical_alignment = ft.MainAxisAlignment.START
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

    # logomarca
    logo = ft.Image(src="A:/spacemapslogo.png", width=150, height=150)

    # opções
    options = ft.Dropdown(
        label="Selecione uma opção",
        options=[
            ft.dropdown.Option("Biblioteca"),
            ft.dropdown.Option("Financeiro"),
            ft.dropdown.Option("Secretaria"),
            ft.dropdown.Option("Sala 2.3"),
        ]
    )

    # acessibilidade
    accessibility_switch = ft.Switch(label="Acessibilidade", value=False)

   
    miniplayer_container = ft.Container()

    # carregar rota 
    def carregar_rota(e):
        selected_option = options.value
        accessibility = "com acessibilidade" if accessibility_switch.value else "sem acessibilidade"

        # imagens
        image_src = ""
        if selected_option == "Biblioteca":
            image_src = "A:\mapa2.gif" if accessibility_switch.value else "A:\mapa6.gif"
        elif selected_option == "Financeiro":
            image_src = "A:\mapa3.gif" if accessibility_switch.value else "A:\mapa7.gif"
        elif selected_option == "Secretaria":
            image_src = "A:\mapa1.png" if accessibility_switch.value else "A:\mapappagaio.gif"
        elif selected_option == "Sala 2.3":
            image_src = "A:\mapa5.gif" if accessibility_switch.value else "A:\escada.gif"

        miniplayer_container.content = ft.Column([
            ft.Text(f"Destino: {selected_option} ({accessibility})"),
            ft.Image(src=image_src, width=300, height=200),
        ])
        page.update()

    # Botão para carregar rota
    carregar_rota_button = ft.ElevatedButton(text="Carregar Rota", on_click=carregar_rota)

    # componentes da página
    page.add(
        logo,
        options,
        accessibility_switch,
        carregar_rota_button,
        miniplayer_container  
    )

ft.app(target=main)

import flet as ft
import random

used_numbers = set()

def generate_unique_indian_number():
    while True:
        number = "+91 " + str(random.randint(7000000000, 9999999999))
        if number not in used_numbers:
            used_numbers.add(number)
            return number

def conversation_view(page: ft.Page) -> ft.View:
    page.window.width = 375
    page.window.height = 700
    page.window.resizable=False
    page.update()
    number_text = ft.Text("", size=18, color="white", weight="bold")

    def checkbox_changed(e):
        if e.control.value:
            number_text.value = generate_unique_indian_number()
        else:
            number_text.value = ""
        page.update()

    # Back button
    back_button = ft.Row(
        controls=[
            ft.IconButton(
                icon=ft.Icons.ARROW_BACK,
                icon_color="white",
                on_click=lambda _: page.go("/landing")
            ),
            ft.Text("Back", color="white", size=16)
        ],
        alignment=ft.MainAxisAlignment.START
    )

    # Checkbox with label
    generate_checkbox = ft.Row(
        [
            ft.Text("Generate Number", weight="bold", size=16, color="white"),
            ft.Checkbox(on_change=checkbox_changed, active_color="#7B91FF"),
        ],
        alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
    )

    # Message + checkbox container
    card = ft.Container(
        content=ft.Column(
            [
                ft.Text(
                    "For having conversation with chatbot you will need to make a call at the number below",
                    color="white",
                    size=16,
                    weight="bold",
                    text_align="center"
                ),
                ft.Container(height=20),
                generate_checkbox,
                ft.Container(height=20),
                number_text
            ],
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        ),
        width=350,
        padding=20,
        border_radius=20,
        bgcolor=ft.colors.with_opacity(0.2, "#FFFFFF"),
        blur=ft.Blur(10, 10, ft.BlurTileMode.MIRROR),
    )

    # Top nav
    # top_bar = ft.Row(
    #     [
    #         ft.IconButton(icon=ft.Icons.MENU, icon_color="white"),
    #         ft.Text("Conversation", size=22, weight="bold", color="white"),
    #         ft.IconButton(icon=ft.Icons.NOTIFICATIONS_OUTLINED, icon_color="white"),
    #     ],
    #     alignment=ft.MainAxisAlignment.SPACE_BETWEEN
    # )

    # Return View
    return ft.View(
        route="/conversation",
        controls=[
            ft.Column(
                [
                    back_button,
                    # top_bar,
                    ft.Container(height=30),
                    card
                ],
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                spacing=20
            )
        ],
        bgcolor="#000A30",
        padding=20
    )
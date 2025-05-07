import flet as ft

def start_view(page: ft.Page) -> ft.View:
    page.title = "LinguaMitra - Sign Up"
    page.window.width = 375
    page.window.height = 812
    page.window.resizable=False
    page.update()
    return ft.View(
        route="/start",
        controls=[
            ft.Text("Do you want to sign up?", size=24, weight=ft.FontWeight.BOLD),
            ft.Row([
                ft.ElevatedButton("Yes, Sign Up", on_click=lambda _: page.go("/signup")),
                ft.ElevatedButton("No, Log In", on_click=lambda _: page.go("/landing")),
            ], alignment=ft.MainAxisAlignment.CENTER, spacing=20)
        ],
        vertical_alignment=ft.MainAxisAlignment.CENTER,
        horizontal_alignment=ft.CrossAxisAlignment.CENTER
    )

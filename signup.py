import traceback,json
import flet as ft
from .firebase_config import auth

def signup_page(page: ft.Page) -> ft.View:
    page.title = "LinguaMitra - Sign Up"
    page.window_width = 400
    page.window_height = 700

    def toggle_password_visibility(e, field, icon):
        field.password = not field.password
        icon.icon = ft.icons.VISIBILITY if field.password else ft.icons.VISIBILITY_OFF
        page.update()
    
    def validate_signup(e):
        if password_input.value != confirm_password_input.value:
            sb=page.snack_bar = ft.SnackBar(content=ft.Text("Passwords don’t match"), bgcolor="red")
        else:
            try:
                print("Attempting Firebase signup…")
                user = auth.create_user_with_email_and_password(
                    email_input.value, password_input.value
                )
                print("✔️ signup succeeded:", user)
                page.snack_bar = ft.SnackBar(content=ft.Text("Account created!"), bgcolor="green")
                page.go("/login")
            except Exception as err:
                # err.args[1] is actual JSON data or a JSON-string
                raw = err.args[1]
                data = json.loads(raw) if isinstance(raw, str) else raw
                message = data["error"]["message"]
                sb = ft.SnackBar(
                    content=ft.Text(f"Error: {message}"),
                    bgcolor="red"
                )
                page.open(sb)
                page.update()


    # Gradient Background
    background = ft.Container(
        expand=True,
        gradient=ft.LinearGradient(
            begin=ft.alignment.top_center,
            end=ft.alignment.bottom_center,
            colors=["#3F5EFB", "#000A30"],
        ),
    )

    # App Title
    title = ft.Text(
        "Lingua\nMitra", 
        size=36, 
        weight=ft.FontWeight.BOLD, 
        color="white",
        text_align=ft.TextAlign.CENTER
    )



    # Input Fields
    email_input = ft.TextField(
    label="Email", width=300, bgcolor="#028090", border_radius=40,
    keyboard_type=ft.KeyboardType.EMAIL
    )

    # Password Fields with Visibility Toggle
    password_input = ft.TextField(
        label="Password", width=260, bgcolor="#028090", border_radius=40,
        password=True, max_length=12
    )
    password_visibility_icon = ft.IconButton(
        icon=ft.icons.VISIBILITY, on_click=lambda e: toggle_password_visibility(e, password_input, password_visibility_icon),
        icon_color="white"
    )
    password_row = ft.Row(
        [password_input, password_visibility_icon], alignment=ft.MainAxisAlignment.CENTER, width=300
    )

    confirm_password_input = ft.TextField(
        label="Confirm Password", width=260, bgcolor="#028090", border_radius=10,
        password=True, max_length=12
    )
    confirm_visibility_icon = ft.IconButton(
        icon=ft.icons.VISIBILITY, on_click=lambda e: toggle_password_visibility(e, confirm_password_input, confirm_visibility_icon),
        icon_color="white"
    )
    confirm_password_row = ft.Row(
        [confirm_password_input, confirm_visibility_icon], alignment=ft.MainAxisAlignment.CENTER, width=300
    )

    # Language Dropdown
    language_dropdown = ft.Dropdown(
        label="Select Language", width=300, bgcolor="#97B4FF", border_radius=10,
        options=[
            ft.dropdown.Option("Hindi"), ft.dropdown.Option("Marathi"), ft.dropdown.Option("Telugu"),
            ft.dropdown.Option("Bengali"), ft.dropdown.Option("Tamil"), ft.dropdown.Option("Gujarati"),
            ft.dropdown.Option("Kannada"), ft.dropdown.Option("Odia")
        ]
    )
        # Login & Signup Buttons
    login_button = ft.ElevatedButton(
        "Log In", width=120, bgcolor="transparent", color="white", on_click=lambda _: page.go("/login")
    )
    signup_button = ft.ElevatedButton(
        "Sign Up", width=120, bgcolor="white", color="black", on_click=validate_signup
    )
    button_row = ft.Row(
        [login_button, signup_button], alignment=ft.MainAxisAlignment.CENTER, spacing=10
    )

    # Layout
    content = ft.Column(
        [
            title,
            button_row,
            email_input,
            password_row,
            confirm_password_row,
            language_dropdown,
        ],
        alignment=ft.MainAxisAlignment.CENTER,
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        spacing=15
    )

    return ft.View(
        route="/signup",
        controls=[
            ft.Stack([background, ft.Container(content, alignment=ft.alignment.center)])
        ]
    )

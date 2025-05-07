import json
import traceback
import flet as ft
from .firebase_config import auth

def login_view(page: ft.Page) -> ft.View:
    page.title = "LinguaMitra - Log In"
    page.window_width = 400
    page.window_height = 700

    def toggle_password_visibility(e, field, icon):
        field.password = not field.password
        icon.icon = ft.icons.VISIBILITY if field.password else ft.icons.VISIBILITY_OFF
        page.update()

    def validate_login(e):
        email = email_input.value.strip()
        pwd   = password_input.value

        # Basic non‐empty check
        if not email or not pwd:
            sb = ft.SnackBar(
                content=ft.Text("Please fill in all fields"),
                bgcolor="red",
                action="OK",
                duration=3000,
            )
            page.open(sb)
            return

        try:
            # Firebase sign‐in
            user = auth.sign_in_with_email_and_password(email, pwd)
            sb = ft.SnackBar(
                content=ft.Text(f"✅ Logged in as {user['email']}"),
                bgcolor="green",
                action="OK",
                duration=3000,
            )
            page.open(sb)
            page.go("/landing")  # navigate on success
        except Exception as err:
            # print full traceback for debugging
            traceback.print_exc()
            # try to extract Firebase's JSON error message
            detail = None
            raw = err.args[1] if len(err.args) > 1 else None
            if isinstance(raw, (dict, str)):
                try:
                    data = raw if isinstance(raw, dict) else json.loads(raw)
                    detail = data["error"]["message"]
                except Exception:
                    detail = str(err)
            else:
                detail = str(err)

            sb = ft.SnackBar(
                content=ft.Text(f"❌ {detail}"),
                bgcolor="red",
                action="OK",
                duration=4000,
            )
            page.open(sb)
            page.update()

    # --- UI setup ---
    # Top tabs
    login_tab = ft.ElevatedButton(
        "Log In", width=120, bgcolor="white", color="black",
        on_click=validate_login
    )
    signup_tab = ft.ElevatedButton(
        "Sign Up", color="white",
        on_click=lambda _: page.go("/signup")
    )
    tab_row = ft.Row([login_tab, signup_tab],
                     alignment=ft.MainAxisAlignment.CENTER, spacing=10)

    # Form fields
    email_input = ft.TextField(
        label="Email", width=300, bgcolor="#028090", border_radius=40,
        keyboard_type=ft.KeyboardType.EMAIL
    )
    password_input = ft.TextField(
        label="Password", width=260, bgcolor="#028090", border_radius=40,
        password=True, max_length=128
    )
    pw_icon = ft.IconButton(
        icon=ft.icons.VISIBILITY, icon_color="white",
        on_click=lambda e: toggle_password_visibility(e, password_input, pw_icon)
    )
    password_row = ft.Row([password_input, pw_icon],
                          alignment=ft.MainAxisAlignment.CENTER, width=300)

    # Main login button
    login_main_button = ft.ElevatedButton(
        "Log In", width=300, bgcolor="white", color="black",
        on_click=validate_login
    )

    content = ft.Column(
        [
            ft.Text("Lingua\nMitra",
                    size=36,
                    weight=ft.FontWeight.BOLD,
                    color="white",
                    text_align=ft.TextAlign.CENTER),
            tab_row,
            email_input,
            password_row,
            login_main_button
        ],
        alignment=ft.MainAxisAlignment.CENTER,
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        spacing=15
    )

    background = ft.Container(
        expand=True,
        gradient=ft.LinearGradient(
            begin=ft.alignment.top_center,
            end=ft.alignment.bottom_center,
            colors=["#3F5EFB", "#000A30"]
        )
    )

    return ft.View(
        route="/login",
        controls=[ft.Stack([background,
                            ft.Container(content, alignment=ft.alignment.center)])]
    )

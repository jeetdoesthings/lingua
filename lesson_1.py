import flet as ft
from .flashcard import flashcards_view
from .quiz import quiz_view
from .match import match_view

def lesson_1_view(page: ft.Page):
    page.title = "Lesson 1"
    page.bgcolor = "#0A1B57"
    page.padding = ft.padding.all(20)
    page.window.width = 375
    page.window.height = 700
    page.window.resizable=False
    page.update()

    # Navigation function
    def go_to(route):
        page.views.clear()
        if route == "/":
            page.views.append(main_view())
        elif route == "/flashcards":
            page.views.append(flashcards_view(page))
        elif route == "/quiz":
            page.views.append(quiz_view(page))
        elif route == "/match":
            page.views.append(match_view(page))
        page.update()

    # Reusable card-button component
    def nav_button(icon, title, subtitle, route):
        return ft.ElevatedButton(
            on_click=lambda _: go_to(route),
            style=ft.ButtonStyle(
                bgcolor="#1A2B6B",
                padding=20,
                shape=ft.RoundedRectangleBorder(radius=15),
                shadow_color="black26",
                elevation=8
            ),
            content=ft.Row([
                ft.Icon(icon, color="#9EB7FF", size=30),
                ft.Column([
                    ft.Text(title, weight="bold", size=16, color="white"),
                    ft.Text(subtitle, size=12, color="white70")
                ], alignment="center", spacing=2)
            ], alignment="start", spacing=10)
        )

    # Main view with buttons
    def main_view():
        return ft.View(
            route="/lesson_1",
            controls=[
                ft.AppBar(
                    title=ft.Text("Lesson 1", weight="bold", size=18),
                    bgcolor="#0A1B57",
                    leading=ft.IconButton(icon=ft.icons.ARROW_BACK, bgcolor="0A1B57",on_click=lambda _:page.go('/lessons')),
                    actions=[ft.IconButton(icon=ft.icons.NOTIFICATIONS_NONE, icon_color="white")]
                ),
                ft.Text("Lesson 1", size=24, weight="bold", color="white"),
                nav_button(ft.icons.NOTE_ALT_OUTLINED, "Flash Cards", "Refine Your Vocabulary", "/flashcards"),
                nav_button(ft.icons.CHECK_BOX_OUTLINE_BLANK, "Quizz", "Guess the correct answers", "/quiz"),
                nav_button(ft.icons.SWAP_HORIZ_OUTLINED, "Match The Correct Pair", "Test Your Knowledge", "/match")
            ],
            bgcolor="#0A1B57",
            padding=20
        )

    # Content view with Back button
    def content_view(title, subtitle):
        return ft.View(
            route=f"/{title.lower().replace(' ', '')}",
            controls=[
                # ft.AppBar(
                #     title=ft.Text(title, weight="bold", size=18),
                #     bgcolor="#0A1B57",
                #     leading=ft.IconButton(icon=ft.icons.ARROW_BACK, icon_color="white", on_click=lambda _: go_to("/lessons"))
                # ),
                ft.Container(
                    ft.Text(f"{title}\n{subtitle}", size=20, color="white", weight="bold"),
                    padding=30,
                )
            ],
            bgcolor="#0A1B57"
        )
        
    return main_view()


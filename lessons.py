import flet as ft

def lessons_view(page: ft.Page) -> ft.View:
    page.window.width = 375
    page.window.height = 700
    page.window.resizable=False
    page.update()    
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

    return ft.View(
        route="/lessons",
        controls=[
            ft.Text("Lessons Stack", size=24, weight=ft.FontWeight.BOLD),
            ft.Column(
                [
                    back_button,
                    # Lesson 1
                    ft.ElevatedButton(
                        on_click=lambda _: page.go("/lesson_1"),
                        content=ft.Row(
                            [
                                ft.Icon(ft.icons.LOOKS_ONE, size=40, color="white"),
                                ft.Column(
                                    [
                                        ft.Text("Lesson 1", size=18, weight=ft.FontWeight.BOLD, color="white"),
                                        ft.Text("Introduction to Basic Words", size=14, color="white70"),
                                    ],
                                    spacing=2
                                ),
                            ],
                            alignment=ft.MainAxisAlignment.START,
                            spacing=20
                        ),
                        style=ft.ButtonStyle(
                            padding=20,
                            bgcolor=ft.colors.with_opacity(0.15, "white"),
                            shape=ft.RoundedRectangleBorder(radius=20),
                        ),
                    ),
                    # Lesson 2
                    ft.ElevatedButton(
                        on_click=lambda _: page.go("/lesson_2"),
                        content=ft.Row(
                            [
                                ft.Icon(ft.icons.SPORTS_SOCCER, size=40, color="white"),
                                ft.Column(
                                    [
                                        ft.Text("Lesson 2", size=18, weight=ft.FontWeight.BOLD, color="white"),
                                        ft.Text("Introduction to Sports", size=14, color="white70"),
                                    ],
                                    spacing=2
                                ),
                            ],
                            alignment=ft.MainAxisAlignment.START,
                            spacing=20
                        ),
                        style=ft.ButtonStyle(
                            padding=20,
                            bgcolor=ft.colors.with_opacity(0.15, "white"),
                            shape=ft.RoundedRectangleBorder(radius=20),
                        ),
                    ),
                    # Lesson 3
                    ft.ElevatedButton(
                        on_click=lambda _: page.go("/lesson_3"),
                        content=ft.Row(
                            [
                                ft.Icon(ft.icons.GROUP, size=40, color="white"),
                                ft.Column(
                                    [
                                        ft.Text("Lesson 3", size=18, weight=ft.FontWeight.BOLD, color="white"),
                                        ft.Text("Phrases Used in Daily Life", size=14, color="white70"),
                                    ],
                                    spacing=2
                                ),
                            ],
                            alignment=ft.MainAxisAlignment.START,
                            spacing=20
                        ),
                        style=ft.ButtonStyle(
                            padding=20,
                            bgcolor=ft.colors.with_opacity(0.15, "white"),
                            shape=ft.RoundedRectangleBorder(radius=20),
                        ),
                    ),
                    # Lesson 4
                    ft.ElevatedButton(
                        on_click=lambda _: page.go("/lesson_4"),
                        content=ft.Row(
                            [
                                ft.Icon(ft.icons.CHECKLIST, size=40, color="white"),
                                ft.Column(
                                    [
                                        ft.Text("Lesson 4", size=18, weight=ft.FontWeight.BOLD, color="white"),
                                        ft.Text("Most Used Sentences", size=14, color="white70"),
                                    ],
                                    spacing=2
                                ),
                            ],
                            alignment=ft.MainAxisAlignment.START,
                            spacing=20
                        ),
                        style=ft.ButtonStyle(
                            padding=20,
                            bgcolor=ft.colors.with_opacity(0.15, "white"),
                            shape=ft.RoundedRectangleBorder(radius=20),
                        ),
                    ),
                    # Lesson 5
                    ft.ElevatedButton(
                        on_click=lambda _: page.go("/lesson_5"),
                        content=ft.Row(
                            [
                                ft.Icon(ft.icons.IMPORT_CONTACTS, size=40, color="white"),
                                ft.Column(
                                    [
                                        ft.Text("Lesson 5", size=18, weight=ft.FontWeight.BOLD, color="white"),
                                        ft.Text("Introductions to Self", size=14, color="white70"),
                                    ],
                                    spacing=2
                                ),
                            ],
                            alignment=ft.MainAxisAlignment.START,
                            spacing=20
                        ),
                        style=ft.ButtonStyle(
                            padding=20,
                            bgcolor=ft.colors.with_opacity(0.15, "white"),
                            shape=ft.RoundedRectangleBorder(radius=20),
                        ),
                    ),
                ],
                scroll=ft.ScrollMode.AUTO,
                alignment=ft.MainAxisAlignment.START,
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                spacing=15,
            )
        ],
        vertical_alignment=ft.MainAxisAlignment.START,
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
    )

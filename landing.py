# import flet as ft

# def landing_view(page: ft.Page):
#     return ft.View(
#         route="/landing",
#         controls=[
#             ft.Container(
#                 content=ft.Column(
#                     [
#                         ft.Text("Welcome Tanay!", size=28, weight=ft.FontWeight.BOLD, color="white"),
#                         ft.Text("Choose Your Learning Mode", size=16, color="white"),
#                         ft.Container(height=20),  # Spacing
#                         ft.Container(
#                             content=ft.ElevatedButton(
#                                 content=ft.Row(
#                                     [
#                                         ft.Icon(ft.icons.HEADSET_MIC, color="white"),
#                                         ft.Container(width=10),  # Space between icon and text
#                                         ft.Text("Chat Bot Conversations", size=16, color="white"),
#                                     ],
#                                     alignment=ft.MainAxisAlignment.CENTER,
#                                 ),
#                                 style=ft.ButtonStyle(
#                                     shape=ft.RoundedRectangleBorder(radius=8),
#                                     overlay_color=ft.colors.TRANSPARENT,
#                                 ),
#                                 bgcolor="#AFCBFF",
#                                 width=320,
#                                 height=56,
#                                 on_click=lambda _: page.go("/chatbot"),
#                             ),
#                             padding=10,
#                         ),
#                         ft.Container(
#                             content=ft.ElevatedButton(
#                                 content=ft.Row(
#                                     [
#                                         ft.Icon(ft.icons.BOOK, color="white"),
#                                         ft.Container(width=10),  # Space between icon and text
#                                         ft.Text("Lessons", size=16, color="white"),
#                                     ],
#                                     alignment=ft.MainAxisAlignment.CENTER,
#                                 ),
#                                 style=ft.ButtonStyle(
#                                     shape=ft.RoundedRectangleBorder(radius=8),
#                                     overlay_color=ft.colors.TRANSPARENT,
#                                 ),
#                                 bgcolor="#AFCBFF",
#                                 width=320,
#                                 height=56,
#                                 on_click=lambda _: page.go("/lessons"),
#                             ),
#                             padding=10,
#                         ),
#                     ],
#                     spacing=0,
#                     alignment=ft.MainAxisAlignment.START,
#                     horizontal_alignment=ft.CrossAxisAlignment.CENTER,
#                 ),
#                padding=20,
#                   width=400,
#                 expand=True,
#                 bgcolor="#00194A",  # Deep blue background as in your image
#            )
#         ],
#         bgcolor="#00194A",  # Ensuring the background color is set at the View level too
#     )


import flet as ft

def landing_view(page: ft.Page):
    page.window.width = 375
    page.window.height = 700
    page.window.resizable=False
    page.update()
    def handle_menu_click(e):
        choice = e.control.content.value
        if choice == "Leader Board":
            page.go("/leaderboard")
        elif choice == "Friends":
            page.go("/friends")
        elif choice == "Progress":
            page.go('/progress_stat_bar')
        elif choice == "Log out":
            page.go('/signup')

    menubar = ft.MenuBar(
        expand=True,
        controls=[
            ft.SubmenuButton(
                content=ft.Text("📒 Menu", color="white"),
                controls=[
                    ft.MenuItemButton(
                        content=ft.Text("Leader Board"),
                        on_click=handle_menu_click
                    ),
                    ft.MenuItemButton(
                        content=ft.Text("Friends"),
                        on_click=handle_menu_click
                    ),
                    ft.MenuItemButton(
                        content=ft.Text("Progress"),
                        on_click=handle_menu_click
                    ),
                    ft.MenuItemButton(
                        content=ft.Text("Log out"),
                        on_click=handle_menu_click
                    ),
                ]
            )
        ]
    )

    return ft.View(
        route="/landing",
        controls=[
            ft.Container(
                content=ft.Column(
                    [
                        ft.Row(
                            [menubar],
                            alignment=ft.MainAxisAlignment.START,
                        ),
                        ft.Container(height=20),
                        ft.Text("Welcome Tanay!", size=28, weight=ft.FontWeight.BOLD, color="white"),
                        ft.Text("Choose Your Learning Mode", size=16, color="white"),
                        ft.Container(
                            content=ft.ElevatedButton(
                                content=ft.Row(
                                    [
                                        ft.Icon(ft.icons.HEADSET_MIC, color="white"),
                                        ft.Container(width=10),  # Space between icon and text
                                        ft.Text("Chat Bot Conversations", size=16, color="white"),
                                    ],
                                    alignment=ft.MainAxisAlignment.CENTER,
                                ),
                                style=ft.ButtonStyle(
                                    shape=ft.RoundedRectangleBorder(radius=8),
                                    overlay_color=ft.colors.TRANSPARENT,
                                ),
                                bgcolor="#AFCBFF",
                                width=320,
                                height=56,
                                on_click=lambda _: page.go("/conversation"),
                            ),
                            padding=10,
                        ),
                        ft.Container(
                            content=ft.ElevatedButton(
                                content=ft.Row(
                                    [
                                        ft.Icon(ft.icons.BOOK, color="white"),
                                        ft.Container(width=10),  # Space between icon and text
                                        ft.Text("Lessons", size=16, color="white"),
                                    ],
                                    alignment=ft.MainAxisAlignment.CENTER,
                                ),
                                style=ft.ButtonStyle(
                                    shape=ft.RoundedRectangleBorder(radius=8),
                                    overlay_color=ft.colors.TRANSPARENT,
                                ),
                                bgcolor="#AFCBFF",
                                width=320,
                                height=56,
                                on_click=lambda _: page.go("/lessons"),
                            ),
                            padding=10,
                        ),
                    ],
                    spacing=0,
                    alignment=ft.MainAxisAlignment.START,
                    horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                ),
                width=400,
                expand=True,
                bgcolor="#00194A",
                padding=20,
                alignment=ft.alignment.top_center,
            )
        ],
        bgcolor="#00194A",
    )

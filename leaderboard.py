import flet as ft

def get_rank_content(rank):
    """Creates rank content based on position (medal for top 3, number for others)"""
    if rank == 1:
        return ft.Icon(ft.icons.EMOJI_EVENTS, color=ft.colors.AMBER_500, size=24)
    elif rank == 2:
        return ft.Icon(ft.icons.EMOJI_EVENTS, color=ft.colors.GREY_400, size=24)
    elif rank == 3:
        return ft.Icon(ft.icons.EMOJI_EVENTS, color=ft.colors.ORANGE_800, size=24)
    else:
        return ft.Text(f"{rank}.", color="white", weight=ft.FontWeight.BOLD, size=18)

def leaderboard_row(rank, name: str, score: str, page: ft.Page) -> ft.Row:
    rank_num = int(rank.replace(".", "")) if isinstance(rank, str) else rank
    return ft.Row(
        controls=[
            ft.Container(
                content=get_rank_content(rank_num),
                width=40,
                height=40,
                alignment=ft.alignment.center,
            ),
            ft.Row(
                controls=[
                    ft.CircleAvatar(
                        content=ft.Icon(ft.icons.PERSON, color=ft.colors.WHITE, size=16),
                        bgcolor=ft.colors.BLUE_400,
                        radius=15,
                    ),
                    ft.Container(width=10),
                    ft.Text(name, color="white", weight=ft.FontWeight.BOLD, size=18),
                ],
                spacing=0,
                expand=True,
                alignment=ft.MainAxisAlignment.START
            ),
            ft.Container(
                content=ft.Text(score, color="white", weight=ft.FontWeight.BOLD, size=18),
                alignment=ft.alignment.center_right
            ),
        ],
        spacing=10,
        vertical_alignment=ft.CrossAxisAlignment.CENTER,
        height=50,
    )

def leader_view(page: ft.Page) -> ft.View:
    page.window.width = 375
    page.window.height = 700
    page.window.resizable=False
    page.update()
    users = [
        {"rank": 1, "name": "Username1", "score": "100000 XP"},
        {"rank": 2, "name": "Username2", "score": "95000 XP"},
        {"rank": 3, "name": "Username3", "score": "85000 XP"},
        {"rank": "4.", "name": "Username4", "score": "75000 XP"},
        {"rank": "5.", "name": "Username5", "score": "65000 XP"},
        {"rank": "6.", "name": "Username6", "score": "50000 XP"},
    ]
    back_button = ft.Row(
        controls=[
            ft.IconButton(
                icon=ft.Icons.ARROW_BACK,
                icon_color="white",
                on_click=lambda _: page.go("/landing")  # Navigate to home or previous page
            ),
            ft.Text("Back", color="white", size=16)
        ],
        alignment=ft.MainAxisAlignment.START
    )
    leaderboard_rows = [leaderboard_row(user["rank"], user["name"], user["score"], page) for user in users]

    return ft.View(
        route="/leaderboard",
        bgcolor="#031956",
        scroll="auto",
        padding=20,
        controls=[
            ft.Column(
                controls=[
                    back_button,
                    ft.Text("Leader Board", 
                            style="headlineMedium", 
                            weight=ft.FontWeight.BOLD, 
                            color="white"),
                    ft.Container(height=80),
                    ft.Container(
                        content=ft.Column(
                            controls=leaderboard_rows,
                            spacing=10,
                        ),
                        width=350,
                        padding=20,
                        border_radius=20,
                        bgcolor=ft.colors.with_opacity(0.2, ft.colors.WHITE),
                        shadow=ft.BoxShadow(
                            spread_radius=1,
                            blur_radius=15,
                            color=ft.colors.with_opacity(0.2, ft.colors.WHITE),
                            offset=ft.Offset(0, 0),
                        ),
                        border=ft.border.all(
                            width=1,
                            color=ft.colors.with_opacity(0.3, ft.colors.WHITE)
                        ),
                    )
                ],
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                alignment=ft.MainAxisAlignment.CENTER,
                expand=True
            )
        ]
    )

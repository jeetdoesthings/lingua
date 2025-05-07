import flet as ft

def leaderboard_row(rank: str, name: str) -> ft.Row:
    return ft.Row(
        controls=[
            # Left section with rank
            ft.Container(
                content=ft.Text(rank, color="white", weight=ft.FontWeight.BOLD, size=18),
                width=50,
                alignment=ft.alignment.center_left
            ),
            
            # Middle section with avatar and username that expands to fill available space
            ft.Container(
                content=ft.Row(
                    controls=[
                        # Avatar circle with icon
                        ft.CircleAvatar(
                            content=ft.Icon(ft.icons.PERSON, color=ft.colors.WHITE, size=16),
                            bgcolor=ft.colors.BLUE_400,
                            radius=15,
                        ),
                        ft.Container(width=10),  # Spacing
                        ft.Text(name, color="white", weight=ft.FontWeight.BOLD, size=18),
                    ],
                    spacing=0,
                ),
                expand=True,  # This container will expand to fill available space
            ),
        ],
        width=400,  # Set a fixed width for the entire row
        spacing=10,
        vertical_alignment=ft.CrossAxisAlignment.CENTER,
        height=50,
    )

def friends_view(page: ft.Page) -> ft.View:
    page.window.width = 375
    page.window.height = 700
    page.window.resizable=False
    page.update()
    # User data
    users = [
        {"rank": "1.", "name": "Username1"},
        {"rank": "2.", "name": "Username2"},
        {"rank": "3.", "name": "Username3"},
        {"rank": "4.", "name": "Username4"},
        {"rank": "5.", "name": "Username5"},
        {"rank": "6.", "name": "Username6"},
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
    # Create rows for the leaderboard
    leaderboard_rows = []
    for user in users:
        leaderboard_rows.append(
            leaderboard_row(user["rank"], user["name"])
        )
    
    leaderboard_container = ft.Container(
        content=ft.Column(
            controls=[
                ft.Text("Friends", 
                       style="headlineMedium", 
                       weight=ft.FontWeight.BOLD, 
                       color="white"),
                
                # Space between heading and table
                ft.Container(height=80),
                
                # Transparent glassy container - making it fill more width
                ft.Container(
                    content=ft.Column(
                        controls=leaderboard_rows,
                        spacing=10,
                        # Make the column take full width of its container
                        width=400,
                    ),
                    width=400,  # Increased from 350 to fill more space
                    padding=20,
                    border_radius=20,
                    bgcolor=ft.colors.with_opacity(0.2, ft.colors.WHITE),  # Transparent white
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
        ),
        alignment=ft.alignment.center,
        expand=True,
    )
    
    # Return the ft.View object
    return ft.View(
        route="/friends",
        controls=[back_button,leaderboard_container],
        bgcolor="#031956",  # Dark blue background
        scroll="auto",
    )

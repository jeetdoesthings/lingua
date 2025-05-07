import flet as ft
import asyncio

async def landing_1_view(page: ft.Page):
    async def door_click(route, door: ft.Container):
        door.scale = 10
        door.border_radius = 0
        door.animate_scale = ft.animation.Animation(600, "easeInOut")
        door.update()

        await asyncio.sleep(0.6)  # Wait for zoom to finish
        return route

    features = [
        ("🧠 Lessons", "/lessons"),
        ("🗣️ Chatbot conversation", "/chatbot"),
        ("📊 Progress", "/progress"),
        ("💪 Leaderboard", "/leaderboard")
    ]

    doors = []

    for icon, route in features:
        door = ft.Container(
            width=120,
            height=220,
            bgcolor=ft.colors.BROWN_200,
            border_radius=20,
            scale=1,
            animate_scale=ft.animation.Animation(300, "easeInOut"),
            alignment=ft.alignment.center,
            content=ft.Column([  
                ft.Text(icon, size=40),
                ft.Text("Enter", size=14, color=ft.colors.WHITE)
            ], alignment="center", horizontal_alignment="center"),
            on_click=lambda e, r=route, d=None: asyncio.create_task(door_click(r, e.control)),
            ink=True,
            margin=10
        )
        doors.append(door)

    # Return the landing view as a ft.View
    return ft.View(
        route="/landing_1",  # Specify the route for the view
        controls=[  
            ft.AppBar(title=ft.Text("🚪 Choose Your Door")),
            ft.Column([  
                ft.Text("Choose Your Door", size=30, weight="bold", color=ft.colors.AMBER_100),
                ft.Row(doors, alignment="center"),
                ft.Text("Step through the portal to your next destination.", italic=True, size=16, color=ft.colors.GREY_400)
            ], alignment="center", horizontal_alignment="center"),
        ],
        vertical_alignment=ft.MainAxisAlignment.CENTER,
        horizontal_alignment=ft.CrossAxisAlignment.CENTER
    )

import flet as ft
from .progress_stat_pie import progress_stat_pie_view

def progress_stat_bar_view(page: ft.Page):
    page.window.width = 375
    page.window.height = 812
    page.window.resizable=False
    page.update()
    # Chart data and reference list
    chart_data = [10, 23, 17, 22, 15, 21, 28]
    bar_refs = []

    def create_bar(x, y):
        bar = ft.BarChartGroup(
            x=x,
            bar_rods=[
                ft.BarChartRod(
                    from_y=0,
                    to_y=y,
                    color="#ADB8FF",
                    width=20,
                    tooltip=f"{y} min",
                    border_radius=ft.BorderRadius(top_left=6, top_right=6, bottom_left=0, bottom_right=0),
                )
            ]
        )
        bar_refs.append(bar)
        return bar

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
    # Navigation buttons
    stat_button = ft.ElevatedButton(
        "Statistics",
        style=ft.ButtonStyle(
            shape=ft.RoundedRectangleBorder(radius=6),
            bgcolor="#1A2C65",
            color="white",
        ),
        on_click=lambda _: page.go('/progress_stat_bar'),
        
    )

    cal_button = ft.ElevatedButton(
        "Calendar",
        style=ft.ButtonStyle(
            shape=ft.RoundedRectangleBorder(radius=6),
            bgcolor="#1A2C65",
            color="white",
        ),
        on_click=lambda _: page.go('/calender'),
    )
    

    # Toggle switch for chart type
    toggle = ft.Switch(
        label="Switch to Pie",
        value=False,
        scale=0.7,
        on_change=lambda _: page.views.append(progress_stat_pie_view(page))
    )

    # Bar chart
    chart = ft.BarChart(
        bar_groups=[create_bar(i, y) for i, y in enumerate(chart_data)],
        border=ft.border.all(1, "white"),
        left_axis=ft.ChartAxis(
            labels=[
                ft.ChartAxisLabel(value=i, label=ft.Text(f"{int(i)} min", size=12, color="white"))
                for i in range(0, 50, 10)
            ],
            labels_size=40,
        ),
        bottom_axis=ft.ChartAxis(
            labels=[
                ft.ChartAxisLabel(value=i, label=ft.Text(day, color="white"))
                for i, day in enumerate(["M", "T", "W", "T", "F", "S", "S"])
            ],
            labels_size=30,
        ),
        horizontal_grid_lines=ft.ChartGridLines(color="white", width=0.5),
        vertical_grid_lines=ft.ChartGridLines(color="transparent"),
        max_y=50,
        min_y=0,
        tooltip_bgcolor="#EB06FF",
        expand=True,
    )

    # Return ft.View instead of modifying page directly
    return ft.View(
        route="/progress_stat_bar",
        controls=[
            ft.Column([
                back_button,
                ft.Text("Progress", size=28, weight=ft.FontWeight.BOLD, color="white", text_align="center"),
                ft.Row([stat_button, cal_button], alignment=ft.MainAxisAlignment.CENTER, spacing=20),
                ft.Container(height=30),
                ft.Container(
                    content=ft.Column([
                        ft.Row([
                            ft.Text("Time Spent", size=16, weight=ft.FontWeight.BOLD, color="white"),
                            ft.Container(content=toggle, alignment=ft.alignment.center_right, expand=True)
                        ], alignment=ft.MainAxisAlignment.SPACE_BETWEEN),
                        ft.Container(height=20),
                        chart
                    ]),
                    padding=20,
                    border_radius=20,
                    bgcolor=ft.colors.with_opacity(0.2, "white"),
                    width=350,
                ),
            ],
                alignment=ft.MainAxisAlignment.START,
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            )
        ],
        bgcolor="#031956",  padding=20)

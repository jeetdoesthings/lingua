import flet as ft
from flet.plotly_chart import PlotlyChart
import plotly.graph_objects as go

def progress_stat_pie_view(page: ft.Page):
    # Pie chart data
    labels = ["Conversation", "Flash Cards", "Quiz & Match"]
    values = [45, 30, 25]
    time_spent = ["3h 15m", "2h 10m", "1h 45m"]

    # Create the pie chart
    fig = go.Figure(data=[
        go.Pie(
            labels=labels,
            values=values,
            hole=0.5,
            hoverinfo="label+percent",
            hovertemplate="%{label}<br>%{percent}<br>Time: %{customdata}<extra></extra>",
            customdata=time_spent,
            textinfo="label",
            textfont=dict(
                color="white",
                size=14,
                family="Poppins"
            ),
            marker=dict(
                colors=["#FF00FF", "#A761CF", "#59C3F0"],
                line=dict(color="#2A3B7D", width=0)
            ),
            pull=[0, 0, 0],
            hoverlabel=dict(
                bgcolor="#000A30",
                font=dict(size=14, color="white")
            )
        )
    ])

    fig.update_layout(
        paper_bgcolor="#2A3B7D",
        plot_bgcolor="#2A3B7D",
        font=dict(color="white", family="Poppins", size=16),
        margin=dict(t=10, b=10, l=10, r=10),
        showlegend=True,
        legend=dict(
            orientation="h",
            y=-0.15,
            x=0.5,
            xanchor="center",
            font=dict(size=14, family="Poppins")
        ),
        hovermode="closest",
        height=380,
        width=380,
    )

    pie_chart = PlotlyChart(fig, expand=True)

    def handle_toggle_change(e):
        if not e.control.value:  # When switching back to bar chart
            on_change=lambda _: page.go('/progress_stat_bar')
        page.update()

    # Update toggle with handler
    toggle = ft.Switch(
        value=True,  # Start as True since we're in pie view
        thumb_color=ft.colors.WHITE,
        track_color="#3F5EFB",
        active_color="#3F5EFB",
        scale=0.7,
        on_change=handle_toggle_change
    )

    toggle_container = ft.Container(
        content=ft.Row(
            [
                ft.Image(
                    src="https://cdn-icons-png.flaticon.com/512/2972/2972385.png",
                    width=16,
                    height=16
                ),
                toggle
            ],
            spacing=2,
            alignment=ft.MainAxisAlignment.CENTER
        ),
        padding=3,
        bgcolor="#1A2C65",
        border_radius=15,
        width=65,
        height=30
    )

    # Header bar
    header = ft.Row(
        [
            ft.Icon(ft.icons.MENU, color="white"),
            ft.Text("Progress", size=24, weight="bold", color="white", expand=True, text_align="center"),
            ft.Icon(ft.icons.NOTIFICATIONS_NONE_OUTLINED, color="white")
        ],
        alignment=ft.MainAxisAlignment.SPACE_BETWEEN
    )

    # Navigation buttons centered
    nav_buttons = ft.Row(
        [
            ft.ElevatedButton("Statistics", bgcolor="#1A2C65", color="white"),
            ft.ElevatedButton("Calendar", bgcolor="#1A2C65", color="white")
        ],
        spacing=20,
        alignment=ft.MainAxisAlignment.CENTER
    )

    # Title row with toggle
    title_row = ft.Row(
        [
            ft.Text("Time Spent", color="white", weight="bold", size=18),
            toggle_container
        ],
        alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
        vertical_alignment=ft.CrossAxisAlignment.CENTER
    )

    # Create a container for the chart
    chart_container = ft.Container(
        content=pie_chart,
        expand=True,
        padding=10
    )

    # Create a container for the centered text
    text_container = ft.Container(
        content=ft.Column(
            [
                ft.Text(
                    "Different\nLearning\nMethods",
                    color="white",
                    weight="bold",
                    size=16,
                    text_align="center"
                )
            ],
            alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER
        ),
        width=380,
        height=380,
        alignment=ft.alignment.center,
        margin=ft.margin.only(top=-40)
    )

    # Combined stack with improved positioning
    chart_with_text = ft.Stack(
        [
            chart_container,
            text_container
        ],
        width=380,
        height=380
    )

    chart_card = ft.Container(
        content=ft.Column(
            [
                title_row,
                ft.Container(
                    content=chart_with_text,
                    alignment=ft.alignment.center,
                    padding=10
                )
            ],
            spacing=10,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER
        ),
        width=430,
        padding=ft.padding.only(left=20, right=20, top=20, bottom=10),
        border_radius=20,
        bgcolor="#2A3B7D",
        height=550
    )

    # Return the ft.View object
    return ft.View(
        route="/progress_stat_pie",
        controls=[
            ft.Column(
                [
                    header,
                    ft.Container(
                        content=nav_buttons,
                        alignment=ft.alignment.center
                    ),
                    chart_card
                ],
                spacing=20,
                horizontal_alignment=ft.CrossAxisAlignment.CENTER
            )
        ],
        bgcolor="#000A30",
        scroll=ft.ScrollMode.AUTO,
    )
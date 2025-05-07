import flet as ft
import calendar
from datetime import datetime, timedelta

def calender_view(page: ft.Page) -> ft.View:
    page.window.width = 375
    page.window.height = 700
    page.window.resizable=False
    page.update()
    # Starting month and year
    current_date = datetime.today()
    selected_month = current_date.month
    selected_year = current_date.year

    study_data = {
        "2025-04-10": "studied",
        "2025-04-11": "studied",
        "2025-04-12": "studied",
        "2025-04-13": "studied",
        "2025-04-15": "studied",
        "2025-04-20": "studied"
    }

    calendar_grid = ft.Column(spacing=5, alignment="center")

    def update_calendar():
        calendar_grid.controls.clear()
        month_label.value = f"{calendar.month_name[selected_month]} {selected_year}"

        month_days = calendar.monthcalendar(selected_year, selected_month)
        streak_days = get_streak_days(study_data)

        for week in month_days:
            week_row = ft.Row(spacing=5, alignment="center")
            for day in week:
                if day == 0:
                    week_row.controls.append(ft.Container(width=40, height=40))
                else:
                    date_str = f"{selected_year}-{selected_month:02d}-{day:02d}"
                    status = study_data.get(date_str, "not_studied")

                    color = "#2C3E50"
                    emoji = ""

                    if date_str in streak_days:
                        color = "#E67E22"
                        emoji = "🔥"
                    elif status == "studied":
                        color = "#3498DB"

                    week_row.controls.append(
                        ft.Container(
                            content=ft.Text(f"{day}{emoji}", color="white", size=14),
                            width=40,
                            height=40,
                            bgcolor=color,
                            alignment=ft.alignment.center,
                            border_radius=8
                        )
                    )
            calendar_grid.controls.append(week_row)
        page.update()

    def get_streak_days(data):
        streak_days = set()
        sorted_dates = sorted(data.keys())

        count = 0
        temp_streak = []

        for i in range(len(sorted_dates)):
            date_obj = datetime.strptime(sorted_dates[i], "%Y-%m-%d")
            if data[sorted_dates[i]] == "studied":
                if i == 0 or (date_obj - datetime.strptime(sorted_dates[i - 1], "%Y-%m-%d")).days == 1:
                    count += 1
                    temp_streak.append(sorted_dates[i])
                else:
                    if count >= 3:
                        streak_days.update(temp_streak)
                    count = 1
                    temp_streak = [sorted_dates[i]]
            else:
                if count >= 3:
                    streak_days.update(temp_streak)
                count = 0
                temp_streak = []

        if count >= 3:
            streak_days.update(temp_streak)

        return streak_days

    def next_month(e):
        nonlocal selected_month, selected_year
        selected_month += 1
        if selected_month > 12:
            selected_month = 1
            selected_year += 1
        update_calendar()

    def prev_month(e):
        nonlocal selected_month, selected_year
        selected_month -= 1
        if selected_month < 1:
            selected_month = 12
            selected_year -= 1
        update_calendar()

    # Back Button
    back_button = ft.Row(
        controls=[
            ft.IconButton(
                icon=ft.Icons.ARROW_BACK,  # Updated to new Icons enum
                icon_color="white",
                on_click=lambda _: page.go("/progress_stat_bar")
            ),
            ft.Text("Back", color="white", size=16)
        ],
        alignment="start"
    )

    # Month navigation header
    header = ft.Row(
        controls=[
            ft.IconButton(
                icon=ft.Icons.ARROW_BACK_IOS_NEW,  # Updated to new Icons enum
                icon_color="white",
                on_click=prev_month
            ),
            ft.Text("", size=26, weight="bold", color="white", key="month_label"),
            ft.IconButton(
                icon=ft.Icons.ARROW_FORWARD_IOS,  # Updated to new Icons enum
                icon_color="white",
                on_click=next_month
            ),
        ],
        alignment="center"
    )
    month_label = header.controls[1]

    # Legend
    legend = ft.Row(
        controls=[
            ft.Container(width=20, height=20, bgcolor="#2C3E50", border_radius=4),
            ft.Text("Not Studied", color="white"),
            ft.Container(width=20, height=20, bgcolor="#3498DB", border_radius=4),
            ft.Text("Studied", color="white"),
            ft.Container(width=20, height=20, bgcolor="#E67E22", border_radius=4),
            ft.Text("🔥 Streak", color="white"),
        ],
        spacing=10,
        alignment="center"
    )

    # Main content
    content = ft.Column(
        controls=[
            back_button,
            ft.Container(height=20),
            header,
            ft.Container(height=30),
            calendar_grid,
            ft.Container(height=30),
            legend
        ],
        alignment="center",
        horizontal_alignment="center",
        spacing=10
    )

    # Initialize calendar
    update_calendar()

    # Return the View
    return ft.View(
        route="/calendar",
        controls=[content],
        bgcolor="#0A1B57",
        padding=20,
        scroll=ft.ScrollMode.AUTO
    )
import flet as ft

def match_view(page: ft.Page):
    page.title = "Matching Quiz"
    page.bgcolor = "#06113C"
    page.padding = 20
    page.scroll = "auto"
    page.window.width = 375
    page.window.height = 700
    page.window.resizable=False
    page.update()
    correct_pairs = {
        "Dog": "Animal",
        "Rose": "Flower",
        "Car": "Vehicle",
        "Apple": "Fruit"
    }

    left_items = list(correct_pairs.keys())
    right_items = list(correct_pairs.values())

    selected_left = None
    selected_right = None

    matched_correct = []
    matched_wrong = []

    left_buttons = {}
    right_buttons = {}

    def style_button(text, color="#1A1A40"):
        return ft.Container(
            content=ft.Text(text, color="white", weight="bold"),
            bgcolor=color,
            padding=15,
            width=120,
            border_radius=25,
            alignment=ft.alignment.center,
            on_click=lambda e: handle_click(e, text)
        )

    def update_ui():
        left_column.controls.clear()
        right_column.controls.clear()

        for item in left_items:
            if item in left_buttons:
                btn = left_buttons[item]
            else:
                btn = style_button(item)
                left_buttons[item] = btn
            left_column.controls.append(btn)

        for item in right_items:
            if item in right_buttons:
                btn = right_buttons[item]
            else:
                btn = style_button(item)
                right_buttons[item] = btn
            right_column.controls.append(btn)

        page.update()

    def handle_click(e, text):
        nonlocal selected_left, selected_right

        # Check if frozen (already correctly matched)
        if text in [p[0] for p in matched_correct] or text in [p[1] for p in matched_correct]:
            return

        # Undo logic if wrong match was selected and clicked again
        for pair in matched_wrong:
            if text in pair:
                matched_wrong.remove(pair)
                reset_button_color(pair[0])
                reset_button_color(pair[1])
                page.update()
                return

        # Selection logic
        if text in left_items:
            selected_left = text
            highlight_button(text, "#3F51B5")
        elif text in right_items:
            selected_right = text
            highlight_button(text, "#3F51B5")

        # Check for complete selection
        if selected_left and selected_right:
            if correct_pairs.get(selected_left) == selected_right:
                # Correct Match
                matched_correct.append((selected_left, selected_right))
                highlight_button(selected_left, "#00C853")  # Green
                highlight_button(selected_right, "#00C853")  # Green
            else:
                # Wrong Match
                matched_wrong.append((selected_left, selected_right))
                highlight_button(selected_left, "#D32F2F")  # Red
                highlight_button(selected_right, "#D32F2F")  # Red

            selected_left = None
            selected_right = None
            page.update()

    def reset_button_color(text):
        if text in left_buttons:
            left_buttons[text].bgcolor = "#1A1A40"
        elif text in right_buttons:
            right_buttons[text].bgcolor = "#1A1A40"

    def highlight_button(text, color):
        if text in left_buttons:
            left_buttons[text].bgcolor = color
        elif text in right_buttons:
            right_buttons[text].bgcolor = color

    def undo_last_match(e):
        if matched_wrong:
            pair = matched_wrong.pop()
            reset_button_color(pair[0])
            reset_button_color(pair[1])
            page.update()

    def submit_quiz(e):
        if len(matched_correct) == len(correct_pairs):
            page.dialog = ft.AlertDialog(
                title=ft.Text("Great job!", color="white"),
                content=ft.Text("You've matched all pairs correctly!", color="white"),
                bgcolor="#1A1A40"
            )
            page.dialog.open = True
        else:
            page.snack_bar = ft.SnackBar(
                content=ft.Text("You have unmatched or incorrect pairs!", color="white"),
                bgcolor="#FF3D00"
            )
            page.snack_bar.open = True
        page.update()

    # Layout
    left_column = ft.Column(spacing=10)
    right_column = ft.Column(spacing=10)

    top_bar = ft.Stack(
        controls=[
            ft.Row(
                controls=[
                    ft.IconButton(
                        icon=ft.icons.ARROW_BACK,
                        icon_color="white",
                        on_click=lambda e: page.go('/lessons')
                    )
                ],
                alignment="start",
                expand=True
            ),
            ft.Row(
                controls=[
                    ft.Text("Lesson 1 - Match the Following", size=20, color="white", weight="bold")
                ],
                alignment="center",
                expand=True
            ),
            ft.Row(
                controls=[
                    ft.Icon(ft.icons.NOTIFICATIONS, color="white")
                ],
                alignment="end",
                expand=True
            )
        ],
        width=page.width
    )
    update_ui()

    return ft.View(
        controls=[
            top_bar,
            ft.Text("Match the following", size=24, color="white", weight="bold"),
            ft.Divider(height=20, color="transparent"),
            ft.Row(
                alignment="center",
                vertical_alignment="start",
                spacing=40,
                wrap=True,
                controls=[
                    left_column,
                    right_column
                ]
            ),
            ft.Divider(height=30, color="transparent"),
            ft.Row(
                alignment="center",
                spacing=20,
                controls=[
                    ft.ElevatedButton(
                        "Undo",
                        on_click=undo_last_match,
                        bgcolor="#FFAA33",
                        color="black",
                        width=120,
                        height=40,
                        style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=20))
                    ),
                    ft.ElevatedButton(
                        "Submit",
                        on_click=submit_quiz,
                        bgcolor="#A259FF",
                        color="white",
                        width=200,
                        height=40,
                        style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=20))
                    )
                ]
            )
        ]
    )


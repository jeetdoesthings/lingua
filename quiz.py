import flet as ft

def quiz_view(page: ft.Page):
    page.title = "Lesson 1 - Quiz"
    page.bgcolor = "#06113C"
    page.window_width = 375
    page.window_height = 700
    page.window_resizable = False

    questions = [
        {"question": "What is '1' called?", "options": ["One", "Oen", "Neo"], "answer": "One"},
        {"question": "Which planet is known as the Red Planet?", "options": ["Earth", "Mars", "Jupiter"], "answer": "Mars"},
    ]

    current_index = 0
    selected_value = ft.RadioGroup(content=ft.Column([]))
    question_text = ft.Text("", size=18, color="white")
    question_number = ft.Text("", size=16, color="white", weight="bold")

    def update_question():
        q = questions[current_index]
        question_text.value = q["question"]
        question_number.value = f"Question {current_index + 1}"
        selected_value.value = None
        selected_value.content.controls = [
            ft.Radio(
                value=opt,
                label=opt,
                label_style=ft.TextStyle(color="white"),
                fill_color="#A259FF",
                active_color="#A259FF"
            )
            for opt in q["options"]
        ]
        page.update()

    def submit_answer(e):
        selected = selected_value.value
        if selected is None:
            snack = ft.SnackBar(
                content=ft.Text("Please select an option!", color="white"),
                bgcolor="#FFA500"
            )
        else:
            correct = questions[current_index]["answer"]
            is_correct = selected == correct
            snack = ft.SnackBar(
                content=ft.Text("Correct!" if is_correct else f"Wrong! Correct: {correct}", color="white"),
                bgcolor="#4BB543" if is_correct else "#FF0033"
            )
        page.snack_bar = snack
        page.open(snack)

    def next_question(e):
        nonlocal current_index
        if current_index < len(questions) - 1:
            current_index += 1
            update_question()

    # Header Top Bar
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
                    ft.Text("Lesson 1 - Quiz", size=20, color="white", weight="bold")
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

    # Question Card
    question_card = ft.Container(
        bgcolor="#0C1F63",
        border_radius=10,
        padding=20,
        width=300,
        content=ft.Column(
            horizontal_alignment="center",
            controls=[
                ft.Row(
                    alignment="spaceBetween",
                    controls=[
                        ft.IconButton(icon=ft.icons.ARROW_BACK, icon_color="#A259FF", on_click=lambda e: None),
                        question_number,
                        ft.IconButton(icon=ft.icons.ARROW_FORWARD, icon_color="#A259FF", on_click=next_question),
                    ]
                ),
                ft.Divider(height=10, color="transparent"),
                question_text,
                ft.Divider(height=10, color="transparent"),
                selected_value,
                ft.Divider(height=20, color="transparent"),
                ft.ElevatedButton(
                    "Submit",
                    on_click=submit_answer,
                    bgcolor="#A259FF",
                    color="white",
                    width=150,
                    height=40,
                    style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=20))
                )
            ]
        )
    )

    view = ft.View(
        route="/quiz",
        controls=[
            top_bar,
            ft.Divider(height=20, color="transparent"),
            ft.Text("Lesson 1", size=24, color="white", weight="bold"),
            ft.Divider(height=20, color="transparent"),
            ft.Row(alignment="center", controls=[question_card])
        ],
        bgcolor="#06113C"
    )

    update_question()
    return view

import flet as ft

from .landing import landing_view
from .signup import signup_page
from .login import login_view
from .start import start_view
from .lessons import lessons_view
from .lesson_1 import lesson_1_view
from .flashcard import flashcards_view
from .quiz import quiz_view
from .match import match_view
from .leaderboard import leader_view
from .friends import friends_view
from .progress_stat_bar import progress_stat_bar_view
from .progress_stat_pie import progress_stat_pie_view
from .calender import calender_view
from .conversation import conversation_view

def main(page: ft.Page):
    page.title = "English Learning App"
    page.theme = ft.Theme(font_family="Poppins")
    page.fonts = {"Poppins": "https://fonts.googleapis.com/css2?family=Poppins:wght@400;600&display=swap"}
    page.window.width = 375
    page.window.height = 700
    page.window.resizable=False
    page.update()
    def route_change(e: ft.RouteChangeEvent):
        print(f"Navigating to route: {page.route}")
        page.views.clear()

        if page.route == "/":
            page.views.append(
                ft.View("/", controls=[
                    ft.Text("Home (always here)", size=14)
                ])
            )
        elif page.route == "/start":
            print("Loading start_view")
            page.views.append(start_view(page))
        elif page.route == "/signup":
            print("Loading signup_page")
            page.views.append(signup_page(page))
        elif page.route == "/login":
            print("Loading login_view")
            page.views.append(login_view(page))
        elif page.route == "/landing":
            print("Loading landing_view")
            page.views.append(landing_view(page))
        elif page.route == "/lessons":
            print("Loading lessons_view")
            page.views.append(lessons_view(page))
        elif page.route == "/lesson_1":
            page.views.append(lesson_1_view(page))
        elif page.route == "/flashcards":
            print("Loading flashcards_view")
            page.views.append(flashcards_view(page))
        elif page.route == "/quiz":
            print("Loading quiz_view")
            page.views.append(quiz_view(page))
        elif page.route == "/match":
            print("Loading match_view")
            page.views.append(match_view(page))
        elif page.route == '/leaderboard':
            print("Loading leaderboard_view")
            page.views.append(leader_view(page))
        elif page.route == '/friends':
            print("Loading friends_view")
            page.views.append(friends_view(page))
        elif page.route == '/progress_stat_bar':
            print("Loading progress_stat_bar_view")
            page.views.append(progress_stat_bar_view(page))
        elif page.route == '/progress_stat_pie':
            print("Loading progress_stat_pie_view")
            page.views.append(progress_stat_pie_view(page))
        elif page.route == '/calender':
            page.views.append(calender_view(page))
        elif page.route == '/conversation':
            page.views.append(conversation_view(page))
        else:
            print(f"Main: Unknown route: {page.route}")
            page.views.append(
                ft.View("/", controls=[
                    ft.Text("404 - Page Not Found", size=24, color="red")
                ])
            )
        page.update()
        print("Main: page.update() called")
    def view_pop(e: ft.ViewPopEvent):
        if len(page.views) > 1:
            page.views.pop()
            top_view = page.views[-1]
            page.go(top_view.route)
        else:
            print("No more views to pop")

    page.on_route_change = route_change
    page.on_view_pop = view_pop

    page.go("/signup")  # Change to "/landing" to test the landing page directly

ft.app(target=main)
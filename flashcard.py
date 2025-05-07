import flet as ft
import base64
from gtts import gTTS
from io import BytesIO

def flashcards_view(page: ft.Page) -> ft.View:
    page.title = "Flashcards"
    page.bgcolor = "#0A1B57"
    page.window.width = 375
    page.window.height = 700
    page.window.resizable = False

    # Back button
    back_button = ft.Row(
        controls=[
            ft.IconButton(
                icon=ft.icons.ARROW_BACK,
                icon_color="white",
                on_click=lambda e: page.go("/lessons")
            ),
            ft.Text("Back", color="white", size=16)
        ],
        alignment=ft.MainAxisAlignment.START
    )

    # Flashcards data
    flashcards = [
        {"word": "Home", "meaning": "तुम्ही घरी गेले याचा तिब्रिते अर्थ तुम्ही आता घरी परत आला आहात.", "sentence": "What time did you get home?"},
        {"word": "Baseball", "meaning": "एक मार्किंग खेळ जो मुख्यत: अमेरिकेत खेळला जातो...", "sentence": "Baseball is a national game of America."},
        {"word": "Stumps", "meaning": "(क्रिकेटमध्ये) तीन लाकूड उभ्या काठ्या...", "sentence": "Stumps are part of the cricket game."}
    ]

    index = 0
    word_ref = ft.Ref[ft.Text]()
    meaning_ref = ft.Ref[ft.Text]()
    sentence_ref = ft.Ref[ft.Text]()
    audio_ref = ft.Ref[ft.Audio]()

    def tts_to_bytes(text: str, lang: str = "en") -> bytes:
        buf = BytesIO()
        gTTS(text, lang=lang).write_to_fp(buf)
        buf.seek(0)
        return buf.read()

    def play_audio(mp3_bytes: bytes):
        b64 = base64.b64encode(mp3_bytes).decode()
        audio_ref.current.src_base64 = b64
        audio_ref.current.autoplay = True
        page.update()


    def on_pronounce(e):
        word = flashcards[index]["word"]
        mp3 = tts_to_bytes(word)
        play_audio(mp3)

    def update_flashcard():
        word_ref.current.value = flashcards[index]["word"]
        meaning_ref.current.value = f"Meaning: {flashcards[index]['meaning']}"
        sentence_ref.current.value = f"Use: {flashcards[index]['sentence']}"
        page.update()

    def prev_word(e):
        nonlocal index
        if index > 0:
            index -= 1
            update_flashcard()

    def next_word(e):
        nonlocal index
        if index < len(flashcards) - 1:
            index += 1
            update_flashcard()

    pronunciation_row = ft.Container(
        content=ft.Row([
            ft.ElevatedButton("Pronunciation", bgcolor="#0A1B57", on_click=on_pronounce),
            ft.Icon(ft.icons.CHEVRON_RIGHT, color="white")
        ], alignment=ft.MainAxisAlignment.SPACE_BETWEEN),
        padding=ft.padding.symmetric(horizontal=16, vertical=12),
        bgcolor="#3949AB",
        border_radius=10,
    )

    view = ft.View(
        route="/flashcards",
        bgcolor="#0A1B57",
        padding=20,
        controls=[
            ft.Column(
                spacing=20,
                scroll=ft.ScrollMode.AUTO,
                controls=[
                    back_button,
                    ft.Row(
                        controls=[
                            ft.IconButton(icon=ft.icons.ARROW_BACK_IOS, icon_color="white", on_click=prev_word),
                            ft.Text("Flashcard", size=16, weight=ft.FontWeight.BOLD, color="white"),
                            ft.IconButton(icon=ft.icons.ARROW_FORWARD_IOS, icon_color="white", on_click=next_word),
                        ],
                        alignment=ft.MainAxisAlignment.SPACE_BETWEEN
                    ),
                    ft.Container(
                        content=ft.Text("", ref=word_ref, size=30, weight=ft.FontWeight.BOLD, color="white"),
                        padding=16, bgcolor="#3949AB", border_radius=10, alignment=ft.alignment.center
                    ),
                    ft.Container(
                        content=ft.Text("", ref=meaning_ref, size=14, color="white"),
                        padding=16, bgcolor="#1F2D5A", border_radius=10
                    ),
                    ft.Container(
                        content=ft.Text("", ref=sentence_ref, size=14, color="white"),
                        padding=16, bgcolor="#1F2D5A", border_radius=10
                    ),
                    pronunciation_row,
                    ft.Audio(ref=audio_ref),  # Only one Audio instance
                ]
            )
        ]
    )

    update_flashcard()
    return view

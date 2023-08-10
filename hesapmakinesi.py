import flet as ft







global_data = ''

def maim(page:ft.Page):
    global global_data
    page.title = "Hesap Makinesi"
    page.vertical_alignment = ft.MainAxisAlignment.END
    page.horizontal_alignment = ft.MainAxisAlignment.CENTER
    page.window_width = 340
    page.window_height = 700
    page.window_resizable = False
    result = ft.Text(value="", color=ft.colors.INDIGO_400, size=40)
    global_data = result.value

    def olay(e):
        global global_data
        data = e.control.data
        if data in "1":
            if len(global_data) < 12:
                global_data += "1"
                result.value += "1"
            else:
                pass

        if data in "2":
            if len(global_data) < 12:
                global_data += "2"
                result.value += "2"
            else:
                pass
        page.update()


        if data in "3":
            if len(global_data) < 12:
                global_data += "3"
                result.value += "3"
            else:
                pass
        page.update()


        if data in "4":
            if len(global_data) < 12:
                global_data += "4"
                result.value += "4"
            else:
                pass
        page.update()


        if data in "5":
            if len(global_data) < 12:
                global_data += "5"
                result.value += "5"
            else:
                pass
        page.update()


        if data in "6":
            if len(global_data) < 12:
                global_data += "6"
                result.value += "6"
            else:
                pass
        page.update()


        if data in "7":
            if len(global_data) < 12:
                global_data += "7"
                result.value += "7"
            else:
                pass
        page.update()


        if data in "8":
            if len(global_data) < 12:
                global_data += "8"
                result.value += "8"
            else:
                pass
        page.update()


        if data in "9":
            if len(global_data) < 12:
                global_data += "9"
                result.value += "9"
            else:
                pass
        page.update()


        if data in "0":
            if len(global_data) < 12:
                global_data += "0"
                result.value += "0"
            else:
                pass
        page.update()


        if data in "00":
            if len(global_data) < 12:
                global_data += "00"
                result.value += "00"
            else:
                pass
        page.update()

    def nokta(e):
        data = e.control.data
        if data in ".":
            pass
        else:
            if len(data) < 12:
                result.value += "."
                page.update()


    def olayC(e):
        global data
        global global_data
        data = e.control.data
        result.value = ""
        global_data = ""
        page.update()

    def d(e):
        result.value = str(result.value[:-1])
        page.update()

    def calc(e):
        global global_data
        data = e.control.data
        result.value = global_data + data
        if data == '=':
            if global_data == "":
                result.value = "Değer Giriniz"
            else:
                try:
                    if global_data.startswith("+") and global_data.startswith("-") and global_data.startswith("*") and global_data.startswith("/") and global_data.startswith("."):
                        global_data = "Düzgün şeçim gir"
                        result.value = eval(global_data)
                    else:
                        result.value = eval(global_data)
                except SyntaxError:
                    result.value = "Error"
            global_data = ''
        else:
            global_data += data
        page.update()

    def theme_changed(e):
        page.theme_mode = (
            ft.ThemeMode.DARK
            if page.theme_mode == ft.ThemeMode.LIGHT
            else ft.ThemeMode.LIGHT
        )
        ft.label = (
            "Light theme" if page.theme_mode == ft.ThemeMode.LIGHT else "Dark theme"
        )
        page.update()

    page.theme_mode = ft.ThemeMode.LIGHT

    page.appbar = ft.AppBar(
        leading_width=40,
        title=ft.Text("Calc"),
        center_title=False,
        bgcolor=ft.colors.SURFACE_VARIANT,
        actions=[
            ft.PopupMenuButton(
                ft.Switch(on_change=theme_changed)
            ),
        ],
    )
    page.update()
    page.add(
        ft.Row(controls=[result], alignment=ft.MainAxisAlignment.END),
        ft.Row(
            spacing=10,
            controls=[
                ft.ElevatedButton("C", data="C",on_click=olayC, style=ft.ButtonStyle(shape=ft.CircleBorder(), padding=30)),
                ft.ElevatedButton("%", data="%",on_click=calc,style=ft.ButtonStyle(shape=ft.CircleBorder(), padding=30)),
                ft.ElevatedButton("d", data="d",on_click=d, style=ft.ButtonStyle(shape=ft.CircleBorder(), padding=30)),
                ft.ElevatedButton("/", data="/",on_click=calc,style=ft.ButtonStyle(shape=ft.CircleBorder(), padding=30))
            ]
        ),
        ft.Row(
            controls=[
                ft.ElevatedButton("7", data="7", on_click=olay,style=ft.ButtonStyle(shape=ft.CircleBorder(), padding=30)),
                ft.ElevatedButton("8", data="8", on_click=olay,style=ft.ButtonStyle(shape=ft.CircleBorder(), padding=30)),
                ft.ElevatedButton("9", data="9",on_click=olay, style=ft.ButtonStyle(shape=ft.CircleBorder(), padding=30)),
                ft.ElevatedButton("x", data="*",on_click=calc,style=ft.ButtonStyle(shape=ft.CircleBorder(), padding=30)),
            ],
        ),
        ft.Row(
            controls=[
                ft.ElevatedButton("4", data="4", on_click=olay,style=ft.ButtonStyle(shape=ft.CircleBorder(), padding=30)),
                ft.ElevatedButton("5", data="5", on_click=olay,style=ft.ButtonStyle(shape=ft.CircleBorder(), padding=30)),
                ft.ElevatedButton("6", data="6",on_click=olay, style=ft.ButtonStyle(shape=ft.CircleBorder(), padding=30)),
                ft.ElevatedButton("-", data="-",on_click=calc, style=ft.ButtonStyle(shape=ft.CircleBorder(), padding=30)),
            ]
        ),
        ft.Row(
            controls=[
                ft.ElevatedButton("1", data="1",on_click=olay, style=ft.ButtonStyle(shape=ft.CircleBorder(), padding=30)),
                ft.ElevatedButton("2", data="2",on_click=olay, style=ft.ButtonStyle(shape=ft.CircleBorder(), padding=30)),
                ft.ElevatedButton("3", data="3",on_click=olay, style=ft.ButtonStyle(shape=ft.CircleBorder(), padding=30)),
                ft.ElevatedButton("+", data="+",on_click=calc, style=ft.ButtonStyle(shape=ft.CircleBorder(), padding=30)),
            ]
        ),
        ft.Row(
            controls=[
                ft.ElevatedButton("00", data="00",on_click=olay, style=ft.ButtonStyle(shape=ft.CircleBorder(), padding=28)),
                ft.ElevatedButton("0", data="0",on_click=olay, style=ft.ButtonStyle(shape=ft.CircleBorder(), padding=30)),
                ft.ElevatedButton(".", data=".", on_click=nokta,style=ft.ButtonStyle(shape=ft.CircleBorder(), padding=30)),
                ft.ElevatedButton("=", data="=",on_click=calc, style=ft.ButtonStyle(shape=ft.CircleBorder(), padding=30)),
            ]
        )
    )

    page.update()

ft.app(target=maim)
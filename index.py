from nicegui import ui
dark=ui.dark_mode()
dark.enable()

def do(arg):
    ans=0
    try:
        ans=eval(arg)
    except:
        ans='String Is Not Calculable'
    Label.set_text(ans)

with ui.tabs().classes('w-full center'):
    with ui.column():
        ui.label('Simplest Calculator')
        answer=""
        string=ui.input(placeholder='Type Here').bind_value(globals(),answer)
        ui.button("Click me", on_click=lambda: do(string.value)).props('flat')
        global Label
        Label=ui.label('Answer Appears Here')
            
ui.run()

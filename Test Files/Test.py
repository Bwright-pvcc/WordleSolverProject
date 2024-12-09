from nicegui import ui

buttontxt = ui.input(label='Text', placeholder='start typing', 
            on_change=lambda b: result.set_text(b.value),
            validation={'Input Must be 5 Characters': lambda value: len(value) == 5})

ui.button(buttontxt.value) 
result = ui.button() 

list = ["hello", "goodbye"]


ui.run()
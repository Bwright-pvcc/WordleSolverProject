from nicegui import ui

class ToggleButton(ui.button):

    def __init__(self, *args, **kwargs,) -> None:
        super().__init__(*args, **kwargs)
        self._state = 1
        self.on('click', self.toggle)

    def toggle(self) -> None:
        """Toggle the button state."""
        
        self._state = self._state + 1
        if (self._state == 4):
            self._state = 1
        self.update()

    def update(self) -> None:
        self.props(f'color={"grey" if self._state == 1 else ""}')
        self.props(f'color={"yellow" if self._state == 2 else ""}')
        self.props(f'color={"green" if self._state == 3 else ""}')
        super().update()

@ui.refreshable


B1 =ui.input(label='Text', placeholder='start typing',
    on_change=lambda e: result1.set_text(e.value),
    validation={'Input One Letter': lambda value: len(value) == 1})
B2 =ui.input(label='Text', placeholder='start typing',
    on_change=lambda e: result2.set_text(e.value),
    validation={'Input One Letter': lambda value: len(value) == 1})
B3 =ui.input(label='Text', placeholder='start typing',
    on_change=lambda e: result3.set_text(e.value),
    validation={'Input One Letter': lambda value: len(value) == 1})
B4 =ui.input(label='Text', placeholder='start typing',
    on_change=lambda e: result4.set_text(e.value),
    validation={'Input One Letter': lambda value: len(value) == 1})
B5 =ui.input(label='Text', placeholder='start typing',
    on_change=lambda e: result5.set_text(e.value),
    validation={'Input One Letter': lambda value: len(value) == 1})


with ui.button_group():
    result1 = ToggleButton()
    result2 = ToggleButton()
    result3 = ToggleButton()
    result4 = ToggleButton()
    result5 = ToggleButton()
        
ui.run()

@ui.refreshable
def inputMake() -> None:
        B1 = ui.input(label='Text', placeholder='start typing',
        validation={'Input One Letter': lambda value: len(value) == 5})
        ToggleButton(B1.value)
@ui.refreshable
def buttonMake() -> None: 
    ToggleButton()

ui.button('Click me!', on_click=lambda: inputMake.refresh())


inputMake()
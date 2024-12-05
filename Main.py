from nicegui import ui

my_list = ["apple", "banana", "cherry"]
texting = "eh"

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


UserInput = ui.input(label='Text', placeholder='start typing',
            on_change=lambda e: result.set_text(e.value),
            validation={'Input Must be Five Letters': lambda value: len(value) == 5})

UserList = list(UserInput.value)

with ui.button_group():
    ToggleButton(my_list[0])
    ToggleButton(my_list[1])
    result = ToggleButton(my_list[1])
    
    
    
   
ui.run()






from nicegui import ui

def create_buttons():
    user_input = input("Enter a string: ")  # Ask the user for a string
    for letter in user_input:
        ui.button(letter).on_click(lambda x, letter=letter: print(f"Button for '{letter}' clicked"))

ui.label("Enter a string to generate buttons for each letter:")
ui.textbox().on_change(lambda text: create_buttons())  # When the user types, buttons will be created

ui.run()

from nicegui import ui # type: ignore

# This is the user input 
class TheInput(ui.input): 
    # Not fully sure what this does but it works 
     def __init__(self, *args, **kwargs,) -> None:
        super().__init__(*args, **kwargs)
        # When the enter key is pressed it runs the change function
        self.on('change', self.change)
    
     def change(self, selflist) -> None: 
        # Sets the value to the current value 
        # Not sure if this is fully nessisary but I'm not changing it 
        self.value = self.value
        # Checking the correct Input Length 
        if len(self.value) == 5:
            selflist = list(self.value)
            # Makes a Group of 5 Buttons out of the list of the user's input 
            with ui.button_group():
                ToggleButton(selflist[0])
                ToggleButton(selflist[1])
                ToggleButton(selflist[2])
                ToggleButton(selflist[3])
                ToggleButton(selflist[4])
        # Updates the UI to reflect the changes 
        # This is what allows the input to update after the code has run 
        self.update()

# This is the Specific Button that can change it's color 
class ToggleButton(ui.button):

    def __init__(self, *args, **kwargs,) -> None:
        super().__init__(*args, **kwargs)
        #Default State is 1
        self._state = 1
        #When the button is clicked run the Toggle Function
        self.on('click', self.toggle)

    def toggle(self) -> None:
        """Toggle the button state."""
        # Increment the state
        self._state = self._state + 1
        # If the state is 4 loop back to 1 
        if (self._state == 4):
            self._state = 1
        # Run the update function 
        self.update()

    def update(self) -> None:
        #Changes the color depending on the state
        self.props(f'color={"grey" if self._state == 1 else ""}')
        self.props(f'color={"yellow" if self._state == 2 else ""}')
        self.props(f'color={"green" if self._state == 3 else ""}')
        #This is what allows the button to update after the code has run 
        super().update()
# Label is the smaller top text. 
# Placeholder only exists before the user starts typing 
# Validation plays an error message if the length isn't correct

TheInput(label='Input', placeholder='start typing',
        validation={'Input a Five Letter Word': lambda value: len(value) == 5})

# Do the UI
ui.run()
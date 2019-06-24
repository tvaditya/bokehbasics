#from bokeh.io import output_file, show
from bokeh.io import curdoc
from bokeh.models.widgets import TextInput, Button, Paragraph
from bokeh.layouts import layout

# The html outpu file
# output_file("wdigettest.html")

# widgets
text_input = TextInput(value="Aditya")
button = Button(label="Type anything")
output = Paragraph()

def update():
    output.text="Hello, " + text_input.value

button.on_click(update)

lay_out=layout([[button, text_input],[output]])

#show(lay_out)
curdoc().add_root(lay_out)
import PySimpleGUI as abreviadojeje

layout = [[abreviadojeje.Text('Enter a Numbe')], [abreviadojeje.Input()], [abreviadojeje.OK()]]

event, values = abreviadojeje.Window('Enter a number example', layout).Read()
abreviadojeje.Popup(event, values[0])

print(event)
print(values[0])

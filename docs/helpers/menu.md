# Menu Helper

## Menu Class
### Initialising
```python
menu = jw_utils.helpers.menu.Menu("My Menu Name")
```
### Adding options

1) Define a callback
```python
def myCallback(): # Must take no arguments
  print("The callback has been triggered")
```
2) Add the option to the menu
```python
menu.addOption("Option Name", myCallback) 
# Note no brackets on myCallback(). We're doing this javascript style, bby
```
### Running the menu
```python
menu.doMenu()
```
##### Outputs
```
=== ===========
Key Action
=== ===========
1   My Option 1
=== ===========
>
```
Then when the user presses 1 the callback is triggered.
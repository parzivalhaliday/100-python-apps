# File Creator
This is a Python script that allows the user to create files with different extensions and add content to them.

## How to Use
Run the `file_creator.py` script.

Enter the name of the file you want to create, including the file extension.

If you want to add content to the file, enter "yes" when prompted. Otherwise, enter "no".

If you chose to add content, enter the content for the file when prompted.

The file will be created with the specified name and content.

If you want to save the file, enter "yes" when prompted. Otherwise, enter "no".

If you chose not to save the file, it will be deleted.

## Supported File Types and Default Content
The script supports the following file extensions:

- `.txt`: Plain text file. Default content: 

```
"This is a test file."
```


- `.py`: Python script. Default content:

```python
 print('This file was automatically generated.')
 ```

- `.js`: JavaScript file. Default content: console.log('This file was automatically generated.');

```javascript
console.log('This file was automatically generated.'))
 ```

- `.html`: HTML file. Default content:

```html
 <html><body><h1>This file was automatically generated.</h1></body></html>
 ```

- `.css`:  CSS file. Default content:

```css
body { background-color: lightblue; }
 ```

If a file with a different extension is created, the default content will be "This is a test file."

## Requirements
`Python 3.x`

## License

This code is licensed under the MIT License. Feel free to use and modify it for your own purposes.




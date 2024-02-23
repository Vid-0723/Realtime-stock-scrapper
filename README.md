# StockProject


## Prerequisites

Please make sure you have `poetry` installed. You can find the installation guide [here](https://python-poetry.org/docs/).

Once installed add it to your **PATH**.

If you followed the instructions from above, poetry should be installed in a platform-specific directory:
- **$HOME/.local/bin** on Unix
- **%APPDATA%\Python\Scripts** on Windows
- **~/Library/Application Support/pypoetry** on MacOS

This is the directory you should add to your **PATH**.
Check by running:
```console
poetry --version
``` 
To have the latest version:
```console
poetry self update
``` 


## Setup for VSCode

Open project in VSCode.

Install dependencies:
```console
poetry install
```

On the bottom right of your VSCode editor select the yellow button saying **Select Interpreter**.

Choose **Select Python Interpreter** and then select option with **Poetry** on the right side. 

This will activate your virtual environment.

Alternatively press `CTRL+Shift+P` and search for `Python: Select Interpreter`. 
Select it and then choose option with **Poetry** on the right side.


## Running the application in VSCode

Navigate to the **Run and Debug** icon in your **Activity bar** on the left of your editor.

Select the green **Start debugging** button with option **Python: Django**.

Alternatively press `F5` to run your application in Debug mode.

Navigate to the development server in your Terminal.

## Running the tests in VSCode

Navigate to the **Testing** icon in you **Activity bar** on the left of your editor.

Expand the `stockscrapper` tab to see the tests available.

Alternatively run all tests in your terminal with the command
```console
poetry run pytest
```

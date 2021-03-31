# AWS Lambda Cookie Cutters #

## Prerequisites ##

Be sure you have Python installed before doing anything else.

Once you have installed Python, install Cookiecutter (a file and project generation tool):

`> pip install cookiecutter`

Copy this repo to your computer.

### With Git ###

Clone this repo:

`> git clone https://github.com/cmstead/lambda_cookiecutters.git`

### Without Git ###

Dowload the zip file:

`https://github.com/cmstead/lambda_cookiecutters/archive/refs/heads/master.zip`

## Install the Cookiecutter Templates ##

To install the templates in this repo, run the following command:

`> python ./install_templates.py`

This will copy all of the templates to a folder called .cookiecutters in your user directory.

## Install VS Code Snippets ##

1. Press F1 to open the command pallette
2. Type "snip" to filter the list, and select "Preferences: Configure User Snippets"
3. Type "yaml" to filter the list, and select "yaml" or "yaml.json". You will have one or the other, but not both.
4. Open `yaml.json` in the `snippets` folder. Copy the contents, and paste them into the `python.json` VS Code snippets file.
5. Save.
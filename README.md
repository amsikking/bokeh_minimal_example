# bokeh_minimal_example
Basic code and structure for a simple bokeh server.

## Quick start:
Download the repository and either:
1) Run 'bokeh_minimal_example.py' directly from Python.
2) Run from the command line with: "bokeh serve --show bokeh_minimal_example.py".

![social_preview](/social_preview.png?raw=true)

## Details:
This example shows:
- How to launch Bokeh directly from a Python script AND from the command line.
- A minimal Bokeh visualization with an updating plot (via periodic callback) and a button.
- A way of stopping the Bokeh server with a button.
- A way of stopping the Bokeh server when the user exits the web browser.

**Note:** supporting both script and command line launch is tricky so it may be best to pick one way for a given application and go with that.

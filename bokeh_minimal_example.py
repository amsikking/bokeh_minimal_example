# Imports from the python standard library:
import numpy as np

# Third party imports, installable via pip:
# -> bokeh graphics and features etc
from bokeh.layouts import column
from bokeh.models.widgets import Button
from bokeh.plotting import curdoc, figure
# -> bokeh server
from bokeh.application import Application
from bokeh.application.handlers.function import FunctionHandler
from bokeh.server.server import Server

class BokehDoc:
    def __init__(self, doc):
        import sys # import here to keep sys reference on session destroyed
        self.doc = doc
        # Plot:
        def _update_plot():
            print('updating plot')
            self.plot.scatter(x=np.random.randint(1, 10),
                              y=np.random.randint(1, 10),
                              size=10)
            return None
        self.plot = figure(title="Live scatter plot", height=400, width=400)
        _update_plot() # add some points
        # Stop button:
        def _stop():
            print('stopping server')
            sys.exit()
            return None
        self.button = Button(label="Stop", button_type="success")
        self.button.on_click(_stop)
        # Document:
        self.doc.title = "Updating plot with a stop button"
        self.doc.add_root(column([self.plot, self.button]))
        self.doc.add_periodic_callback(_update_plot, 500) # Update every x ms
        # Detect if browser is closed:
        def _session_destroyed(session_context):
            print('session_destroyed:', session_context.destroyed)
            sys.exit()
            return None        
        self.doc.on_session_destroyed(_session_destroyed) # is browser closed?

if __name__ == '__main__':
    # -> Running from script:
    bk_app = {'/': Application(FunctionHandler(BokehDoc))} # doc created here
    server = Server(
        bk_app,
        port=5000, # default 5006
        # check session status sooner (.on_session_destroyed callback)
        check_unused_sessions_milliseconds=500,     # default 17000
        unused_session_lifetime_milliseconds=500)   # default 15000
    server.start()
    server.io_loop.add_callback(server.show, "/")
    server.io_loop.start()
else:
    # -> Running with commmand: "bokeh serve --show bokeh_minimal_example.py"
    doc = curdoc()  # create base bokeh doc (container for bokeh models)
    bokehdoc = BokehDoc(doc) # pass doc into create_doc function
    # Note .on_session_destroyed callback will fire after ~17 seconds...

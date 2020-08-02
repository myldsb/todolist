from functools import wraps

class MyWidget:

    def __init__(self):
        pass

    def cache(self, widget_class):
        # wrap a widget class, when init it, and will add it to self with its class name
        @wraps(widget_class)
        def wrapper(*args, **kwargs):
            widget = widget_class(*args, **kwargs)
            setattr(self, widget_class.__name__, widget)
            return widget
        return wrapper

    def switch(self, close_attr, show_attr):
        # switch central widget of MainWindow. close current and show another.
        if hasattr(self, close_attr):
            close_w = getattr(self, close_attr)
            close_w.close()
            delattr(self, close_attr)
        if not hasattr(self, show_attr):
            module = __import__("interface")
            setattr(self, show_attr, getattr(module, show_attr)())
        else:
            raise RuntimeError("there is not a widget to show!")
        show_w = getattr(self, show_attr)
        my_widget.Window.setCentralWidget(show_w)
        show_w.show()




my_widget = MyWidget()
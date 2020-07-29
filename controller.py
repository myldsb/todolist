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


my_widget = MyWidget()
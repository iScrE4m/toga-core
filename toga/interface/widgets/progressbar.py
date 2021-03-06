from .base import Widget


class ProgressBar(Widget):
    """
    Progressbar widget

    :param id:          Identifier for this widget
    :param style:       Style of the button
    :type style:        colosseum.CSS
    :param max:         Maximum of the progress bar
    :type max:          int
    :param value:       Current progress
    :type value:        int
    """
    def __init__(self, id=None, style=None, max=None, value=None):
        super().__init__(id=id, style=style, max=max, value=value)

    def _configure(self, max, value):
        self.value = value
        self.max = max
        self.running = False
        self.rehint()

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, value):
        self._value = value
        self._running = self._value is not None

    @property
    def max(self):
        return self._max

    @max.setter
    def max(self, max):
        self._max = max
        self._set_max(max)

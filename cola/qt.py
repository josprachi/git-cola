from cola.compat import set
from cola.widgets import defs
    def __init__(self, parent):
        layout.setSpacing(defs.spacing)
        layout.setMargin(defs.margin)
            item.setIcon(qtutils.git_icon())
        git_icon = qtutils.git_icon()
        # used to hide the completion popup after a drag-select
        self._drag = 0
    def is_case_sensitive(self, text):
        return bool([char for char in text if char.isupper()])

        case_sensitive = self.is_case_sensitive(text)
    def update_matches(self):
        text = self.last_word()
        case_sensitive = self.is_case_sensitive(text)
        self._model.update_matches(case_sensitive)

            return unicode(self.text())
    def do_completion(self):
        self._completer.popup().setCurrentIndex(
                self._completer.completionModel().index(0,0))
        self._completer.complete()

                self.do_completion()
        if prefix != unicode(self._completer.completionPrefix()):
    #: _drag: 0 - unclicked, 1 - clicked, 2 - dragged
    def mousePressEvent(self, event):
        self._drag = 1
        return QtGui.QLineEdit.mousePressEvent(self, event)

    def mouseMoveEvent(self, event):
        if self._drag == 1:
            self._drag = 2
        return QtGui.QLineEdit.mouseMoveEvent(self, event)

    def mouseReleaseEvent(self, event):
        if self._drag != 2 and event.buttons() != QtCore.Qt.RightButton:
            self.do_completion()
        self._drag = 0
        return QtGui.QLineEdit.mouseReleaseEvent(self, event)

    def close_popup(self):
        self._completer.popup().close()

def color(c, a=255):
    qc = QColor(c)
    qc.setAlpha(a)
    return qc

default_colors = {
    'color_add':            color(Qt.green, 128),
    'color_remove':         color(Qt.red,   128),
    'color_begin':          color(Qt.darkCyan),
    'color_header':         color(Qt.darkYellow),
    'color_stat_add':       color(QColor(32, 255, 32)),
    'color_stat_info':      color(QColor(32, 32, 255)),
    'color_stat_remove':    color(QColor(255, 32, 32)),
    'color_emphasis':       color(Qt.black),
    'color_info':           color(Qt.blue),
    'color_date':           color(Qt.darkCyan),
}
    dialog = SyntaxTestDialog(qtutils.active_window())
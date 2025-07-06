import traceback
import sys

def capture_exception(exc_type, exc_value, exc_traceback):
    if issubclass(exc_type, KeyboardInterrupt):
        # Let the user interrupt
        sys.__excepthook__(exc_type, exc_value, exc_traceback)
        return

    tb = ''.join(traceback.format_exception(exc_type, exc_value, exc_traceback))
    return {
        "type": exc_type.__name__,
        "message": str(exc_value),
        "traceback": tb
    }

# Attach globally
def install_global_hook(callback):
    def _hook(exc_type, exc_value, exc_traceback):
        error_info = capture_exception(exc_type, exc_value, exc_traceback)
        callback(error_info)

    sys.excepthook = _hook

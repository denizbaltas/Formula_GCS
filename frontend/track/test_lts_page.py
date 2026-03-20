# mainden çalıştırmak yerine lts_page'i test eder

import sys
from PyQt6.QtWidgets import QApplication
from lts_page import LTSPage


if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = LTSPage()
    window.resize(800, 600)
    window.show()

    sys.exit(app.exec())

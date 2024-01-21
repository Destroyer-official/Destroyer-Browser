import sys
import os
from enum import Enum
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import Qt, QUrl,QTimer
from PyQt5 import QtCore, QtWidgets

from PyQt5.QtWidgets import (
    QDesktopWidget, QApplication, QMainWindow, QWidget, QTabBar, QToolBar,
    QAction, QLineEdit, QTabWidget, QPushButton, QVBoxLayout, QToolButton, QHBoxLayout
)
from PyQt5.QtWebEngineWidgets import QWebEngineView, QWebEnginePage, QWebEngineSettings
import qdarkstyle
import atexit


class WebPage(QWebEnginePage):
    def certificateError(self, error):
        return True
def modify_number(input_number):
    if input_number > 1900:
        return input_number / 1.2
    if input_number > 1870:
        return input_number / 1.3
    elif input_number > 1770:
        return input_number / 1.4
    elif input_number > 1670:
        return input_number / 1.5
    elif input_number > 1570:
        return input_number / 1.6
    elif input_number > 1470:
        return input_number / 1.8
    elif input_number > 1370:
        return input_number / 2.2
    elif input_number > 1270:
        return input_number / 2.4
    elif input_number > 1170:
        return input_number / 2.6
    elif input_number > 1070:
        return input_number / 2.8
    elif input_number > 970:
        return input_number / 3.2
    elif input_number > 870:
        return input_number / 3.4
    elif input_number > 770:
        return input_number / 3.6
    else:
        return input_number // 3.8
class Urls(Enum):
    DEFAULT_HOME = "https://duckduckgo.com/"
    SHODAN = 'https://www.shodan.io/'
    DRONEBL = 'https://dronebl.org/lookup?'
    DNSDUMPSTER = 'https://dnsdumpster.com/'
    DEHASHED = 'https://www.dehashed.com/'
    CYBERCRIME = 'https://cybercrime-tracker.net/'
    ONYPHE = 'https://www.onyphe.io/'
    AHMIA = 'https://ahmia.fi/'
    ARCHIVE = 'https://archive.org/search?'
    ARIN = 'https://search.arin.net/arin/'
    BGPVIEW = 'https://bgpview.io/'
    CERTIFICATE = 'https://crt.sh/'
    THREAT_CROWD = "http://ci-www.threatcrowd.org/"
    VIRUS_TOTAL = "https://www.virustotal.com/"
    MIT_OCW = "https://ocw.mit.edu/"
    HACKER_ONE = "https://www.hackerone.com/"
    CYBRARY = "https://www.cybrary.it/"
    OWASP_TOP_10 = "https://owasp.org/Top10/"
    HACKER_NEWS = "https://thehackernews.com/"
    KREBS_ON_SECURITY = "https://krebsonsecurity.com/"
    TECHCRUNCH = "https://techcrunch.com/"
    GITHUB = "https://github.com/"
    STACK_OVERFLOW = "https://stackoverflow.com/"
    REDDIT_INFOSEC = "https://www.reddit.com/r/Infosec/"
    PROJECT_GUTENBERG = "https://dev.gutenberg.org/"
    METAEXPLOIT_RAPID7 = "https://www.rapid7.com/products/metasploit/"
    HACKER_NMAP = "https://hackertarget.com/nmap-online-port-scanner/"
    ZDNET_SECURITY = "https://www.zdnet.com/topic/security/"
    SECURITY_WEEK = "https://www.securityweek.com/"
    HACKER_NEWS_YCOMBINATOR = "https://news.ycombinator.com/"
    DARK_READING = "https://www.darkreading.com/"
    WHOIS_LOOKUP = "https://who.is/"
    URL_VOID = "https://www.urlvoid.com/"
    NIST_NVD = "https://nvd.nist.gov/vuln/search"
    INTERNET_ARCHIVE = "https://archive.org/"
    DNS_DUMPSTER = "https://dnsdumpster.com/"
    EXPLOIT_DB = "https://www.exploit-db.com/"
    MITRE_ATTACK = "https://attack.mitre.org/"
    OSVF = "https://openssf.org/"
    TENABLE = "https://www.tenable.com/plugins"
    SANS_INSTITUTE = "https://www.sans.org/"


class Navigator:
    @staticmethod
    def navigate(web_view, url):
        try:
            web_view.setUrl(QUrl(url))
        except (ValueError, TypeError) as e:
            print(f"Error navigating to {url}: {e}")


class TabWidget(QWidget):
    urlChanged = QtCore.pyqtSignal(QUrl)

    def __init__(self, url=None):
        super().__init__()
        self.webView = QWebEngineView()
        self.webView.setPage(WebPage())
        self.webView.setUrl(QUrl(url)) if url else self.webView.setUrl(
            QUrl(Urls.DEFAULT_HOME.value))
        layout = QVBoxLayout(self)
        layout.addWidget(self.webView)

        self.webView.urlChanged.connect(self.handleUrlChanged)
        self.page = self.webView.page()
        self.page.linkHovered.connect(self.handleLinkHovered)

    def handleUrlChanged(self, url):
        self.urlChanged.emit(url)

    def handleLinkHovered(self, url):
        modifiers = QApplication.keyboardModifiers()
        openInNewTab = modifiers == Qt.ControlModifier or modifiers == Qt.ShiftModifier

        if openInNewTab:
            self.urlChanged.emit(QUrl(url))


class ClosableTabWidget(QTabWidget):
    def __init__(self, parent=None):
        super(ClosableTabWidget, self).__init__(parent)
        self.setTabsClosable(True)
        self.tabCloseRequested.connect(self.closeTab)

    def createTab(self, url=None, tabName=None, tabIndex=None):
        browserTab = TabWidget(url)
        index = self.insertTab(tabIndex if tabIndex is not None else self.count(
        ), browserTab, tabName if tabName else "Destroyer")

        closeButton = QPushButton("❌")
        closeButton.clicked.connect(
            lambda _, index=index: self.closeTab(index))
        self.tabBar().setTabButton(index, QTabBar.RightSide, closeButton)

        browserTab.urlChanged.connect(self.updateUrl)
        browserTab.webView.titleChanged.connect(
            lambda title, index=index: self.setTabText(index, title))

    def closeTab(self, index):
        widget = self.widget(index)
        if widget:
            widget.deleteLater()
            self.removeTab(index)

    def updateUrl(self, url):
        index = self.indexOf(self.sender().parent())
        self.setTabText(index, url.host())


class AppMainWindow(QMainWindow):
    def __init__(self):
        super(AppMainWindow, self).__init__()

        settings = QWebEngineSettings.globalSettings()
        settings.setAttribute(QWebEngineSettings.LocalStorageEnabled, False)
        settings.setAttribute(QWebEngineSettings.PluginsEnabled, False)
        self.statusBar = self.statusBar()
        self.tabs = ClosableTabWidget()
        self.setCentralWidget(self.tabs)

        self.tabBar = QTabBar()
        self.tabBar.setTabsClosable(True)
        self.createTab()

        layout = QHBoxLayout()
        navbar1 = QToolBar()
        self.setupUi(navbar1)
        layout.addWidget(navbar1)

        navbarq = QToolBar()
        self.quit(navbarq)
        layout.addWidget(navbarq)

        navbar2 = QToolBar()
        self.setupBookmarksNavbar(navbar2)
        layout.addWidget(navbar2)

        container = QWidget()
        container.setLayout(layout)
        self.addToolBar(navbar1)
        self.addToolBar(navbarq)
        self.addToolBar(navbar2)
        self.addToolBar(Qt.LeftToolBarArea, navbar2)

        
        self.urlBar = QLineEdit()
        self.urlBar.returnPressed.connect(self.navigateToUrl)
        navbar1.addWidget(self.urlBar)

        self.setWindowTitle("Destroyer Browser")

        self.setStyleSheet(qdarkstyle.load_stylesheet_pyqt5())
        self.show()


        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update_window_size)
        self.timer.start(100)  # Update every 100 milliseconds

    def update_window_size(self):
        window_size = self.size()
        window_width = window_size.width()

        if hasattr(self, 'saved_window_size'):
            saved_width = self.saved_window_size
            if window_width != saved_width :
                self.saved_window_size = (window_width)
                window_width_s=int(modify_number(window_width))
                self.urlBar.setFixedWidth(window_width_s)
        else:
            self.saved_window_size = (window_width)

    def navigateBack(self):
        currentTab = self.tabs.currentWidget()
        if currentTab and hasattr(currentTab, 'webView'):
            currentTab.webView.back()

    def navigateForward(self):
        currentTab = self.tabs.currentWidget()
        if currentTab and hasattr(currentTab, 'webView'):
            currentTab.webView.forward()

    def reloadPage(self):
        currentTab = self.tabs.currentWidget()
        if currentTab and hasattr(currentTab, 'webView'):
            currentTab.webView.reload()

    def createTab(self, url=None, tabName=None, tabIndex=None):
        browserTab = TabWidget(url)
        index = self.tabs.insertTab(tabIndex if tabIndex is not None else self.tabs.count(
        ), browserTab, tabName if tabName else "Destroyer")

        closeButton = QPushButton("❌")
        closeButton.clicked.connect(
            lambda _, index=index: self.closeTab(index))
        self.tabBar.setTabButton(index, QTabBar.RightSide, closeButton)

        browserTab.urlChanged.connect(self.updateUrl)
        browserTab.webView.titleChanged.connect(
            lambda title, index=index: self.tabs.setTabText(index, title))

    def updateUrl(self, url):
        index = self.tabs.currentIndex()
        self.urlBar.setText(url.toString())
        self.tabs.setTabText(index, url.host())
        self.statusBar.showMessage(f'Page loaded: {url.toString()}')

    def navigate(self, url):
        currentWidget = self.tabs.currentWidget()
        if currentWidget and hasattr(currentWidget, 'webView'):
            Navigator.navigate(currentWidget.webView, url)

    def quit(self, navbar):
        quitAction = QAction('Quit', self)
        iconPath = "icons/exit.png"
        icon = QIcon(iconPath)
        quitAction.setIcon(icon)
        quitAction.triggered.connect(self.quitApplication)
        navbar.addActions([quitAction])

    def setupUi(self, navbar):
        backAction = QAction('Back', self)
        iconPath = "icons/Back.svg"
        icon = QIcon(iconPath)
        backAction.setIcon(icon)
        backAction.triggered.connect(self.navigateBack)

        forwardAction = QAction('Forward', self)
        iconPath = "icons/Forward.svg"
        icon = QIcon(iconPath)
        forwardAction.setIcon(icon)
        forwardAction.triggered.connect(self.navigateForward)

        reloadAction = QAction('Reload', self)
        iconPath = "icons/reload.svg"
        icon = QIcon(iconPath)
        reloadAction.setIcon(icon)
        reloadAction.triggered.connect(self.reloadPage)

        homeIconPath = "icons/home.svg"
        homeIcon = QIcon(homeIconPath)
        homeAction = QAction('Home', self)
        homeAction.setIcon(homeIcon)
        homeAction.triggered.connect(self.navigateHome)

        navbar.addActions(
            [backAction, forwardAction, reloadAction, homeAction])

        newTabButton = QToolButton()
        newTabButton.setText(" ➕ ")
        iconPath = "icons/new_tab.svg"
        icon = QIcon(iconPath)
        newTabButton.setIcon(icon)
        newTabButton.clicked.connect(self.createTab)
        navbar.addWidget(newTabButton)

    def navigateHome(self):
        homeUrl = Urls.DEFAULT_HOME.value
        self.navigate(homeUrl)

    def closeTab(self, index):
        self.tabs.closeTab(index)

    def closeCurrentTab(self):
        index = self.tabs.currentIndex()
        self.closeTab(index)

    def quitApplication(self):
        appInstance = QtWidgets.QApplication.instance()
        if appInstance and self.isVisible():
            self.close()
        os.system('cls' if os.name == 'nt' else 'clear')

    def navigateToUrl(self):
        url = self.urlBar.text()
        currentTab = self.tabs.currentWidget()
        if currentTab:
            currentTab.webView.setUrl(QUrl(url))

    def setupBookmarksNavbar(self, navbar):
        bookmarks = [
            ('Shodan', Urls.SHODAN),
            ('DroneBL', Urls.DRONEBL),
            ('Dnsdumpster', Urls.DNSDUMPSTER),
            ('Dehashed', Urls.DEHASHED),
            ('Cybercrime', Urls.CYBERCRIME),
            ('Onyphe', Urls.ONYPHE),
            ('Ahmia', Urls.AHMIA),
            ('Archive', Urls.ARCHIVE),
            ('Arin', Urls.ARIN),
            ('Bgpview', Urls.BGPVIEW),
            ('Certificate', Urls.CERTIFICATE),
            ('Threat Crowd', Urls.THREAT_CROWD),
            ('VirusTotal', Urls.VIRUS_TOTAL),
            ('MIT OCW', Urls.MIT_OCW),
            ('HackerOne', Urls.HACKER_ONE),
            ('Cybrary', Urls.CYBRARY),
            ('OWASP Top 10', Urls.OWASP_TOP_10),
            ('Hacker News', Urls.HACKER_NEWS),
            ('Krebs Sec', Urls.KREBS_ON_SECURITY),
            ('TechCrunch', Urls.TECHCRUNCH),
            ('GitHub', Urls.GITHUB),
            ('Stack Overflow', Urls.STACK_OVERFLOW),
            ('Reddit Infosec', Urls.REDDIT_INFOSEC),
            ('Gutenberg', Urls.PROJECT_GUTENBERG),
            ('MetaX Rapid7', Urls.METAEXPLOIT_RAPID7),
            ('Hackertarget', Urls.HACKER_NMAP),
            ('ZDNet Security', Urls.ZDNET_SECURITY),
            ('SecurityWeek', Urls.SECURITY_WEEK),
            ('YCombinator', Urls.HACKER_NEWS_YCOMBINATOR),
            ('Dark Reading', Urls.DARK_READING),
            ('Whois Lookup', Urls.WHOIS_LOOKUP),
            ('URLVoid', Urls.URL_VOID),
            ('NIST NVD', Urls.NIST_NVD),
            ('Internet Archive', Urls.INTERNET_ARCHIVE),
            ('DNS Dumpster', Urls.DNS_DUMPSTER),
            ('Exploit DB', Urls.EXPLOIT_DB),
            ('Mitre ATT&CK', Urls.MITRE_ATTACK),
            ('OSVF', Urls.OSVF),
            ('Tenable', Urls.TENABLE),
            ('SANS Institute', Urls.SANS_INSTITUTE),
        ]

        for bookmarkText, bookmarkUrl in bookmarks:
            bookmarkAction = QAction(bookmarkText, self)
            bookmarkAction.triggered.connect(
                lambda _, url=bookmarkUrl: self.openBookmarkInNewTab(url.value))
            navbar.addAction(bookmarkAction)
    def openBookmarkInNewTab(self, url):
        currentTab = self.tabs.currentWidget()
        if currentTab:
            self.createTab(url)
            self.urlBar.setText(url)
            self.navigate(url)

def main():
    try:
        app = QApplication(sys.argv + ['--no-sandbox'])
        QApplication.setApplicationName("Destroyer Browser")
        window = AppMainWindow()
        atexit.register(window.quitApplication)
        sys.exit(app.exec_())
    except Exception as e:
        print(e)


if __name__ == "__main__":
    main()

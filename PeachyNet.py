

#cookie holder
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setGeometry(100, 100, 600, 400)
        
        self.cookie_jar = QNetworkCookieJar(self)
        self.network_manager = QNetworkAccessManager(self)
        self.network_manager.setCookieJar(self.cookie_jar)
        
        self.cookie_output = QPlainTextEdit(self)
        self.cookie_output.setGeometry(50, 50, 500, 300)
        self.cookie_output.setReadOnly(True)
        self.cookie_output.setPlainText("")
        
        self.load_cookies()
        
    def load_cookies(self):
        self.cookie_jar.setAllCookies([]) # clear any existing cookies
        
        # Load cookies from file
        with open('cookies.txt', 'r') as f:
            for line in f:
                cookie = QNetworkCookie.parseCookies(line.encode())[0]
                self.cookie_jar.insertCookie(cookie)
                
        self.cookie_output.setPlainText("Cookies loaded:\n" + "\n".join([str(cookie.toRawForm()) for cookie in self.cookie_jar.allCookies()]))
        
    def save_cookies(self):
        with open('cookies.txt', 'w') as f:
            for cookie in self.cookie_jar.allCookies():
                f.write(cookie.toRawForm().data().decode() + "\n")
                
        self.cookie_output.setPlainText("Cookies saved:\n" + "\n".join([str(cookie.toRawForm()) for cookie in self.cookie_jar.allCookies()]))
        
#style sheet
class MyWidget(QWidget):
    def __init__(self):
        super().__init__()
        
        # Set the background color of the widget
        self.window.setStyleSheet("background-color: lightblue;")
        
        # Set the size of the widget
        self.setGeometry(100, 100, 400, 300)
        
        

class MyWebBrowser():
    
    def __init__(self):
        
        self.window = QWidget()
        self.window.setWindowTitle("PeachyNet")
        self.window.setStyleSheet("background-color: #FFFFFFF; color: peach;")
        
        self.layout = QVBoxLayout()
        self.horizontal = QHBoxLayout()
                
        self.url_bar = QTextEdit()
        self.url_bar.setMaximumHeight(30)
        self.url_bar.setStyleSheet("background-color: #FFFFFF; color: white;")
        
        self.go_btn = QPushButton("Go")
        self.go_btn.setMinimumHeight(30)
        self.go_btn.setStyleSheet("background-color: #4CAF50; color: white;")
    
        self.back_btn = QPushButton("<")
        self.back_btn.setMinimumHeight(30)
        self.back_btn.setStyleSheet("background-color: #F98B88; color: peach;")
    
        self.forward_btn = QPushButton(">")
        self.forward_btn.setMinimumHeight(30)
        self.forward_btn.setStyleSheet("background-color: #F98B88; color: peach;")
        
        self.reload_btn = QPushButton("R")
        self.reload_btn.setMinimumHeight(30)
        self.reload_btn.setStyleSheet("background-color: #F98B88; color: peach;")
        
        self.home_btn = QPushButton("🍑")
        self.home_btn.setMinimumHeight(30)
        self.home_btn.setStyleSheet("background-color: #F98B88; color: peach;")
        
        #Buttons
        self.horizontal.addWidget(self.reload_btn)
        self.horizontal.addWidget(self.home_btn)
        self.horizontal.addWidget(self.url_bar)
        self.horizontal.addWidget(self.go_btn)
        self.horizontal.addWidget(self.back_btn)
        self.horizontal.addWidget(self.forward_btn)
        
        #Le browser
        self.browser = QWebEngineView()
        
        #search bar
        self.go_btn.clicked.connect(lambda: self.navigate(self.url_bar.toPlainText()))
        self.back_btn.clicked.connect(self.browser.back)
        self.forward_btn.clicked.connect(self.browser.forward)
        self.reload_btn.clicked.connect(self.browser.reload)
        self.home_btn.clicked.connect(lambda: self.navigate("http://google.com"))
        
        #Layout
        self.layout.addLayout(self.horizontal)
        self.layout.addWidget(self.browser)
        
        #Starting Url
        self.browser.setUrl(QUrl("http://google.com"))
        
        #Show the window buddy boy
        self.window.setLayout(self.layout)
        self.window.show()
        
        #More Url stuff
    def navigate(self, url):
        if not url.startswith("http"):
            url = "http://" + url + ".com"
            self.url_bar.setText(url)
        self.browser.setUrl(QUrl(url))

class MyTabWidget(QTabWidget):
    def __init__(self):
                
        # Create two tabs
        self.tab1 = QWidget()
        self.tab2 = QWidget()
        
        # Add widgets to first tab
        layout1 = QVBoxLayout()
        label1 = QLabel("This is the content of Tab 1")
        layout1.addWidget(label1)
        self.tab1.setLayout(layout1)
        
        # Add widgets to second tab
        layout2 = QVBoxLayout()
        label2 = QLabel("This is the content of Tab 2")
        layout2.addWidget(label2)
        self.tab2.setLayout(layout2)
        
        # Add tabs to tab widget
        self.addTab(self.tab1, "Tab 1")
        self.addTab(self.tab2, "Tab 2")
        
#Actually starting the thing
app = QApplication(sys.argv)
window = MyWebBrowser()
app.exec_()

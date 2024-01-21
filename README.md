<div align="center">

# 🌐 Destroyer-Browser 🌐

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python](https://img.shields.io/badge/Python-3.6%2B-blue.svg)](https://www.python.org/downloads/)

</div>

### 🌟 Overview
<div align="center">
Destroyer Browser is a lightweight web browser built using Python. It has been enhanced with additional features to prioritize user privacy and security. The browser does not save any user data on the device, including cookies. Additionally, a set of OSINT (Open Source Intelligence) tools has been integrated to enhance the user's ability to gather information online.
</div>

### 📂 Project Structure
```
.
├── destroyer-browser.py
├── icons/
│   ├── exit.png
│   ├── home.svg
│   ├── Back.svg
│   ├── Forward.svg
│   ├── reload.svg
│   ├── new_tab.svg
├── README.md
├── requirements.txt
└── ...
```


### 🛠️ Features 

- **Tabbed Browsing:** 🔄 Open multiple tabs to browse different websites simultaneously.
- **Navigation Controls:** ⬅️⬆️➡️🏠 Back, forward, reload, and home buttons for easy navigation.
- **Bookmarks:** 📚 Quick access to popular websites through the bookmarks toolbar.
- **Closeable Tabs:** 🔄 Close individual tabs with the option to reopen them later.
- **Responsive Design:** 📱 Adjusts to the window size dynamically for a seamless user experience.
- **Browse Privately:** 🔒 Browse without saving any browsing history, cookies, or cached data. Close the browser to remove all associated data.

### OSINT Tools

The following OSINT tools have been integrated for users interested in gathering information online:

- **Shodan:** 🌐 Discover information about devices connected to the internet.
- **DroneBL Lookup:** 🛑 Check if an IP address is listed on the DroneBL blacklist.
- **DNSDumpster:** 🔍 Explore DNS information about a domain.
- **Dehashed Search:** 🔍 Search for leaked passwords and personal information.
- **Cybercrime Tracker:** 🌐 Monitor cybercrime activities and threats.
- **Onyphe:** 🔍 Access information about IP addresses and domains.
- **Ahmia Search:** 🔍 Search the dark web for content.
- **Archive.org Search:** 📜 Explore archived web pages and content.
- **Threat Crowd:** 🌐 Investigate and analyze cyber threats.
- **VirusTotal:** 🦠 Scan files for malware and viruses.

- **Data Removal:** 🧹 Upon exiting the browser, all browsing history, cookies, and cached data are automatically removed to ensure maximum privacy.

### 🚀 Usage

1. **Clone the repository:**
    ```bash
    git clone https://github.com/Destroyer-official/Destroyer-Browser.git
    ```

2. **Navigate to the directory:**
    ```bash
    cd Destroyer-Browser
    ```

3. **📦 Install the required packages:**
    ```bash
    pip install -r requirements.txt
    ```

4. **✨ Execute the script:**
    ```bash
    python destroyer-browser.py
    ```

### 📚 How It Works

Destroyer Browser is built on the PyQt5 and PyQtWebEngine frameworks, utilizing Python for scripting. The browser's core functionality revolves around the following key components:

1. **Tabbed Browsing:**
   - Destroyer Browser enables users to open multiple tabs, each representing a different website or web resource.
   - The tabbed interface allows for convenient multitasking and efficient organization of browsing activities.

2. **Navigation Controls:**
   - Back, forward, reload, and home buttons provide users with intuitive navigation controls for a seamless browsing experience.
   - These controls are implemented using PyQt5 signals and actions, ensuring responsive interaction with the web content.

3. **Privacy and Security:**
   - Destroyer Browser prioritizes user privacy by incorporating an incognito mode.
   - While in incognito mode, the browser ensures that no user data, including browsing history, cookies, or cached data, is stored on the device.

4. **OSINT Tools Integration:**
   - The browser comes equipped with a set of OSINT tools to empower users in gathering information online.
   - Each tool, such as Shodan, DNSDumpster, and VirusTotal, is seamlessly integrated to provide quick access to relevant information.

5. **Data Removal on Exit:**
   - To enhance privacy, all browsing history, cookies, and cached data are automatically removed when the user exits the browser.
   - This feature ensures that no trace of the user's online activity remains on the device.

6. **Responsive Design:**
   - Destroyer Browser adjusts dynamically to the window size, offering a responsive design that adapts to various screen dimensions.
   - This responsiveness ensures a consistent and user-friendly browsing interface across different devices.

7. **Script Execution:**
   - The browser script is executed using Python, leveraging the capabilities of PyQt5 and PyQtWebEngine for web rendering and user interface components.
   - The use of Python provides flexibility and ease of development for both the browser's core features and additional functionalities.

This combination of features makes Destroyer Browser a versatile and privacy-focused web browser with a range of tools for users interested in Open Source Intelligence (OSINT) activities.


### 🤝 Contributing

🤝 Contributions are welcome! For suggestions, enhancements, or issues, feel free to create a pull request or submit an issue in the repository.

---

### 📜 License

⚖️ This project is licensed under the MIT License. Refer to the [LICENSE](LICENSE) file for detailed licensing information.
<div align="center">

---

</div>
```

# IP Extractor

IP Extractor is a Python tool that provides detailed information about an IP address. It displays information like IP version, IP class, hostname, open ports, ASN, ISP, country, geographical coordinates, city, state, and postal code.

## Installation

### Prerequisites

-   Python 3.6 or later

### Clone or Download the Repository

To clone the repository using git, run the following command:

bash

`git clone https://github.com/yourusername/IP-Extractor.git` 

Alternatively, you can download the repository as a ZIP file and extract it to your desired location.

### Installing required packages

To install the required packages, navigate to the repository directory and run the following command:

bash

`pip install -r requirements.txt` 

Here's the `requirements.txt` file with the required packages:

`ipaddress
ipwhois
geocoder
python-nmap` 

Please note that for using `python-nmap`, you need to have `nmap` installed on your system. Below are the installation instructions for various operating systems:

### Windows

1.  Download the latest stable version of Nmap from [the official Nmap download page](https://nmap.org/download.html).
2.  Run the installer with default settings.
3.  Add the Nmap installation directory (usually `C:\Program Files (x86)\Nmap`) to the system PATH environment variable in the `ip_extractor.py` File.

### macOS

Using Homebrew:

bash

`brew install nmap` 

Using MacPorts:

bash

`sudo port install nmap` 

### Linux

On Debian-based distributions:

bash

```bash
sudo apt-get install nmap
```

## Usage

To use the IP Extractor tool, run the following command:

bash

`python IP_Extractor.py` 

Then, enter the IP address when prompted.

## Supported Operating Systems

IP Extractor should work on any operating system with Python 3.6 or later installed, including:

-   Windows
-   macOS
-   Linux

## Contributing

Contributions are welcome! Please create a pull request or open an issue if you have any suggestions or improvements.

## License

This project is licensed under the MIT License. 

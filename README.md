# Layer-7
![LAYER 7](https://github.com/Rip70022/Layer-7/blob/main/LAYER7.jpeg?raw=true)
This `repository` contains a `Python-based` toolkit for performing `Layer 7` `(application layer)` denial-of-service `(DoS)` attacks. It is intended for educational purposes `only`, to help `security professionals` understand and defend against `such attacks`.

## Features

- **Configurable Parameters**: `Easily` set target `IP`, port, `request method` `(GET/POST)`, and `path`.
- **User-Agent Randomization**: Spoof various `browser` `user agents` to avoid `detection`.
- **Multi-Threading Support**: Launch multiple `threads` to `simulate` `high traffic`.
- **Bot Hammering**: Utilize bots for distributed `attack simulation`.

## Installation

1. **Clone the repository**:
   ```bash
   git clone https://github.com/Rip70022/Layer-7.git
   ```
   ```bash
   cd Layer-7
   ```
   
2. **Install dependencies**:
-  Make sure you have Python installed (Python 3 recommended). You can install required libraries using:
   ```bash
   pip install colorama
   ```
   
## Usage:
-  Run the script with the necessary parameters:
   ```bash
   python Layer_7.py -s <target_host> -p <target_port> -t <threads> -a <path> -u <uri> -m <method> -d <data>
   ```
   
## Parameters:
-  `-s` or `--host`: The target host `(e.g., www.example.com)`.
-  `-p` or `--port`: The target port `(default is 80)`.
-  `-t` or `--turbo`: Number of threads to use `(default is 200)`.
-  `-a` or `--path`: Specific path to attack `(e.g., /index.php)`.
-  `-u` or `--uri`: The URI to target `(default is /)`.
-  `-m` or `--method`: The HTTP method to use `(default is GET)`.
-  `-d` or `--data`: Data to send with POST requests `(e.g., user=test&pass=test)`.
  
## Example:
```bash
python Layer_7.py -s www.target.com -p 80 -t 500 -a /login -u /api/login -m POST -d "username=test&password=test"
```

## Warning:
LEGAL NOTICE: IF YOU `ENGAGE` IN ANY `ILLEGAL` ACTIVITY THE `AUTHOR DOES NOT TAKE ANY RESPONSIBILITY FOR IT`. BY `USING` THIS `SOFTWARE`.

## Author:
`Shadow_Sadist/Rip70022`
   

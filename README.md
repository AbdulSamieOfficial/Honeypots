# Honeypot Project - Information Security
A Python-based honeypot project designed to simulate a vulnerable system, log attacker activities, and gather intelligence about their techniques and intentions.

# Please note that running a honeypot can expose your system to potential risks. It is essential to implement proper security measures and monitoring when using a honeypot.

# Features
  1. Simulates a Kali Linux environment with a fake command prompt
  2. Logs usernames, passwords, and commands used by attackers
  3. Handles multiple connections simultaneously using threads
  4. Can be customized to change the simulated environment, login credentials, or response messages
 
# Installation
  1. Clone this repository: 
    
    git clone https://github.com/abdulsamieofficial/Honeypots.git
  2. Change to the project directory:
  
    cd honeypot-project
  3. Install the required dependencies:
  
    pip install -r requirements.txt

# Usage
  1. Open honeypot.py with a text editor and adjust the host variable to your system's IP address.
  2. Run the script:
  
    python3 honeypot.py
  3. Monitor the log.txt file for logged activities from attackers.
  
# Customization
  1. Change the predefined username and password used for authentication by modifying the values in the threaded_client(c) function.
  2. Add or modify commands and responses by editing the cmdTerm(user_cmd,c,user_dict) and commandLS(inp_cmd) functions.
  3. Customize the appearance of the command prompt by adjusting the sendCmds(inp_cmd,c) function. 
  
# Contributing
  1. Fork the repository on GitHub.
  2. Clone your fork and create a new branch for your feature or bugfix.
  3. Commit your changes to your branch.
  4. Push your changes to your fork on GitHub.
  5. Submit a pull request to the original repository.  
 
# License
This project is licensed under the MIT License. See LICENSE for more information.

# Disclaimer
The author is not responsible for any misuse of this project. The honeypot is intended for educational and research purposes only. By using this project, you agree to take full responsibility for any consequences resulting from its usage.


# PID_enumeration

This script is a method to enumerate PID in a linux machine through LFI vulnerability.

*Script developed to solve Backdoor HTB retired machine.*

## How to use it
**1st. Clone the repository with**
*git clone https://github.com/GaboLC98/PID_enumeration*

**2nd. Run the script with**
*python3 PID_enum.py < "url" >  < length > < number_of_PID_to_bruteforce >*
 
 --------------------------------------------

*url = string (e.g. http://backdoor.htb/wp-content/plugins/ebook-download/filedownload.php?ebookdownloadurl=)* 

*min_lenght = int (e.g. 50)*

*total_pid = int (e.g. 5000)*


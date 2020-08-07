# EDIBO
EDIBO projekta elektroniskā klade 
In Linux Ubuntu Terminal
## Day 01 - Day 02
### Topics:
- Terminal (hot-keys)
- Shell (basics)
- Git (basics)
- ASCII table

#### ASCII table
[ASCII table](http://www.ecowin.org/ascii.htm)

#### Terminal (hot-keys)
Ctrl+alt+T - open new Terminal log  
Ctrl+Shift+Q - close Terminal log  
Ctrl+Shift+T - open new Terminal tab  
Ctrl+Shift+ "+" - Zoom in terminal  
Ctrl+Shift+ "-" - Zoom out terminal  
Ctrl+L - move last line of code to upper log part  
To finish command/file name type first letters and press double Tab, ex. De (press double tab) -> Desctop  
To see last used command press ↓ arrow on the keyboard  

#### Shell (basics)
**date**- shows date and time  
**cal** - shows calendar  
**historu** - shows all commands used  
**whoami** - shows user  
**who** - shows who and when logged in from local device  
**last** -  to see when was last connection  
**PS="$"**  - Promt string name change 
**a=11** - add variable a with value 11  
**echo**  - is used to display line of text/string (on Desctop) that are passed as an argument . This is a built in command that is mostly used in shell scripts and batch files to output status text to the screen or a file. (https://www.geeksforgeeks.org/echo-command-in-linux-with-examples/)  
To make math calculation use **((A +,-,*,/,% B))** % - will show surplus    
to open other file type user@epk428-3:~$ **firefox &** & - is used to remain working in terminal, while firefow will open in background  
**pwd**- (print working directory) writes the full pathname of the current working directory to the standard output files marked with blue collor represent files/directory   
**man** - to see command manual ex. *man ls*  
**ls** - Linux shell command that lists directory contents of files and directories (https://www.rapidtables.com/code/linux/ls.html)  
**la** - list all, shows hidden files  
**-l, or other** - is called as a key openes new options ex. ls-l -  list with long format - show permissions  
**mkdir "name"** - used to make new directory (file)  
**rmdir "name"** - used to remove directory  
**cd "name"** - change directory to other one "name"  
**cd ..** - to go 1 step back in directory ex. we have been in /home/user/dev -> type cd .. and then with a next command pwd -> /home/user  
To return to the file home type **cd /home** or  **cd ../..**  
**echo Hello World > a.txt** - used to creathe a .txt file with text  
To reflect on the terminal screen what is inside of the a.txt file, type **cat, head, tail, more, less a.txt**  
To add more rows **echo Hello World! >>a.txt**  
**touch a.txt** - create empty file

**cp a.txt b.txt** - copy a.txt to b.txt  
**init 0** - turn off system  
**exit** - to get out of limited shell  
**git clone https:/github.com/NewFL/EDIBO** - copy file to github  
**hex dump -C README.md** - to see in hexksidecimalo code  
**nano "README.md"** - to modify text  
**history > history_20200807a.txt** - save all history in txt file (ls -lt command used to make sure .txt has been created)  
(Actions to paste creadet files to github ->  
1) git config --global user.email "my email"   
2) git add . - to compile all changed files  
3) git commit -m "20200807_13_30_pirmais_upload_no_cli"  
4) git push origin master)  
**chmod 744 mans_pirmais_skripts.sh / ./mans_pirmais_skripts.sh  /  home/user/..** - to grant acces to execute file rw **x** 

#### Git (basics)
Git is an open-source version control system that was started by Linus Torvalds—the same person who created Linux.  
GitHub used to save created codes and with a system help track it progress and share with other github users. 

A repository is a location where all the files for a particular project are stored.  
README.md -(md - markup document) this created file  




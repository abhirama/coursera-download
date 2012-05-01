1. You should have python(http://www.python.org/) preinstalled for this script to work.
2. Extract download.py and download.cfg files into the folder where you want to download files from Coursera.
3. Edit download.cfg with your Coursera user name, password and the video listing page of the class that you want to donwload. You should have already registered for this class, otherwise this will not work. The example file provided has the link for algo class.
4. Using the command prompt, go to the directory where you extracted download.py and download.cfg and type 'python download.py'.
5. Run the script periodically as the course contents are updated and the script takes care of downloading the newly updated contents.
6. Script creates a directory called .info in the directory where it is present. Do not delete or tamper with this directory as this is where it keeps track of already downloaded content.

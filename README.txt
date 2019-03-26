Description: Python file 'daemon.py' is daemonized and will be run on startup.

In order to make 'daemon.py' run on start up on a Ubuntu machine, you should add it into your Startup Applications, it should be as easy as follows:
1. Move 'daemon.py' to your Desktop.
2. Open Dash (The First Icon In Sidebar). Then type Startup Applications and open that app.
3. Here Click the Add Button on the right.
4. There fill in the details and in the command area browse for 'daemon.py'
5. Restart the system



However, if it is just a linux system not Ubuntu, please follow the alternative:
1. Put 'init.sh' into your Desktop, to check if it works for you

2. Copy it into the /bin manually or use the following command:
sudo cp -i ~/Desktop/daemon.p /bin

3. Adda new Cron job:
sudo crontab -e

4. Scroll to the bottom and add the following line (after all the #'s)
@reboot python /bin/daemon.py& 

5. Restart the system



***Note***
We assume that group 'wheel' has been created for sudo users.

# Part 3 Summary #

This part consists of the following things:

1) Resizing the VM window, and adjusting the VM screen resolution so you can use it in full screen, etc.
2) Finding your way around the LXDE desktop, customising the desktop, etc.

## Changing the virtual screen resolution ##

This requires a bit of fiddling. When you originally start up the image, it probably won't be taking up the entire screen, which is annoying. A rather dodgy way to fix this is to first put it into scale mode, which causes the VirtualBox window to resize. From here, RightCtrl-Home should allow you to change it out of scale mode. This should cause the desktop to resize. From here, you can logout and log back in from the LXDE Start button analogue, and it should be at a much easier to use resolution. This resolution will be saved for future runs. 

## Using LXDE ##

The desktop environment which the image uses is LXDE, the Lightweight X11 Desktop Environment. (X11 refers to the X Window System, the graphics subsystem in a Linux system that manages everything GUI related).

In the default image, LXDE comes with a single panel at the bottom, analogous to the Windows taskbar. You can customise this panel by right clicking on it, and choosing Panel Settings; the settings here are quite self explanatory.

The things you actually see on the taskbar are called applets, which you can customise in the "Panel Applets" tab. For instance, if you didn't want a clock, or you wanted two Start buttons, or anything else, you can use the options to customise it to your liking. The applets themselves also have options, which you can access by right clicking them on the panel; for instance, the start menu analogue applet will allow you to change the image it uses.  

You can also create multiple panels, if you so wish.

LXDE uses the Openbox window manager to manage how windows look. This provides the base of the GUI, whilst LXDE adds stuff like the panels, panel applets, and other things to complete the desktop environment. You can customise how windows look using the Openbox Configuration Manager, available from the Start menu analogue. These options should be quite self-explanatory.

You can also right click on the desktop to undertake actions like changing the wallpaper, etc.

## Customisations ##

We've made a few customisations to the image that people have requested information about.

### Adding entries to the menu ###

In the newest image, there'll be a link for "Chromium with SGS Proxy" that was manually added to the menu. In LXDE, there unfortunately isn't yet a nice graphical way of adding menu entries. You'll have to achieve this manually via ".desktop files".

The .desktop files for the menu are found in /usr/share/applications. A new .desktop file called chromium-browser-schoolproxy.desktop was created, which you can view by opening it up in a text editor. The options should be fairly self-explanatory:

The "Exec" line simply gives the command to execute - in this case, the command is chromium-browser (for chromium) followed by the --proxy-server option, which tells chromium to use the local proxy server provided by ntlmaps, which itself proxies to the school proxy system. The "Categories" line is used to tell LXDE which menu categories to put the entry in.

For people who have an old image and do not want to get the new image simply for a menu entry: You can download the .desktop file in this directory, and put it in your /usr/share/applications directory.

You will probably need root access to do this. You can achieve this by opening a terminal and executing "sudo pcmanfm" (hence giving the file manager window root access), then copying the file to the said directory.

You can get more information on this and all things LXDE at:

wiki.lxde.org/en/Main_Menu

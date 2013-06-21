## The Laconic Guide to Building the Computer Club disk image ##

Q: Who is this for?

- This is for technically able people who want to make their own version of the Ubuntu minimal image that will be placed on the shared drive. Everyone else should just copy over the image once it becomes available. Alternatively, if you want to get a feel for a minimalist build of Linux that doesn't require as much complexity as the extremely hardcore Arch or Gentoo distros, you could try this.
- Linux is about customisation. If you're technically able, there's no reason why you should have to follow the instructions. If you know what you're doing, it's up to you to customise the system as you see fit, change the password, hostname, keyboard layout, file systems, partition setup, etc. The steps are just how we setup the default image.

Q: What will I end up with?

- You will end up with a minimal Ubuntu installation with the LXDE desktop that is exactly the same as the offical image on the shared drive, possibly give or take a few updates. Also, since the official image has been booted and played with multiple times in testing, there will of course be differences in system logs, etc.

Q: What are the prerequisites?

- You should have VirtualBox installed, and have used/played with it
- You should have experience with and not be afraid of text-based interfaces, ncurses-based programs, and the command line.
- NB: You will *not* have a nice mouse/pointy-clicky thing anywhere. There are no pretty Graphical User Interfaces (GUIs) or the like.

Q: Is this dangerous to my files or me?

- No, you're just playing in a VM. Even if you stuff up, nothing outside the VM (i.e. your computer) will be affected.
- Your mental sanity may be affected ;)

### Stuff to Note ###

- The following instructions assume you are following along with the install as you read this guide, which is why some of them have zero context and make no sense when read by themselves

- The following instructions are for building the old image, not the new one that will be pushed to the S drive soon. Those instructions will come shortly.

1) Get mini.iso (the Ubuntu network-install image) from http://archive.ubuntu.com/ubuntu/dists/quantal/main/installer-i386/current/images/netboot/

2) Set up a new virtual machine with your favourite amount of RAM, CPU time, and the like.

3) Attach mini.iso to it, as normal, and start the normal install

4) Languages, location, keyboard layout: English, Australia, and English US keyboard.

5) Hostname for image is "compclub"

6) Australian mirror

7) The build system didn't need proxies.

8) Wait for it to download stuff

9) Username and real name are "ubuntu" for the image. Password for the image is "123"

10) Didn't bother encrypting, because it's a VM.

11) Wait a bit

12) Timezone meh.

13) The stock image had 1 primary partition as ext4 taking up the entire disk, mount point "/". No swap space was allocated. This was done by: (from a clean, unformatted virtual disk)

14) Select Manual partitioning

15) Select sda, create a new partition table on it

16) Create a new primary partition on the free space, using up all of it

17) Leave as "Ext4 Journaling File System". Leave mount point as "/". No disk label. Toggle the bootable flag to "on"

18) Then finish the partitioning, not caring about when it complains about swap

19) Wait for a while as it installs the system

20) "No Automatic Updates"

21) Select "Manual Package Selection"

22) The ncurses Aptitude package manager is a shocking trainwreck on a galactic scale. Quit it immediately.

23) Wait more

24) Install GRUB on MBR, UTC hardware clock

25) Reboot the system and remember to remove the disk, then login

26) Issue the following commands:

sudo apt-get install xorg

sudo apt-get install lxde

sudo apt-get install synaptic

to install a GUI using LXDE and a nice graphical package manager

31) Then issue "startx" and you should get a basic, if somewhat non-full-featured LXDE desktop

32) For some bizarre reason by default there's an "Other" entry in the menu which provides a very long and extremely unhelpful list of "applications". You can remove it by editing /etc/xdg/menus/lxde-applications.menu with your favourite text editor and removing the "Other" entry (it should be obvious where it is if you know your XML)

33) Upon reboot, the system should now boot into a graphical login screen with some poorly configured users. Select "ubuntu,,," and enter the password. This was removed by editing /etc/lxdm/lxdm.conf, setting it to autologin to "ubuntu" and setting display user list to disabled.

33) Customise your system! If you really hate LXDE (like Patrick O'Connell), there are tonnes of other desktops to choose from. If you don't like Chromium, you can uninstall it and install Firefox or something else from Synaptic. You can try out Libreoffice, the free office suite, VLC media player, and thousands of other packages that you can find in the Ubuntu repositories through Synaptic. If you're pro, you don't even have to use the Ubuntu repositories. Or, if you hate Synaptic, you can even replace that!

Extra stuff

1) Shutting down from the shell

sudo shutdown -P now

2) Rebooting from the shell

sudo shutdown -r now

3) If you need proof of Linux's speed, the clean disk image, even in a VM, on the build computer boots in just under 20 seconds and shuts down in 3 seconds.

4) Auto-adjusting screen resolution in VirtualBox. When you increase the window dimensions in VirtualBox, sometimes the screen will stretch, sometimes it'll stay at the same resolution and sometimes it'll try auto-adjusting the resolution, with varying degrees of success. Advice is just to keep trying if it plays up, the default disk image should support auto-adjustment, but it might require reboots with a maximised window or other jumping through hoops to get it working.

5) A note regarding passwords on the shell. By default, when you type in a password at the shell/command line on Linux, it won't display the characters or even "*"s - there's no visual indication of how long your password is, for security reasons. Just type as normal, and press enter - your keypresses are going in, it's not a bug.

6) There may be a problem with networking, which could include a very long boot time with a "Waiting for network configuration" message, or a non-functional internet connection. In this case, run the following command from your favourite terminal emulator:

ifconfig -a

Check the number after "eth". Then open up /etc/network/interfaces, and check the primary network interface. If necessary, adjust the numbers after "eth" to match up with the ifconfig output. Networking problems should be finished after this.

Update: it seems that the networking problems are related to new VMs having different MAC addresses. If you go to Settings, Networking, and advanced options for your adaptor, and set the same MAC address for all your VMs, as well as ensure that the eth* config in Linux is working, then there should be no networking issues no matter what VM you boot the disk image in. As a side note, yes this is the reason why we've gotten everyone to set the MAC address in the network settings.

7) Upon further testing, it has been concluded that the pkexec/PolicyKit/gnome-authentication-agent method of launching Synaptic, which is basically a graphical dialog box that allows you to enter your credentials to launch it, is totally and completely dysfunctional. Problems included the necessary processes refusing to launch upon startup, and other stuff that resisted fixing.

As such, the official image has been tweaked such that the Synaptic link in the menu launches "gksudo synaptic" rather than "synaptic-pkexec".

This was achieved by editing /usr/share/applications/synaptic.desktop and changing the "Exec" line to read "gksudo synaptic" instead of "synaptic-pkexec".

In addition, the policykit-1-gnome package was removed using synaptic as it's now a bit redundant (assuming Synaptic was the only app using it), but of course this is conpletely optional. With that in mind, if any other apps are found using policykit, we'll look more into retrying getting the authentication agent working again, or alternatively move them over to gksudo as well.

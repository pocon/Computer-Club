# Part 4 Summary #

This is where the club is currently at. We'll go through the following things in this part:

1) Package Management, why it is good, how to use Synaptic.

2) General Linux structure and usage - AKA "Where is the C: drive?"

3) Command lines, terminal emulators, and shells - AKA "White text on a black background"

## Package Management ##

Software for most of the major Linux distros comes in blobs called "packages". These can be thought of as analogous to .apks on Android phones. They contain a bundle of stuff, whether that be documentation, a library, debugging information or the GUI component of an application, which can be unpacked and installed on the system. Major distributions maintain centralised repositories of packages, often in the thousands, which the distros pull in from the original creators of the software and repackage and test for the system.

Ubuntu is preconfigured with package management software that points at the Ubuntu repositories; this software manages what packages are installed on your system. Usually, unlike on Windows or Mac (but similarly to app stores on many smartphone OSes), Linux users can simply get all their software from these central repositories.

Package management is perhaps one of the great strengths of a Linux system - the package manager will keep track of all software installed through it on a system, will notify you of all updates, as well as automatically resolve dependencies. These are packages upon which another package depends on - for instance, VLC media player might depend on an audio library. The package manager will automatically install that library when you install VLC. Similarly, if you try removing that library, the package manager will inform you that VLC must also be removed. Finally, if you remove VLC, the package manager will automatically detect that the library is redundant, and notify you it can be safely removed. In this way, package management creates a highly integrated way for the management of software on a Linux system. All packages from a respectable distro's (like Ubuntu) repositories will be cryptographically signed; in this way it means if you stick to these repos, it's almost impossible to install malicious or unwanted software.

### Package management for our image ###

As we've demonstrated in sessions, the main interface to the package manager we're using is "Synaptic". Synaptic provides a graphical interface to the command line tool "apt-get", which provides more low-level control of packages. apt-get itself is an interface to the even more low level "dpkg", which does the actual handling, unpacking and installation of package files.

### Using Synaptic ###

Synaptic is generally quite intuitive to use. (If you want a friendlier option, you can try "Lubuntu Software Center", which can be searched for in Synaptic).
 To search for a package, use the search button. To manipulate a package, click on it, and the relevant options (install, remove, etc.) will be enabled. After you have marked the changes you want, click apply changes to apply them. Synaptic will display dialogs if packages are pulling in others as dependencies.

In "Sections", you'll find the various categorisations for packages
In "Status", you'll find the status the package manager has assigned to each package.

In "Installed", you'll find all installed packages
In "Installed (manual)", you'll find packages that you installed yourself. Installed packages which are NOT here were automatically installed as dependencies. Manually installed packages will not be marked as redundant ever, because it means they have been intentionally installed by the user, and not pulled in by another package
In "Installed (autoremovable)", you'll find packages that were automatically installed as dependencies and are now redundant because the parent package has been removed.

Click "reload" to refresh the package index, which will download the information about the latest versions of packages from the central repo, giving you the most up-to-date package info.

Click "Mark all Upgrades" to automatically mark for installation those packages that have newer versions available (note you still need to click "Apply Changes")

## Filesystem Structure ##

Linux does not have C: or D: drives corresponding to separate partitions, external storage devices, or separate hard drives. Instead, all devices, and partitions in those devices, fall under the root, "/". A *partition* is merely a logical division of a disk - for instance, on most Windows systems with one hard drive, there is "C:" and "D:" - these correspond to two partitions on that one disk.

The system partition (the one Linux is installed on), is given "/". Other partitions, external devices, etc can be "mounted" (i.e., made accessible) in a directory under "/". In Ubuntu, such devices or partitions will be mounted, by default, in the "/media" directory. For instance, if your USB is called "MyUSB", when plugged in, Ubuntu will automatically make the data on it accessible in the "/media/MyUSB" folder. It is also possible to manually mount devices to random other directories, but this is generally not necessary or recommended.

Let's go through the random directories we find under "/":

### /bin ###

/bin contains basic system programs, the most fundamental utilities necessary for the sane operation of the Linux system. Examples include "ls", a very basic command line utility for listing files and directories within a directory. Stuffing around in this directory is not recommended.

### /boot ###

/boot contains files important for the boot process, such as the initial system image which is loaded before anything else. It also contains files for GRUB, the "bootloader", which is a very small piece of code that loads the rest of the operating system. Stuffing around in this directory is not recommended.

### /dev ###

/dev contains really weird files. These files are "abstractions" of physical devices. For instance, /dev/sda represents your actual hard disk, whilst /dev/random represents a stream of random data. These aren't actual files, but abstracted representations of hardware or other stuff. Stuffing around in this directory is not recommended.

### /etc ###

/etc contains the configuration files for many parts of your Linux system. Usually, changing stuff here is not recommended, but sometimes in the course of customisation or fixing a problem editing one of the config files might be necessary.

### /home ###

/home contains the directories for the normal users of the system - a bit like C:\Users on Windows. Since the default user is "ubuntu", in /home/ubuntu you'll find ubuntu's home directory. Do whatever you like in your home directory (however there are some user specific config files here the mangling of which can stuff up your user experience)

### /lib ###

/lib contains the libraries on which programs depend. Stuffing around in this directory is not recommended.

### /media and /mnt ###

These are the directories where devices will be mounted (see above). Ubuntu by default will use /media; /mnt is basically rejected.

### /opt ###

Some random large programs might use this directory. Otherwise, it's kind of a backwater

### /proc and /run ###

More abstract directories to do with running programs. Stuffing around in this directory is not recommended.

### /root ###

The home directory for the root (Administrator) user. Since root is disabled in Ubuntu anyway, this is irrelevant.

### /sbin ###

Another directory containing system programs. Stuffing around not recommended.

### /sys ###

Directories containing important system files. Stuffing around not recommended.

### /tmp ###

A directory for the storage of temporary files by programs. Usually no need to touch this; programs will automatically place/delete files here has needed.

### /usr ###

/usr is for the storage of user-installed programs; /usr/bin and /usr/lib basically correspond to /bin and /lib except that the latter two are for system programs, whilst the former are for user installations.

### /var ###

A bit of a miscellaneous directory for stuff that changes often. For instance, system logs of various things can be found in /var/log.

## The Command Line ##

Command Line interfaces (colloquially, and non-technically known as "shells") play a significant role in the usage of a GNU/Linux system - with proper graphical tools on a full desktop, it's possible to not use it at all, but it's still an important tool to know, and can usually perform tasks faster than on a point and click interface.

A shell is simply a program that allows the user to control the computer. Hence, technically a graphical interface is also a shell. However, this discussion is about command-line shells, which generally take the form of a "working directory", the folder you're currently in, and a part that listens for user commands/input, and subsequently acts on those commands.

The standard shell program for most desktop Linuxen is the Bourne Again Shell, or "bash". The naming is because it descended from an earlier shell program called the Bourne Shell, or "sh".

The terminal emulator program, such as lxterminal, or xterm, is separate from the shell. The terminal emulator does exactly what its name suggests - it emulates a terminal, which is basically a text only display. Shells generally expect to run within a text-only environment (as they are a text-only interface), so a terminal emulator program creates a virtual terminal, within which the shell program is run.

The commands available in a shell environment can generally be divided up into two groups - built in commands, and external executables or scripts.

Built in commands are those that the shell inherently comes with; these generally are commands that configure or display information about the shell itself, such as "cd", the change directory command, which changes the directory the shell is currently in.

External commands are those executables that can be run from a shell. These could expect or display text to the terminal (emulated or not), and perform other actions - examples might be a terminal based text editor such as vi.

This is only a very basic introduction to the command-line interface on Linux; for more information, you should look at the Cool Stuff file, which contains some links to good introductory tutorials that go more in depth into shells and how to use them.

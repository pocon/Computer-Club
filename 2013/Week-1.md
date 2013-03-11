# Week 1 Summary #

The first week is about a general introduction to what Linux is, why we care, free and open source software (FOSS), and the basic foundations of running a GNU/Linux system inside a virtual environment (VirtualBox)

## Miscellaneous Stuff ##

- This club will not automagically turn you all into badass supergeeks. That requires time and effort.
- Whilst Linux encourages customisation and tweaking at quite a low level, hacking is not condoned. Please do not tamper with school systems, port scan stuff, etc etc.

## Operating Systems (OSes) ##

- Operating Systems are those "master programs" that manage a computer's resources and oversees user programs. Examples: Microsoft Windows, Mac OSX
- Linux is an operating system *kernel*
- A kernel is the central part of an OS which juggles resources between user programs, manages hardware, etc.
- Other programs, such as the desktop environment (i.e. stuff you can click on), various utilities, etc. run on top of the kernel and make up the rest of the operating system
- In most desktop Linux systems, a lot of this user stuff is provided by the GNU project, hence many Linux OSes might be called "GNU/Linux"
- However most people simply call the whole OS "Linux"
- Similarly, Android is an operating system that has Google's touch optimised interface, etc. built on top of the Linux kernel
- Linux is NOT a program that you install on Windows or Mac. It is a replacement for these.

## A bit of history ##

- The Linux kernel was first written back in the 1990s by a cool kid from Scandinavia
- This was combined with the GNU project, which had been going since the 1980s, to make a usable GNU/Linux operating system

## How is Linux important today? ##

- Linux is popular in enterprise for its security, reliability, and customisability
- 95% of supercomputers run Linux, again for reliability and customisability
- The majority of web servers run Linux
- Android runs on a Linux kernel

## Why should we use/care about Linux? ##

- Free and open source software (FOSS) - GNU/Linux and many programs written for it are based on the principles of customising, sharing and working together as a community (it's also completely free. 100%. If you pay for Linux, you're either paying for other stuff like support, or you're getting swindled)
- Customisable. The user has the POWAH
- Secure. Much more so than even Mac, and definitely Windows. The Android malware situation is not applicable to GNU/Linux systems.
- Reliable. Linux systems rarely crash, if ever, which is why the majority of web servers use Linux, and can stay continuously online for years
- Fast. Windows is slow and bloated. The fastest Linux desktops can boot from cold start in under 5 seconds, but a standard installation will still shave tens of seconds off startup times. Interfaces are faster and more responsive, because of lighter memory requirements. Linux systems also take up much less disk space.

## Linux Distributions ##

- Distributions, aka "distros", are various flavours of Linux that are typically GNU/Linux systems with different desktop interfaces and programs slapped on top, allowing them to be used for different purposes
- Some distros might aim to be good desktop systems, others may be optimsed for low end machines/laptops, others may be optimised as secure systems, still others are designed to be portable and able to be carried around on a USB to be booted on any supported computer you come across
- distrowatch.com has quite a comprehensive list (i.e. hundreds). If you're just starting, it's probably best to start with the few most popular ones. (NB: distrowatch also talks about a number of "BSD" systems, like FreeBSD, etc, these are substantially different, but still FOSS, OSes that generally require much more tech knowledge and ability to install and use

### Some popular distributions ###

- Ubuntu: considered one of the best distros for beginners, it provides a fancy modern desktop known as Unity. It's developed by Canonical Ltd and the associated community, and was originally forked from Debian
- Debian: the "Universal Operating System", Debian has succeeded in building an extremely stable, reliable system that supports many different CPUs, at the cost of having extremely outdated software that is kept "up-to-date" through a rather complex system of backports (don't worry if you don't know what that means). As a result, people love it for use as servers, but probably not the ideal desktop solution. Also, Debian sticks very firmly to FOSS values. Debian provides the old, venerable GNOME 2 desktop environment
- Linux Mint: a distro based off Ubuntu (but also Debian if you so wish), which aims also to be an extremely user friendly, beginner-friendly distribution. Linux Mint comes with either the Cinnamon or MATE desktops, which are reimaginings of the original GNOME 2 environment (more on this below)
- Fedora: A distro from the Linux company Red Hat, which is used to test new features going into the commercial Red Hat Enterprise Linux. It places a particular focus on security and FOSS principles, and uses the GNOME 3 desktop (not GNOME 2). Also quite a good choice for the Linux beginner.
- Arch and Gentoo: Distros for pros, these provide total control over your system starting from a minimalist beginning. Definitely NOT recommended for beginners, or even intermediate Linux users.
- openSUSE, Mandriva, Mageia: Random distros which I know have something to do with Novell but that's all I know...

### Desktop environments ###

- Unlike Windows or Mac, in Linux there is a large variety of different "Desktop Environments"/"Window Managers" you can choose from, which basically mean different styles of Graphical User Interfaces, or GUIs
- Even though distributions generally have a desktop they are associated with, desktops can be easily changed, as they are simply programs that are installed/uninstalled
- These are generally built on top of the X server, which is a subsystem providing graphical services to Linux programs
- GNOME: A popular desktop environment. THe old GNOME 2 was one of the most famous desktops. Its update to the overhauled GNOME 3 caused quite a bit of controversy, and GNOME 2 has sprung up in various reincarnations, like Cinnamon and MATE
- KDE: Another popular, full featured desktop environment with nice integration between the various parts and widgets
- Xfce, LXDE: Lightweight, slightly less full-featured desktops that aim to be less memory and CPU-hogging than the full desktop environments
- Unity: Ubuntu's own little desktop environment because it's special. Also caused quite a bit of controversy when it replaced GNOME 2, which Ubuntu originally used. That said it is modern, slick and quite usable.
- Enlightenment: A lightweight desktop/window manager which the author knows nothing about
- wmii, dwm, xmonad, ratpoison, twm, icewm, flvm, openbox, fluxbox, blackbox, etc.: Really minimalist and lightweight window managers which are used by the pros (like Patrick O'Connell) and make Windows 95 seem full-featured. Definitely not recommended for beginners.
Still need bit on virtualisation, installation

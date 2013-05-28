# Part 1 Summary #

The first week is about a general introduction to what Linux is, why we care, free and open source software (FOSS), and the basic foundations of running a GNU/Linux system inside a virtual environment (provided by VirtualBox)

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

- The Linux kernel was first written back in the 1990s by a cool kid from Scandinavia (Linus Torvalds)
- This was combined with the GNU project, which had been going since the 1980s, to make a usable GNU/Linux operating system
- A bit of stuff relating to the club's discussions about Unix, Mac and Linux, and how they're all related:
- First, see the Wikipedia article on Unix. As was shown in the club it has a very nice graphic showing how everything is related.
- Linux is an open-source REWRITE of Unix. It tries to provide a Unix-compatible system that is distinctly Unix-flavoured, but does not contain any actual Unix code. Mac OSX is something that has direct descent from the original Unix. 

## How is Linux important today? ##

- Linux is popular in enterprise for its security, reliability, and customisability
- 95% of supercomputers run Linux, again for reliability and customisability
- The majority of web servers run Linux
- Android runs on a Linux kernel

## Why should we use/care about Linux? ##

- Free and open source software (FOSS) - GNU/Linux and many programs written for it are based on the principles of customising, sharing and working together as a community (it's also completely free. 100%. If you pay for Linux, you're either paying for other stuff like support, or you're getting swindled)
- Customisable. The user has the power, to customise every single detail of the system, to tailor their computer to their needs and wants.
- Secure. Much more so than even Mac, and definitely Windows. The Android malware situation is not applicable to GNU/Linux systems.
- Reliable. Linux systems rarely crash, if ever, which is why the majority of web servers use Linux, and can stay continuously online for years
- Fast. Windows is slow and bloated. The fastest Linux desktops can boot from cold start in under 5 seconds, but a standard installation can still shave tens of seconds off startup times. Interfaces are faster and more responsive, because of lighter memory requirements. Linux systems also take up much less disk space. NB: Due to the inefficiency that virtualisation places on, well, everything, the true speed of a Linux system is much faster than what a virtualised interface might show.

## What is this "Open Source" thing? ##

- Computer programs today, whether user applications, operating systems, etc, are almost always written in one of many programming languages - abstract representations of the actual code that is designed to be easily learnt, interpreted, and created by human beings - this is the "source code"
- Proper programs, OSes and the like must be *compiled* by a special program known as a compiler into machine code, which is binary stuff that can only then be read and executed by a computer's processor
- To read or attempt to convert such machine code back into the readable stuff is extremely difficult, and effectively impossible except for people who have far too much time on their hands
- This means that such programs, without the source code, are impossible for users to modify or use in anyway except as the creator originally intended
- Such things are known as "closed source"
- Open source programs are released under a license that gives the user the source code. In addition, they generally come with licenses that explicitly permit the user to modify, play with, etc. the code, because this is clearly important to being able to customise said program
- Also, many open source licenses, such as the GNU General Public License, come with clauses that force any modifications to the program to also be released under the same license, allowing the open source community to grow
- Open source allows a worldwide community of developers to review, modify, and improve the code whenever they want, and allows anyone to be part of this community. The many pairs of eyes passing over the code means security bugs are fixed very quickly

## Linux Distributions ##

- Distributions, aka "distros", are various flavours of Linux that are typically GNU/Linux systems with different desktop interfaces and programs slapped on top, allowing them to be used for different purposes
- Some distros might aim to be good desktop systems, others may be optimsed for low end machines/laptops, others may be optimised as secure systems, still others are designed to be portable and able to be carried around on a USB to be booted on any supported computer you come across
- distrowatch.com has quite a comprehensive list (i.e. hundreds). If you're just starting, it's probably best to start with the few most popular ones. (NB: distrowatch also talks about a number of "BSD" systems, like FreeBSD, etc, these are substantially different, but still FOSS, OSes that generally require much more tech knowledge and ability to install and use. Not recommended for beginners.)

### Some popular distributions ###

- Ubuntu: considered one of the best distros for beginners, it provides a fancy modern desktop known as Unity. It's developed by Canonical Ltd and the associated community, and was originally forked from Debian
- Debian: the "Universal Operating System", Debian has succeeded in building an extremely stable, reliable system that supports many different CPUs, at the cost of having extremely outdated software that is kept "up-to-date" through a rather complex system of backports (don't worry if you don't know what that means). As a result, people love it for use as servers, but it's probably not the ideal desktop solution. Also, Debian sticks very firmly to FOSS values. Debian provides the old, venerable GNOME 2 desktop environment
- Linux Mint: a distro based off Ubuntu (but also Debian if you so wish), which aims also to be an extremely user friendly, beginner-friendly distribution. Linux Mint comes with either the Cinnamon or MATE desktops, which are reimaginings of the original GNOME 2 environment (more on this below)
- Fedora: A distro from the Linux company Red Hat, which is used to test new features going into the commercial Red Hat Enterprise Linux. It places a particular focus on security and FOSS principles, and uses the GNOME 3 desktop (not GNOME 2). Also quite a good choice for the Linux beginner.
- Arch and Gentoo: Distros for pros, these provide total control over your system starting from a minimalist beginning. Definitely NOT recommended for beginners, or even intermediate Linux users.
- openSUSE, Mandriva, Mageia: Some other random distros.

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

## Getting Linux ##

- Linux distributions are typically availble as CD images (.iso) from the distribution websites. These can be burned to CD or USB and booted.

## Running Linux ##

- Linux can be installed normally on a hard drive and used in place of Windows. This is usually done by running the installation CD/USB/whatever
- Linux can also be taken for a "test drive" via Live CD/DVD/USB. In this instance, it is not installed to disk but run straight from the removable media. As you're not touching the hard drive at all, this is an easy and safe method to try out Linux with little risk. However, due to the read-only nature of many such live disks (e.g. CDs), persistence, or the saving of settings and files across reboots, is generally limited
- Multiboot - this involves installing Linux alongside Windows/even other Linux. You will be able to choose an option to boot upon computer startup. This is often useful if you'd like to use Linux but there are things in Windows you can't do without.
- Virtualisation involves the emulation of a "fake" or "virtual" environment, enabling Linux, or another OS, to be run "inside" an existing OS. The virtualisation software creates a pretend environment, simulating the presence of a processor, memory, screen, and other hardware to the guest OS, or the OS that is being virtualised. In this way, Linux can be run easily within Windows without anything at risk except a virtual disk file, or even Windows within Linux, or Linux within Linux.

## Virtualisation with VirtualBox ##

- VirtualBox is a popular, open source, and easy-to-use option for virtualisation
- You can get it here: https://www.virtualbox.org
- See the Start-Here.md tutorial file in this directory for detailed instructions on how to set up VirtualBox.

## Our Linux setup ##

- We plan to use VirtualBox to virtualise a Linux environment within the school computer.
- We'll be using a customised version of Ubuntu, built from the minimal Ubuntu network installer, using LXDE as our desktop environment
- Please see the Start-Here.md tutorial for how to set up your virtual disk. A starting disk image, with the chosen setup already installed, will be provided on the shared drive at school
- You'll need a USB, preferably 8GB (4GB is usable, but will restrict how much stuff you can add). You can carry around the virtual disk image containing your Linux installation, run it using VirtualBox at school, and also with your VirtualBox install at home (indeed, you can run it with any VirtualBox installation you can access)
- At any time, if you stuff up your disk image, if you've made a backup you can just switch to that, or simply recopy the original disk image from the shared drive

## Other setups ##

- We won't be installing Linux on the school computers, or booting Live USBs/CDs. However, if you wish, you have some other options available to you:

### Bring your own hardware ###

- You could simply bring along a laptop on which you're willing to install or multiboot Linux.
- If you choose to do so, obviously be aware of the risk of damage, theft, etc.
- Hardware compatibility and Linux can sometimes be problematic; we make no guarantees that we will be able to fix, rescue, or otherwise troubleshoot your setup
- Installing Linux is an involved process that can require more technical knowledge. You can, if you're not careful, destroy files you wanted not to be destroyed. This includes things you might have wanted kept, like Windows, family photos, or your English essay. Whilst we'll provide what support we can, you may find yourself relying on documentation, manuals, and random blog posts for information. That's how a lot of DIY Linux users roll - relying on the massive community that's grown up around Linux, in the form of forums, chat rooms, and the like.
- The advantages of this, however, are clearly the much greater customisation possible than using a pre-installed image, much greater speed due to the lack of virtualisation, etc.

### Custom install in VirtualBox ###

- You could, rather than using a pre-installed Linux image, install any distro in your own virtual disk image
- A tutorial/guide on our specific setup with Ubuntu-minimal will be available shortly.
- Those of you who want the added challenge of installing Linux without putting actual hardware or such at risk might want to try this approach.
- Bear in mind though that if you want to transfer your customised install to actual hardware and run it natively (i.e., not inside a VM), this might be quite an involved and complex process

PS: FYI, this summary was written in vi. emacs sucks.

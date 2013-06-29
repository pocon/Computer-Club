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

21) Select "Lubuntu minimal installation" - don't install any other packages, unless you want to

23) Wait more

24) Install GRUB on MBR, UTC hardware clock

25) Reboot the system and remember to remove the disk, then login

This will give you a stripped down Lubuntu installation. It won't be configured to work with the school proxy, and only contain a really basic set of apps.

Things to note:

- Since the "Linux" iteration of the Computer Club began, Ubuntu has had another release. The image link above is for version 12.10, whilst the current version as of June is 13.04. You might like to try the newer installer, or given that the Linux plot arc is over, try another distribution. GNU/Linux is much bigger than just Ubuntu!

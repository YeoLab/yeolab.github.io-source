Title: Access TSCC files locally with SSHFS
Date: 2020-05-28
icon: mdi mdi-account-multiple

# Access TSCC files locally with SSHFS

**Authors**: Clarence Mah, Brian Yee<br>
**Last Updated**: 5-07-20

You should be able to double click the downloaded packages to run (for Macs!):

**FUSE:** [Latest as of 2020/02/21](https://github.com/osxfuse/osxfuse/releases/download/osxfuse-3.10.4/osxfuse-3.10.4.dmg)

**SSHFS:** [Latest as of 2020/02/21](https://github.com/osxfuse/sshfs/releases/download/osxfuse-sshfs-2.5.0/sshfs-2.5.0.pkg)

## Using SSHFS

Create a directory (or use an empty directory - has to be empty!)

```bash
mkdir -p ~/sshfs/home
```

Mount a remote drive to your local empty directory

```bash
sshfs USERNAME@tscc-login1.sdsc.edu:/home/USERNAME ~/sshfs/home -o follow_symlinks
```

- Replace `USERNAME` with your TSCC login name.
- Replace `tscc-login1` with `tscc-login2` if you prefer.
- The `-o follow_symlinks` will follow symlinks within your mounted directory

## Alias this command (optional)

Attach this command to something shorter so you don’t have to remember the full command and add this to your `~/.bashrc`.

For example, if my TSCC username is `brianyee01` and my local mount directory is `/Users/brianyee/sshfs/home`, I could add the following line to my `~/.bashrc` file so I can mount simply by typing `sshfs_home`:

```bash
alias sshfs_home="sshfs brianyee01@tscc-login1.sdsc.edu:/home/brianyee01 /Users/brianyee/sshfs/home -o follow_symlinks"
```

“refresh” your `.bashrc` file to see changes:

```bash
source ~/.bashrc
```

Navigate to the directory you created earlier, and you should be able to see your TSCC files!

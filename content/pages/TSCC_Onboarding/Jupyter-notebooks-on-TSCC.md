# Jupyter notebooks on TSCC

**Authors**: Clarence Mah, Brian Yee<br>
**Last Updated**: 5-07-20


**Warning: Do NOT run your Jupyter notebook on the login node. Doing so will cause everything to slow to a crawl for everyone on the cluster. Follow the instructions below for running your notebooks in interactive jobs, thank you!**

This has two sections: Setup and Running. They should be done in order :)

## 1. Setup Jupyter notebooks on TSCC

- First, on your personal computer, you will want to set up [passwordless ssh](http://www.linuxproblem.org/art_9.html) from your laptop to TSCC. For reference, `a@A` is you from your laptop, and `b@B` is TSCC. So everywhere you see `b@B`, replace that with `yourusername@tscc.sdsc.edu`. For `a@A`, since your laptop likely doesn’t have a fixed IP address or a way to log in to it, you don’t need to worry about replacing it. Instead, use `a@A` as a reference point for whether you should be doing the command from your laptop (`a@A`) or TSCC (`b@B`)
- To set up Jupyter notebooks on TSCC, you will want to add some `alias` variables to your  `~/.bashrc`

```
IPYNB_PORT=[some number above 1024]
alias tscc='ssh obotvinnik@tscc-login2.sdsc.edu'
```

This way, I can just type `tscc` and log onto `tscc-login2` **specifically**. It is important for Jupyter notebooks that you always log on to the same node. You can use `tscc-login1` instead, too, this is just what I have set up. Just replace my login name (“`obotvinnik`”) with yours.

- Activate all the commands you just added:

```bash
source ~/.bashrc
```

- Next, type `tscc` and log on to the server.
- On TSCC, add these lines to your `~/.bashrc` file.

```
IPYNB_PORT=same number as the above IPYNB_PORT from your laptop
alias ipynb="jupyter notebook --no-browser --port $IPYNB_PORT &"
alias sshtscc="ssh -NR $IPYNB_PORT:localhost:$IPYNB_PORT tscc-login2 &"
```

Notice that in `sshtscc`, I use the same port as I logged in to, `tscc-login2`. The ampersands “`&`” at the end of the lines tell the computer to run these processes in the background, which is super useful.

- You’ll need to run `source ~/.bashrc` again on TSCC, so the `$IPYNB_PORT` variable, and `ipynb`, `sshtscc` aliases are available.
- Set up passwordless ssh between the compute nodes and TSCC with:

```
cat .ssh/id_rsa.pub >> .ssh/authorized_keys
```

- Back on your home laptop, edit your `~/.bash_profile` on macs, `~/.bashrc` for other unix machines to add the line:

```
alias tunneltscc="ssh -NL $IPYNB_PORT\:localhost:$IPYNB_PORT obotvinnik@tscc-login2.sdsc.edu &"
```

Make sure to replace “`obotvinnik`” with your TSCC login :) It is also important that these are double-quotes and not single-quotes, because the double-quotes evaluate the `$IPYNB_PORT` to the number you chose, e.g. `4000`, whereas the single-quotes will keep it as the letters `$IPYNB_PORT`.

## 2. Run Jupyter Notebooks on TSCC

Now that you have everything configured, you can run Jupyter notebooks on TSCC! Here are the steps to follow.

- Log on to TSCC
- Now that you have those set up, start up a `screen` session, which allows you to have something running continuously, without being logged in.

```
screen -x
```

**Note:** If this gives you an error saying “There is no screen to be attached” then you need to run plain old `screen` (no `-x`) first.
If this gives you an error saying you need to pick one session, make life easier for yourself and pick one to kill all the windows in, (using `Ctrl-j K` if you’re using the `.screenrc` that I recommended earlier, otherwise the default is `Ctrl-a K`). Once you’ve killed all screen sessions except for one, you can run `screen -x` with abandon, and it will connect you to the only one you have open.

- In this `screen` session, now request an interactive job, e.g.:

```
qsub -I -l walltime=2:00:00 -q home-yeo -l nodes=1:ppn=1
```

- Wait for the job to start.
- Run your TSCC-specific aliases on the compute node:

```
ipynb sshtscc
```

- **Back on your laptop**, now run your tunneling command:

```
tunneltscc
```

- Open up `http://localhost:[YOUR IPYNB PORT]` on your browser

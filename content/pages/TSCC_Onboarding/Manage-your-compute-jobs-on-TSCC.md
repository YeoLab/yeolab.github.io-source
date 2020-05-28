Title: Manage your compute jobs on TSCC
Date: 2020-05-28
icon: mdi mdi-account-multiple


# Manage your compute jobs on TSCC

**Authors**: Clarence Mah, Brian Yee<br>
**Last Updated**: 5-07-20


## Submit jobs

To submit a script that you wrote, in this case called `myscript.sh`, to TSCC, do:

```
qsub -q home-yeo -l nodes=1:ppn=2 -l walltime=0:30:00 myscript.sh
```

- `-q home-yeo` specifies which queue your job is submitted to
- `-l nodes=1:ppn=2` requests 1 node and 2 processors per node
- `-l walltime=0:30:00` reserves the requested nodes for 30 minutes

## Submit interactive jobs

To submit interactive jobs, add the `-I` interactive flag:

```
qsub -I -q home-yeo -l nodes=1:ppn=2 -l walltime=0:30:00
```

## Helpful hints

Unless your software/module utilizes MPI (if you don't know what MPI, is don't worry about it), you will only need 1 node (`nodes=1`) per job. Most jobs (such as running Jupyter) require only 1-2 ppn (`ppn=1`), however memory-intensive jobs (ie. STAR) may require up to 8 ppn.

Generally speaking, you cannot modify walltime after your job request is granted. So if you think 2 hours to run a job, best to request 3 or 4 hours of walltime (`walltime=3:00:00`).

## Check job status, aka “why is my job stuck?”

Check the status of your jobs (replace bay001 with your username):

```
qstat -u bay001
```

outputs:

```
(brian)[bay001@tscc-login2 ~]$ qstat -u bay001

tscc-mgr.sdsc.edu:
                                                                                  Req'd    Req'd       Elap
Job ID                  Username    Queue    Jobname          SessID  NDS   TSK   Memory   Time    S   Time
----------------------- ----------- -------- ---------------- ------ ----- ------ ------ --------- - ---------
2006527.tscc-mgr.local  bay001      home-yeo STDIN             35367     1     16    --   04:00:00 R  02:35:36
2007542.tscc-mgr.local  bay001      home-yeo STDIN              6168     1      1    --   08:00:00 R  00:28:08
2007621.tscc-mgr.local  bay001      home-yeo STDIN               --      1     16    --   04:00:00 Q       --
```

## Check job status of array jobs

Check the status of your array jobs, you need to specify `-t` to see the status of the individual array pieces.

```
qstat -t
```

## Killing jobs

If you have a job you want to stop, kill it with `qdel JOBID`, e.g.

```
qdel 2006527
```

## Kill an array job

If the job is an array job, you’ll need to add brackets, like this:

```
qdel 2006527[]
```

## Kill ALL your jobs

To kill all the jobs that you’ve submitted, do:

```
qdel $(qselect -u $USER)
```

## Which queue do I submit to? (check status of queues)

Check the status of the queue (so you know which queues to NOT submit to!). Generally, `home-yeo` queues move more quickly but we also have condo and hotel available to us should `home-yeo` queues be full.

```
qstat -q
```

Example output is,

```
(olga)[obotvinnik@tscc-login2 ~]$ qstat -q

server: tscc-mgr.local

Queue            Memory CPU Time Walltime Node  Run Que Lm  State
---------------- ------ -------- -------- ----  --- --- --  -----
home-dkeres        --      --       --      --    2   0 --   E R
home-komunjer      --      --       --      --    0   0 --   E R
home-ong           --      --       --      --    2   0 --   E R
home-tg            --      --       --      --    0   0 --   E R
home-yeo           --      --       --      --    3   1 --   E R
home-visres        --      --       --      --    0   0 --   E R
home-mccammon      --      --       --      --   15  29 --   E R
home-scrm          --      --       --      --    1   0 --   E R
hotel              --      --    168:00:0   --  232  26 --   E R
home-k4zhang       --      --       --      --    0   0 --   E R
home-kkey          --      --       --      --    0   0 --   E R
home-kyang         --      --       --      --    2   1 --   E R
home-jsebat        --      --       --      --    1   0 --   E R
pdafm              --      --    72:00:00   --    1   0 --   E R
condo              --      --    08:00:00   --   18   6 --   E R
gpu-hotel          --      --    336:00:0   --    0   0 --   E R
glean              --      --       --      --   24  75 --   E R
gpu-condo          --      --    08:00:00   --   16  36 --   E R
home-fpaesani      --      --       --      --    4   2 --   E R
home-builder       --      --       --      --    0   0 --   E R
home               --      --       --      --    0   0 --   E R
home-mgilson       --      --       --      --    0   4 --   E R
home-eallen        --      --       --      --    0   0 --   E R
                                               ----- -----
                                                 321   180
```

So right now is not a good time to submit to the `hotel` queue, since it has a bunch of both running and queued jobs!

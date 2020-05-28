# Running the eCLIP Pipeline on TSCC

**Authors**: Clarence Mah, Brian Yee<br>
**Last Updated**: 5-07-20


These are basic See the `github` [https://github.com/yeolab/eclip](https://github.com/yeolab/eclip) for more detailed instructions.

Load the `eclip` module into your environment:

```bash
module load eclip/0.5.0
```

If you look at `$ECLIP_HOME/examples/` you'll see an example template `REFERENCE_SE_TEMPLATE.yaml`. Since the template specifies the full paths to these files, you should be able to copy and just run inside a scratch directory:

```bash
# the pipeline needs an interactive node to act as the head node that submits jobs to other nodes
qsub -I -q home-yeo -l nodes=1:ppn=1 -l walltime=80:00:00;

mkdir /oasis/tscc/scratch/bay001/example_clip
cp $ECLIP_HOME/examples/REFERENCE_SE_TEMPLATE.yaml ./
chmod +x ./REFERENCE_SE_TEMPLATE.yaml
./REFERENCE_SE_TEMPLATE.yaml
```

This will create a folder called `REFERENCE_SE_TEMPLATE` (it'll create a folder with the same name as the file, minus ext) and begin running the main pipeline (`fastq` -> `peaks`). In the meantime, feel free to poke around and refer to the github page for more documentation on steps/outputs/etc.

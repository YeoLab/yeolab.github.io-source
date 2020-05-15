Title: Research
Date: 2015-07-29 11:46
icon: mdi mdi-magnify

<style>
.image:before{
  background-image: None;
  height: 100%;
}
em{
  font-style: italic;
}
</style>

<div class="row">
  <div class="6u">

<section>
  <a href="#stem-cells" class="image feature"><img src="/images/research/IMP1_OCT4 IF_2.svg" alt="" /></a>
  <header>
    <h3>Homeostasis in pluripotent stem cells</h3>
  </header>
  <p>We study how RNA binding proteins and RNA modifications affect cellular homeostasis in human pluripotent stem cells.</p>
</section>

  </div>
  <div class="6u">

<section>
  <a href="#neural-rbps" class="image feature"><img src="/images/research/neuron.svg" alt="" /></a>
  <header>
    <h3>Neural RNA binding proteins</h3>
  </header>
  <p>We are interested in how defects in RNA binding proteins cause neurological disease, such as ALS.</p>
</section>

  </div>
</div>
<div class="row">
  <div class="6u">

<section>
  <a href="#rna-processing" class="image feature"><img src="/images/research/mRNP.svg" alt="Decoding the relationships between RNAs, their binding partners, and the effect on the RNA life cycle"/></a>
  <header>
    <h3>RNA Processing</h3>
  </header>
  <p>We study post-transcriptional processing of RNAs by multiple mechanisms.</p>
</section>

  </div>
  <div class="6u">

<section>
  <a href="#single-cell" class="image feature"><img src="/images/research/immunology_singlecell.svg" alt="" /></a>
  <header>
    <h3>Single-cell analyses</h3>
  </header>
  <p>We develop new computational approaches to decipher biological meaning from thousands of single-cell RNA-seq/proteomics data.</p>
</section>

  </div>
</div>


A major focus of our lab is to understand how gene expression is controlled at the RNA level to maintain proper functioning of cells during development and aging.  Over the past decade, there has been a dramatic increase in the recognition that members of a broad class of proteins termed RNA binding proteins (RBPs) are crucial for **maintaining molecular and cellular homeostasis**. RBPs regulate processes such as cell survival, pluripotency of embryonic stem cells, and neuronal function, as well as aid in the transition between cellular states in **response to stimuli**, such as during neural specification of stem cells, cellular stresses, or viral infections.

RBPs perform these tasks by influencing the fate of hundreds to thousands of target RNAs via interactions with specific sequences or RNA secondary structural features within the transcribed RNA molecule (Figure 1A) to regulate **post-transcriptional processing of RNA** such as alternative splicing, polyadenylation, stability and turnover, localization, or translation control. Consequently, mutations or defects in the expression and/or localization of these RBPs (Figure 1B) cause a diversity of diseases such as neurodegeneration, cancer, and obesity. With the increasing number of proteins that are now classified as RBPs (more than a thousand) and the startling variation in diseases that they seem to cause, fundamental questions about how RBPs function, which RNA targets they interact with, and how they regulate gene expression remain unsolved.  In particular, addressing these in the context of development and genetic diseases is crucial to predicting consequences of abnormal behavior of these RBPs and identifying new therapeutics for human diseases.     

In our group, our primary aims have been to uncover regulatory principles of how RBPs influence RNA processing.  Specifically:

1. How do RBPs maintain cellular homeostasis in different cell-types and in development?
2. How do RBPs change in expression and respond to environmental stimuli (such as cellular stress and virus infection)?   
3. How do RBPs give rise to disease-relevant phenotypes when altered?

In doing so, our secondary aims are:

4. Developing molecular and chemical methods to alter RBP-RNA interactions to modulate gene expression.
5. Engineering novel protein-complexes that interact with RNA at specific sites to track and modulate RNA expression.
6. Developing computational and experimental workflows for understanding RNA processing at the single-cell level.

**Our work strikes an important balance between hypothesis-driven research and exploration**. In my lab, we apply a wide variety of approaches that include molecular biology, biochemistry, imaging, high-throughput sequencing, and large-scale genetic, genomics and chemical screens.  One of our key strengths is in our ability to analyze diverse and large datasets generated from high-throughput genomics/genetics approaches in a rigorous and reproducible manner. From our explorations, we have identified many novel RNA targets of RNA binding proteins and new mechanisms of regulation. This balance is a key point in our lab as it encourages trainees to keep an open scientific mind while still testing specific hypotheses.

 
## Fundamental insights from global perspectives.

### Homeostasis in pluripotent stem cells <a name="stem-cells"></a>

Post-transcriptional regulation of gene expression had been proposed to be important for the survival and pluripotency of pluripotent stem cells (PSCs).  PSCs are an infinite resource for regenerative medicine and an exciting and accessible system for modeling human development and diseases in a dish.  My research in this area focuses on hypotheses underlying the importance of candidate RBPs with two characteristics, namely RBPs that are highly expressed in PSCs compared to other cell-types, and whose expression levels decrease when PSCs are differentiated towards mature lineages.

*RBFOX2*. Our expectation was that alternative splicing changes in many genes would accompany the differentiation of PSCs to mature lineages.  However it was not known which are these genes and which RBP (splicing factor) would be responsible for alternative splicing changes.  To test the hypothesis that one or more RBPs are responsible for modulating these changes, we had performed an *unbiased identification of alternative splicing (AS) events during neural differentiation of human embryonic stem cells (hESCs) using splicing-sensitive microarrays* (Yeo et al.).  We found that the motif (U)GCAUG was enriched within introns proximal to alternative exons in hESCs.  Thus, we pursued the Rbfox family of RBPs that was known to bind to (U)GCAUG to regulate alternative splicing. Unsatisfied with selecting single genes that frequently lead to conclusions that do not generalize to the majority of RNA targets, we isolated direct RNA binding sites of RBFOX2 across the transcriptome using my modification of the cross-linking and immunoprecipitation (CLIP) technology.  As one of the first lab to adapt the technology for high-throughput sequencing using the Illumina HTS platform (Yeo et al., 2009), we developed computational approaches to analyze and integrate global binding data with functional information such as splicing changes measured by RNA-seq or arrays upon depletion of RBPs using RNAi or antisense oligonucleotide technology. We published the *first genome-wide RNA binding mapping study in PSCs* that verified that Rbfox2 indeed binds in vivo to these predicted binding sites, and was one of the first using CLIP-seq to show that *RBPs had position-dependent effects on alternative splicing* (Yeo et al.). In our explorations, we also showed that Rbfox2 was a “master splicing regulator” as it controlled other splicing factors and was **necessary for PSC survival but not other cell-types**, illustrating a **distinct cellular function for an RBP in PSCs**. In ongoing research we are validating other modes of RBFOX2 regulation of gene expression (see II) and studying RBFOX proteins in the brain (see below).

*LIN28-let7-IMP network*. The Lin28, Imp1, Imp3, Esrp1 and Esrp2 RBPs are highly expressed in PSCs.  Importantly, Lin28 is a reprogramming factor, raising my hypothesis that its mRNA targets will reveal networks that are key for pluripotency. We published the *first nucleotide-level RNA binding map of the pluripotency-associated RBP Lin28 and showed that LIN28 binds within GGAGA motifs in loop structures in mRNAs, reminiscent but distinct from its interaction with let-7 microRNA precursors* (Wilbert et al.).  In ongoing research, we are investigating the Imp1, Imp2 and Imp3 proteins, which are part of the regulatory circuit consisting of Lin28 and let-7 microRNAs. Using genome-wide binding assays, we found that IMP1, IMP2 and LIN28 bind to largely overlapping target genes. Importantly, when IMP1 levels are reduced, IMP1 targets such as cellular adhesion genes decrease, causing hESCs to detach and undergo apoptosis.  Thus we have unveiled a novel function for these proteins in PSCs (Conway*, Van Nostrand* et al, in preparation).  

### Normal and mutant functions of RBPs in the central nervous system <a name="neural-rbps"></a>

Defects in RNA regulation in the nervous system lead to neurodevelopmental dysfunction (e.g. autism) and neurodegenerative diseases (e.g. ALS). The mechanisms by which RBPs cause neurological disease are diverse, and in several cases the molecular details continue to remain elusive.

*RBFOX1, RBFOX2, RBFOX3.* Rbfox proteins interact with proteins mutated in spinal cerebellar ataxia and individuals with mutations mapping to the Rbfox1 gene locus have mental retardation, epilepsy and autism. Animal models with knockout or knockdown of Rbfox protein expression show extensive defects in neuronal physiology. **To test the hypothesis that alternative splicing targets of Rbfox proteins would reveal pathways important in autism**, we mapped the Rbfox 1 and 2 transcriptome-wide binding sites in mouse brains. We were excited to find that loci associated with autism spectrum disorders such as the Neurexins, Neuroligins and Shank genes contained both Rbfox sites nearby alternatively spliced exons but interestingly, also far away from any exons (LovcWe et al.). With further exploration, we found that similarly to exon-proximal sites, distal sites bound by Rbfox1 and Rbfox2 contain evolutionarily conserved GCAUG sequences and are associated with splicing regulation upon modulation of Rbfox abundance. We showed that a conserved long-range RNA-RNA base-pairing interaction (an “RNA bridge”) facilitates Rbfox-mediated exon inclusion in the ENAH (enabled homology) gene, demonstrating, *a fundamental RNA-mediated mechanism for AS control by distally bound RBPs* [(Lovci et al.)](/papers/2013/nsmb2699.pdf).

*ALS-associated RBPs*. A paradigm shift in the pathogenesis of Amyotrophic Lateral Sclerosis (ALS) occurred when mutations in RBPs, in particular Tar DNA-binding protein 43 (or TDP-43) and (fused in sarcoma) FUS/TLS, were found in patients with ALS. To understand the normal functions of TDP-43 and FUS/TLS in the central nervous system, in collaboration with Don Cleveland’s laboratory at UCSD, we generated *genome-wide RNA binding sites of TDP-43 in vivo* (Polymenidou et al., 2011). A year later, also in collaboration with Don’s lab, we published *genome-wide binding sites for FUS/TLS* (Lagier-Tourenne et al.).  Our results supported a common loss-of-function (gene expression and alternative splicing) pathway in the pathogenesis of TDP-43 and FUS/TLS misregulation.  In ongoing research in my lab, we are evaluating the role of TAF15 and hnRNP protein A2/B1, reported to cause multisystem proteinopathy and ALS (Kim et al.).


## New mechanistic views of RNA processing <a name="rna-processing"></a>

*Alternative splicing regulation by multiple RBPs*. In order for cells to maintain homeostasis, it is thought that multiple RBPs coordinately control RNA processing of individual transcripts. The specific hypothesis we sought to test was that multiple RBPs would coordinately control alternative splicing events in human cells. As a pilot experiment, we were interested in how members of the most abundantly expressed RBPs named heterogeneous ribonucleoparticle (hnRNP) proteins coordinately affect alternative splicing in human cells. We published the *first integrated genome-wide analyses of alternative splicing regulated by multiple RBPs and their binding sites in human cells* (Huelga et al.). Surprisingly, we showed that the hnRNPs had a high degree of cross- and auto-regulation, and basically attempted to compensate for each other’s absence.

To understand coordinated control it important to systematically evaluate what is the composition of RBP-RNA complexes? RBPs interact with shared RNA substrates to form RNP-complexes. Knowing the protein interactors of each RBP will enable us to attribute novel functions to known RBPs. In ongoing research, we performed **unbiased quantitative proteomics** to comprehensively identify proteins that interact with 10 hnRNPs, RBFOX2 and UPF1 proteins. We identified hundreds to thousands of interactors for each RBP, the majority of which RNA-dependent interactors. This protein-protein interaction data is a rich resource for identifying previously unknown linkages to cellular machineries, signaling pathways or subcellular structures.

And as part of the NIH-funded ENCODE efforts, my lab screened more than 700 commercially available antibodies against >500 RBPs for their ability to selectively immunoprecipitate the target protein.  We found antibodies that are effective against >250 RBPs where all this information is publicly available to the community. With these antibodies, my lab is in the process of generating a large RBP-RNA interactome dataset in the world to-date, consisting of 250 RBPs in two human cell-lines.  Our improvements in the cross-linking and immunoprecipitation (CLIP) protocol have enabled us to operate at this scale in a highly reproducible fashion, setting the standard for such analyses in the field.  

*Adenosine-to-inosine RNA editing* is mediated by RBPs named adenosine deaminase acting on RNA (ADARs). With the advent of high-throughput sequencing, RNA-seq datasets can be mined for evidence of RNA editing in tissues and cell-lines.  However, it is often difficult to distinguish A-to-I RNA edit sites in the transcriptome with sequencing errors or nucleotide variation in the genomes. We started a project to build a computational approach that takes as input RNA-seq data and predicts A-to-I sites.  At that point, several high-profile papers were published in genome-wide identification of A-to-I sites, rapidly followed by criticisms in the community about the treatment of these data bordering on being incorrect.  Taking a step back, we realized that many of these studies did not have the proper genetic control, which is to knockout the ADAR proteins thus any predicted A-to-I site in the ADAR knockout would be considered a false positive by the algorithm.  In a close collaboration with Prof. Hundley (Indiana University), we found that the non-catalytic ADR-2 in worms could still affect RNA editing in vivo by affecting the same substrates as ADR-1 (Washburn et al Cell Reports).

*RNA quality control* mechanisms are important for the removal of faulty RNAs.  In order to discriminate normal RNAs from ones destined for degradation, Suzanne Lee that is co-mentored with Prof. Lykke-Andersen (UCSD) led a study that demonstrated that the ATPase cycle of the SF1 helicase Upf1 is necessary for mRNA target discrimination. Gabriel Pratt and Fernando Martinez also contributed significantly to the study. Pratt performed all the bioinformatics analyzing the large CLIP-seq, RIP-seq and RNA-seq datasets generated by Fernando and Suzanne (Lee et al Molecular Cell).

*Repetitive elements in the genome* can interact with RBPs. In collaboration with Tim Behrens at Genentech, we found that the Ro60 RBP binds an RNA motif derived from endogenous Alu retroelements. Alu transcripts were found to be induced by type I interferon and stimulated pro-inflammatory cytokine secretion by human peripheral blood cells.  Importantly Ro60 deletion resulted in enhanced expression of Alu RNAs and interferon-regulated genes.  Tiffany Hung, a fellow at Genentech who led the study went on to show that anti-Ro60 positive systemic lupus erythematosus immune complexes contained Alu RNAs and Alu transcripts were enriched in SLE whole blood samples compared to control.  This exciting finding was recently published in the journal Science in 2015.


## Single cell views of RNA processing <a name="single-cell"></a>

Until recently, the overwhelming majority of biological conclusions about mechanisms of RNA processing and transcriptomic diversity are derived from bulk populations of cells or tissues.  However, the multitude of cell-types in heterogeneous mixtures in vivo and even in vitro during differentiation of PSCs, coupled with stochastic control of gene expression have been largely ignored. The transcriptomic composition of individual cells is lost in conventional sequencing projects, which typically analyze RNA extracted from pooled populations of cells and variations that specify individual cell-types are largely hidden in the bulk signal. Advances in the techniques for the isolation of single cells coupled with next-generation sequencing (NGS) devices have revealed new insights in specific “bimodal” gene expression patterns within a population of cells (Shalek et al., 2013), allele specific expression (Deng et al., 2014) and transcriptional programs in single cells from human and mouse embryos (Xue et al., 2013; Yan et al., 2013).

In ongoing research, my lab has developed novel experimental and computational analytical tools to isolate and analyze hundreds to thousands of individual cells. As part of our development and validation process for our tools, together with our collaborator John Chang (UCSD), we have analyzed ~5,000 single cells, each analyzed using qRT-PCR of ~90 genes to develop a fate map in cells, published recently in Nature Immunology (Arsenio et al.). My graduate student Boyko Kakaradov and Janilyn Arsenio, a talented postdoc in Chang’s lab co-led the work.

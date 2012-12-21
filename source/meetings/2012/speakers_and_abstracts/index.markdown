---
layout: page
title: "Speakers and Abstracts for Scientific Software Days 2012"
comments: true
sharing: true
footer: true
---

## <a id="abram"></a>My Monitor is Bigger than yours: Running Visualization with DisplayCluster on Tiled Arrays 

>  [Greg Abram](http://www.tacc.utexas.edu/staff/gregory-d.-abram) and [Greg Johnson](http://www.tacc.utexas.edu/staff/greg-p.-johnson)</a>  
> Texas Advanced Computing Center

<a href="http://mediasite.aces.utexas.edu/UTMediasite/Play/1a498563bf334e64a84d17faa1ffad6e1d?catalog=3ead8f01-e8c2-4985-ac58-8646be39c432" ><img src="{{ root_url }}/images/1356069297_Video.png" /></a>  

[DisplayCluster](https://github.com/TACC/DisplayCluster) is a software
environment for interactively driving large-scale tiled displays. The software
allows users to interactively view media such as high-resolution imagery and
video, as well as stream content from remote sources such as laptops / desktops
or high-performance remote visualization machines. Many users can
simultaneously interact with DisplayCluster with devices such as joysticks or
touch-enabled devices such as the iPhone / iPad / iTouch or Android
devices. Additionally, a Python scripting interface is provided to automate
interaction with DisplayCluster.  


##  <a id="demeler"></a>Biophysics and HPC: The UltraScan XSEDE Science Gateway

> [Borries Demeler](http://www.demeler.uthscsa.edu/)  
> UT Health Science Center San Antonio

<a href="http://mediasite.aces.utexas.edu/UTMediasite/Play/b35b0a7e2f5246a09970d3addd0879d91d?catalog=3ead8f01-e8c2-4985-ac58-8646be39c432" ><img src="{{ root_url }}/images/1356069297_Video.png" /></a> <a href="{{ root_url }}/meetings/2012/speakers_and_abstracts/bdemeler_ssd2012.pdf" ><img src="{{ root_url }}/images/1356069234_Slides.png" /></a>  

[UltraScan](http://www.ultrascan.uthscsa.edu) is a software package for the analysis of biophysical data from experiments investigating solution properties of macromolecules. This presentation will discuss the analysis workflow used to solve a complex computational problem. We describe the UltraScan-3 XSEDE Gateway, which provides a unique analysis environment that  combines multiple tools and layers, including MySQL databases, the XSEDE HPC infrastructure, multi-platform GUI software, a PHP-based LIMS web frontend, and the Apache Airavata Generic Factory (GFAC) into a powerful analysis toolchain. Together, these components provide an easy-to-learn and user-friendly, yet very flexible analysis environment for remote HPC analysis and large data management.

## <a id="james"></a>Having It Both Ways: Eclipse PTP on Desktop and Cluster

> [Doug James](http://www.tacc.utexas.edu/staff/doug-james)  
> Texas Advanced Computing Center

<a href="http://mediasite.aces.utexas.edu/UTMediasite/Play/a7c998484a97403b88effcb2df460f311d?catalog=3ead8f01-e8c2-4985-ac58-8646be39c432" ><img src="{{ root_url }}/images/1356069297_Video.png" /></a> <a href="{{ root_url }}/meetings/2012/speakers_and_abstracts/djames_ssd2012.pdf" ><img src="{{ root_url }}/images/1356069234_Slides.png" /></a>    

This is an overview of [Eclipse PTP](www.eclipse.org/ptp), a robust, open source, multi-platform Integrated Development Environment (IDE) supporting the development of parallel applications in C, C++, and Fortran.  PTP also delivers customized, tight integration with XSEDE (including TACC's) clusters. Developers can use PTP on their desktops to develop, build, debug, manage, submit and monitor remote jobs on XSEDE resources; they can also create "synchronized projects" that reside on both their desktops and remote clusters. Eclipse PTP offers a promising path for improving both code quality and developer productivity; the presenter hopes to increase its visibility and promote its use.


## <a id="koesterke"></a>Bring on the Stampede: Coding with the Xeon Phi

> [Lars Koesterke](http://www.tacc.utexas.edu/staff/lars-koesterke)  
> Texas Advanced Computing Center

<a href="http://mediasite.aces.utexas.edu/UTMediasite/Play/644b2b36ad9c4e7eb4d33658af862cc01d?catalog=3ead8f01-e8c2-4985-ac58-8646be39c432" ><img src="{{ root_url }}/images/1356069297_Video.png" /></a> <a href="{{ root_url }}/meetings/2012/speakers_and_abstracts/lkoesterke_ssd2012.pdf" ><img src="{{ root_url }}/images/1356069234_Slides.png" /></a>    

In January of 2013, TACC will deploy Stampede, the first large-scale cluster
deployment to include Intel Xeon Phi (MIC) co-processors. The Xeon Phi is a
highly parallel architecture combining many x86 cores into a single chip.
Leveraging the standard Intel Xeon technology, developers are able to program
the Xeon Phi using standard threading models.  This highly-parallel processor
architecture with a portable threading model promises substantial performance
gains for highly-parallel computing workloads. In this presentation, we discuss
porting computationally intensive algorithms, scaling to large numbers of
threads and cores, and using Stampede and the Intel Xeon Phi.

## <a id="mclay"></a>Reading/Writing Large Parallel Files without upsetting Supercomputer Administrators

> [Robert McLay](http://www.tacc.utexas.edu/staff/robert-mclay)  
> Texas Advanced Computing Center

<a href="http://mediasite.aces.utexas.edu/UTMediasite/Play/877df0af98a64d258278717dbfda3a541d?catalog=3ead8f01-e8c2-4985-ac58-8646be39c432" ><img src="{{ root_url }}/images/1356069297_Video.png" /></a>  

Large parallel filesystem are magical.  They are a collection of
computers and disks that act as if they are one very large disk.
However the magic only goes so far and they are somewhat fragile.
This talk will explain what issues are and how to avoid the pitfalls.
As an example this talk will show that it is possible to write single
large files efficiently in parallel.


## <a id="oliphant"></a>Fortran speed in Python: Numba the Python LLVM Compiler

<a href="http://mediasite.aces.utexas.edu/UTMediasite/Play/1a498563bf334e64a84d17faa1ffad6e1d?catalog=3ead8f01-e8c2-4985-ac58-8646be39c432" ><img src="{{ root_url }}/images/1356069297_Video.png" /></a>  

> [Travis Oliphant](http://www.continuum.io/our-team.html#travis)  
> Continuum Analytics, Inc

[Numba](https://github.com/numba/numba) and [NumbaPro](https://store.continuum.io/cshop/numbapro) is a Python bytecode to LLVM translator that allows creation of fast, machine code from Python functions. The Low Level Virtual Machine (LLVM) project is rapidly becoming a hardware-industry standard for the intermediate representation (IR) of compiled codes. Numba's high-level translator to the LLVM IR provides Python the ability to take advantage of the machine code generated by the hardware manufacturers contributions to LLVM. Numba translates a Python function comprised of a subset of Python syntax to machine code using simple type inference and the creation of multiple machine-code versions. In this talk, I will describe the design of Numba, illustrate its applications to multiple domains and discuss the enhancements to NumPy and SciPy that can benefit from this tool.

## <a id="pawlik"></a>Everything about scientific software documentation that wasn't in the manual

> [Aleksandra Pawlik](http://users.mct.open.ac.uk/anp58/)  
> Open University

<a href="http://mediasite.aces.utexas.edu/UTMediasite/Play/8cd241f4964441e08b0d6f1824e0fdbd1d?catalog=3ead8f01-e8c2-4985-ac58-8646be39c432" ><img src="{{ root_url }}/images/1356069297_Video.png" /></a> <a href="{{ root_url }}/meetings/2012/speakers_and_abstracts/SciSoftDays-Pawlik2012.pdf" ><img src="{{ root_url }}/images/1356069234_Slides.png" /></a>    

How does documentation fit into different contexts of scientific software development? The answer is different for end-user developers and in the case of software used by a wider scientific community. The talk will examine these scenarios and will look in detail at the SciPy Documentation Project, to illustrate how documentation can be crowdsourced in scientific software development. This will lead us to consider how crowdsourcing documentation relates to open source software development and community building.

## <a id="poole"></a>Data Processing for the NASA GRACE Mission

> Peter Nagel and [Steve Poole](http://www.csr.utexas.edu/info/staff/poole.html)  
> Center for Space Research, UT Austin

<a href="http://mediasite.aces.utexas.edu/UTMediasite/Play/49212cd152f347d88befa962c0a6cadf1d?catalog=3ead8f01-e8c2-4985-ac58-8646be39c432" ><img src="{{ root_url }}/images/1356069297_Video.png" /></a> <a href="{{ root_url }}/meetings/2012/speakers_and_abstracts/spoole_ssd2012.pdf" ><img src="{{ root_url }}/images/1356069234_Slides.png" /></a>    

The NASA GRACE satellite mission obtains a set of global high-resolution
gravity measurements which are used to solve for an Earth gravity model every
month.  The procedures used to create this monthly gravity model will be
discussed, including the challenges involved in getting large amounts of data
ready for processing, keeping large data files on-line during the processing,
condensing the data into manageable-size files for use in creating multi-year
mean gravity models, and archiving the results.  The software used to solve for
the gravity model, the Advanced Equation Solver for Parallel Systems (Aesop),
will be discussed.

## <a id="schroeder"></a> Scaling the Future: How to Practice Open Science

> [Will Schroeder](http://www.kitware.com/company/team/schroeder.html)  
>  Kitware, Inc.

<a href="http://mediasite.aces.utexas.edu/UTMediasite/Play/061708aa9c4f41f883a9363309ae95301d?catalog=3ead8f01-e8c2-4985-ac58-8646be39c432" ><img src="{{ root_url }}/images/1356069297_Video.png" /></a> <a href="{{ root_url }}/meetings/2012/speakers_and_abstracts/Schroeder-TACC-2012.pdf" ><img src="{{ root_url }}/images/1356069234_Slides.png" /></a>    

The growing complexity and scale of research demands that we embrace new methods if we are to support future scientific progress. These methods must be based on the three pillars of Open Science: Open Access, Open Data, and Open Source. This presentation describes some practical means to practice open science, with examples from analytics, computational chemistry, big data, medical computing, video analysis, and visualization. 


## <a id="terrel"></a>Sharing is Caring: NumFOCUS and Open Scientific Code Initiative

> [Andy R. Terrel](andy.terrel.us)  
> Texas Advanced Computing Center

<a href="http://mediasite.aces.utexas.edu/UTMediasite/Play/2b1aac0da459437eb4faf0fd3f8715391d?catalog=3ead8f01-e8c2-4985-ac58-8646be39c432" ><img src="{{ root_url }}/images/1356069297_Video.png" /></a> <a href="{{ root_url }}/meetings/2012/speakers_and_abstracts/aterrel_scisoft2012.pdf" ><img src="{{ root_url }}/images/1356069234_Slides.png" /></a>    

Scientific software is complex, hard to install, and usually written by overworked indentured servants, i.e. graduate students.  Perhaps more importantly, it is the large basis of the modern scientific method, but unlike proofs and lab methodologies, it is often hidden from our peers. To address these issues, a number of initiatives to promote open scientific codes have emerged from various organizations.  I will focus on the [NumFOCUS](http://numfocus.org/) foundation, a new organization promoting the use of accessible and reproducible computing in science and technology.  I will also survey a number of other resources available for scientists to share their code and experiences.

## <a id="thiruvathukal"></a> Filesystems: Addressing the Last-mile "problem" in Services-Oriented/Cloud Computing

> [George K. Thiruvathukal](http://works.bepress.com/gkthiruvathukal/)  
> Loyola University

<a href="http://mediasite.aces.utexas.edu/UTMediasite/Play/a3a4eed80e504854a4b8f1c547de18981d?catalog=3ead8f01-e8c2-4985-ac58-8646be39c432" ><img src="{{ root_url }}/images/1356069297_Video.png" /></a> <a href="http://adhoc.thiruvathukal.com/ssd.2012/nofs.html#(1)" ><img src="{{ root_url }}/images/1356069234_Slides.png" /></a>    

## <a id="tobis"></a>Tex-MECS: Infrastructure for managing ensembles of computations

> [Michael Tobis](http://www.ig.utexas.edu/people/staff/tobis/)  
> University of Texas Institute for Geophysics

<a href="http://mediasite.aces.utexas.edu/UTMediasite/Play/1c24109975ae4d3c93871f2854cb98cb1d?catalog=3ead8f01-e8c2-4985-ac58-8646be39c432" ><img src="{{ root_url }}/images/1356069297_Video.png" /></a>  

## <a id="turk"></a> The yt Project: Growing and Engaging a Community of Practice

> [Matthew Turk](https://sites.google.com/site/matthewturk/)  
> Columbia University

<a href="http://mediasite.aces.utexas.edu/UTMediasite/Play/370d0f2f528340d29139808d71eefbbd1d?catalog=3ead8f01-e8c2-4985-ac58-8646be39c432" ><img src="{{ root_url }}/images/1356069297_Video.png" /></a> <a href="{{ root_url }}/meetings/2012/speakers_and_abstracts/mturk_scisoft2012_community.pdf" ><img src="{{ root_url }}/images/1356069234_Slides.png" /></a>    

In this talk, I will present on the [yt Project](http://yt-project.org/) an
analysis and visualization tool for astrophysical simulations.  I will provide
a brief motivation for its development, describe its capabilities for analysis
of astrophysical simulation data, and then describe the method by which the
community attempts to balance pragmatic, goal-driven development with best
practices in software development and high-performance computing.

Title: Scientific Software Days 2009
Slug: 2009_details
Category: workshops


The Texas Advanced Computing Center, the University of Texas Institute for Geophysics, and the University of Texas Bureau of Economic Geology are organizing the 2009 Scientific Software Days, where the scientific community can share experiences of developing software and learn about new developments in general scientific software.

## Schedule:

May 21: general lectures

9-9:30 Computational Biology at TACC. Michael Gonzales, Texas Advanced Computing Center 
> 
> TACC provides a number of advanced computing resources to serve the life science research community. This includes several large computational systems that enable the analysis of very large datasets and simulations of systems at biologically meaningful time scales. To enable utilization of these computational resources, a robust software stack is available for molecular dynamics simulations, genomic sequence assembly and analysis, protein-ligand interactions and statistical calculations. Dr. Michael B. Gonzales, Program Director for Computational Biology, will provide an introduction to these resources and activities for the life science community. 

9:30-10 libMesh: A Parallel Adaptive Finite Element Library. John Peterson, Texas Advanced Computing Center 
> 
> LibMesh is an open-source finite element library that was originally developed to facilitate serial and parallel simulation of multi scale, multi physics applications using adaptive mesh refinement and coarsening strategies. The library was created in the CFDLab at the  University of Texas’s Aerospace Engineering and Engineering Mechanics Department, but, as with other open-source software projects, contributions are being made elsewhere in the US and abroad. In this talk, which will be geared toward a general audience, we will describe the underlying philosophy and software design approach used in the library. We will give additional details on the adaptive mesh refinement and coarsening (AMR/C) schemes utilized, and finally, describe our implementations in the key areas of domain decomposition, message passing, and parallel mesh data structures. Other topics include: discussion of C++ programming paradigms (scientific software and the STL) software reusability in the face of diverse user applications, and integration with high-level threading APIs for making efficient use of hybrid parallel architectures. Finally, results from some of the various applications which utilize the library are presented, and areas of future research are discussed. 

10:15-10:45 Introduction to parallel debugging with DDT. Carlos Rosales, Texas Advanced Computing Center 
> 
> With the continuous trend to analyze larger and more complex problems using computational techniques and the increasing reliance on multicore platforms to execute scientific codes, the necessity for parallel debugging tools has become clear. This talk will give a guided introduction to parallel debugging using Allinea’s Distributed Debugger Tool (DDT). DDT allows for debugging and extensive memory checking over thousands of processors, and it is an example of the kind of tools that are becoming indispensable for building reliable large scale scientific codes. 

10:45-11:15 Use ssh, catch bullets between your teeth. Bill Barth, Texas Advanced Computing Center.

11:30-12:30 The impact of computational science on the scientific method (keynote). Victoria Stodden, Berkman Center for Internet and Society 
> 
> Computation has become a pervasive and transformative part of the modern scientific enterprise, sometimes even referred to as a new branch of the scientific method. Massive simulation and the search for subtle patterns in vast datasets are emblems of our age. Computation appears to have become a mode of discovery in itself, rather than merely a tool facilitating traditional empirical approaches to research. Additionally, an increasingly large proportion of scientific research is now digitized, and coupled with scientists’ near ubiquitous use of the Internet, transparency in computational science seems all but inevitable. But, with several important exceptions, scientists are not availing themselves of this opportunity to communicate not only their results but also their complete methods, often expressed through the code and data. In short, computational science today typically is not reproducible and we are missing a crucial opportunity to control for error through verification, a central motivation of the  scientific method. In this talk I explore these two changes to the scientific method and present  possible ways to bring reproducibility into today’s scientific endeavor. I propose a licensing structure for all components of the research, called the “Reproducible Research Standard,” designed to align Intellectual Property law with longstanding communitarian scientific norms, and outline the need for software tools that can facilitate attribution tracking, data and code sharing, research verification, and thus encourage scientists to release their full research compendium and re-establish reproducibility as core component of modern computational science. 

lunch break

1:30-2:00 Parallel programming in Fortress. Eric Allen, SunLabs 
> 
> Fortress is a new programming language designed for high-performance computing (HPC) with high programmability. In order to explore breakaway approaches to improving programmability, the Fortress design has not been tied to legacy language syntax or semantics; all aspects of HPC language design have been rethought from the ground up. As a result, we are able to support features in Fortress such as transactions, specification of locality, and implicit parallel computation, as integral features built into the core of the language. In this talk I will give a brief overview of the key features of Fortress relevant to parallel programming and provide examples of programs currently using these features.

2:00-2:30 Scientific computing at BP. Phuong Vu, BP 
> 
> In this talk I will give a short introduction to DDS, BP internal seismic software infrastructure, give some example of pseudo implementation of seismic imaging application, and discuss some of the IO issues I encounter in the development of application using DDS.

2:45-3:15 Computational Application Development with Python Steve Lang 
> 
> This presentation is for software developers who are considering adopting Python for their computational application development. Python is an excellent scripting language for prototyping. However, a limiting factor in using Python is the quality and breadth of analytics support. With the recent release of PyIMSL™ Studio one can access a comprehensive set of seasoned mathematical and statistical algorithms to create prototype models of Python based analytical applications. When required to migrate the Python models to a production version, the same algorithm coverage is available, whether through Python or converting the algorithms to a native language such as C/C++, Java, C# or Fortran for more flexibility. This presentation will provide an overview of PyIMSL Studio, the only commercially-available numerical analysis development environment which brings together how fully supported and documented Python tools and the analytics in the IMSL® C Numerical Library for developing computational applications. Examples of IMSL use within Python and C will be shown.

3:15-3:45 Automated Code Analysis and Transformation tools to Support Scientific Computing Ira Baxter 
> 
> Modeling complex physical phenomena requires complex codes. Building such complex codes is difficult, and often takes many engineers and years to construct and validate. Software Engineering tools can help this process, shortening cycle times and raising quality. This talk will cover the general concept of a highly customizable program transformation system, and several possible applications to large codes. In particular, we will examine searching large source code bases, and finding duplicated code using large FORTRAN codes as examples. We will also briefly examine parallel code generation from C++.

3:45-4:15 Efficient Parallel Fourier Transform Using Non-blocking Collective Communications and Its Application to Seismic Modeling and Imaging Chunlei Chu, Paul L. Stoffa and Roustam Seif, Institute for Geophysics, The University of Texas at Austin 
> 
> Fast Fourier transforms lie at the heart of many scientific computations. Parallelizations of the fast Fourier transforms have been implemented on different architectures and are commonly employed in a wide spectrum of applications. The implementation of the fast Fourier transforms on distributed memory systems requires global matrix transposition operations which can be realized by an all-to-all type communication in MPI, i.e. MPI_Alltoall or MPI_Alltoallv. We observe that this all-to-all communication becomes a major performance bottleneck for large scale problems, especially when using many processors. To reduce this communication cost, we use the non-blocking collective communication library LibNBC to optimize the parallel fast Fourier transform by overlapping communication with computation and apply it to the pseudo spectral seismic wave simulations and earth imaging. The benchmarking results on Ranger show that the communication-computation overlapping strategies we proposed can successfully conceal a large amount of communication overhead. As a result, a performance improvement of up to 40% is observed by simply changing blocking all-to-all communication calls to non-blocking ones, which demonstrates the promising potential of using non-blocking collective communications for large scale parallel Fourier transforms on clusters. 

Day 2 (May 22): tutorials

Two half-day tutorials will be offered, that will teach you in-depth about various software packages. The tutorials include hands-on lab sessions.

Scientific Data Management: version control and storage. Karl Schulz, Texas Advanced Computing Center 
> 
> In this tutorial you will learn the basics of the version control systems cvs and svn, and the scientific data libraries NetCDF and Silo. CVS and svn are version control systems, (also known as revision control, source control or (source) code management (SCM)) for the management of changes to documents, programs, and other information stored as computer files. They are most commonly used in software development, where a team of people may be changing the same files, but they also serve to have access to previous versions of files. 
> 
> NetCDF (network Common Data Form) is a set of interfaces for array-oriented data access and a freely-distributed collection of data access libraries for C, Fortran, C++, Java, and other languages. The netCDF libraries support a machine-independent format for representing scientific data. Together, the interfaces, libraries, and format support the creation, access, and sharing of scientific data. 
> 
> Silo is a library for reading and writing a wide variety of scientific data to binary, disk files. The files Silo produces and the data within them can be easily shared and exchanged between wholly independently developed applications running on disparate computing platforms 

Introduction to PETSc. Dr. Matthew G. Knepley, Argonne National Laboratory, Chicago, IL. 
> 
> The Portable, Extensible Toolkit for Scientific Computation (PETSc) provides a framework for development of computational science codes. Although scalability and high performance are crucial for scientific applications, the usability often turns upon other software factors, such as version control, modular design, and extensibility. We will discuss each of these issues in the context of PETSc development. Moreover, we will present examples of PDE solvers developed in PETSc with advanced capabilities, such as unstructured meshes, multigrid, and parallel sparse direct solvers. This course should enable a researcher to independently develop usable, scalable, extensible code with PETSc. Attendees are encouraged to bring a laptop as installation help will be provided. 
> 
> The course will cover: 
> Design of large scale simulations 
> Solution of linear and nonlinear algebraic systems 
> Debugging, profiling, and management of scientific code 
> Structured and unstructured meshes 
> Example problems in PETSc 
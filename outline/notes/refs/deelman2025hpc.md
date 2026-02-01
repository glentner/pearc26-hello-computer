---
bibkey: "deelman2025hpc"
title: "High-performance computing at a crossroads"
authors: "Ewa Deelman, Jack Dongarra, Bruce Hendrickson, Amanda Randles, Daniel Reed, Edward Seidel, Katherine Yelick"
year: 2025
source_type: "paper"
url: "https://doi.org/10.1126/science.adu0801"
journal: "Science"
volume: 387
issue: 6736
pages: "829-831"
doi: "10.1126/science.adu0801"
pub_date: "2025-02-21"
status: "complete"
key_findings:
  - "HPC has enabled considerable advances over four decades but faces critical bottlenecks in data handling, algorithm efficiency, and architectural scalability"
  - "AI integration is intensifying demands on HPC systems while introducing new computational requirements—particularly tension between double-precision scientific needs and lower-precision AI workloads"
  - "The US lacks a comprehensive long-term strategy for HPC unlike coordinated national programs in Europe (EuroHPC), Japan (Fugaku), and China"
  - "Energy consumption and power efficiency have become paramount challenges as systems scale"
  - "Authors call for reimagining the entire HPC ecosystem from hardware through software stack to applications"
sample_sentences: |
  A 2025 Science Policy Forum featuring prominent HPC leaders from national labs 
  and major research universities warned that HPC stands at a crossroads, facing 
  mounting technical challenges in energy consumption and architectural scalability 
  while simultaneously being transformed by the computational demands of AI. The 
  authors call for a comprehensive national strategy to ensure HPC continues to 
  power scientific discovery in the AI era.
quotable:
  - "We need to reimagine how the HPC ecosystem should look from the hardware level, through the software stack, the connections to distributed computing resources, and all the way up to applications in science, engineering and manufacturing"
  - "HPC faces bottlenecks in data handling, algorithm efficiency, and the scalability of new architectures"
---

# High-performance computing at a crossroads

## Overview

This Science Policy Forum, published February 21, 2025, represents an authoritative
call-to-action from some of the most prominent figures in high-performance computing.
The author list reads like a who's who of HPC leadership: Ewa Deelman (USC Information
Sciences Institute, Pegasus workflow system creator), Jack Dongarra (University of
Tennessee, Oak Ridge National Lab, Turing Award recipient for high-performance computing
contributions), Bruce Hendrickson (Lawrence Livermore National Lab Computing Directorate),
Amanda Randles (Duke University), Daniel Reed (University of Utah), Edward Seidel
(University of Wyoming president, DOE advisory committees), and Katherine Yelick
(UC Berkeley, former NERSC director).

The paper argues that HPC is at a pivotal moment—having powered four decades of
scientific discovery but now facing an inflection point driven by AI integration,
energy constraints, and geopolitical competition.

## Core Arguments

### Four Decades of Impact

The authors begin by establishing HPC's track record: enabling "considerable advances
in scientific discovery and engineering, spurring technological development across
the globe." This ranges from weather forecasting and climate modeling to drug discovery,
molecular simulations, cryptography, and aircraft design.

### Mounting Technical Challenges

However, the paper identifies critical bottlenecks:

1. **Data handling**: Modern scientific workflows generate and consume petabytes of
   data, straining storage and I/O systems
2. **Algorithm efficiency**: Traditional methods may no longer suffice for increasingly
   complex scientific models
3. **Architectural scalability**: New architectures introduce complexity in ensuring
   seamless data flow and efficient parallel processing
4. **Energy consumption**: As machines become more powerful, their energy requirements
   escalate correspondingly—balancing computational performance with energy efficiency
   is now paramount

### The AI Tension

A central tension emerges from AI's rise. The paper notes that AI has intensified
demands on HPC systems while introducing fundamentally different computational
requirements. Most critically:

- **Precision mismatch**: HPC has relied on 64-bit double-precision floating point
  calculations for scientific fidelity, but AI workloads (especially inference)
  gravitate toward lower precision (32-bit, 16-bit, or even lower)
- **Market forces**: Chip manufacturers increasingly optimize for AI workloads,
  potentially leaving traditional HPC needs behind
- **Diverging trajectories**: As one HPC analyst put it, "the technologies and
  configurations that serve AI drift farther away from what scientific computing needs"

The authors advocate for reconciling these needs rather than allowing them to diverge,
but acknowledge the commercial pressures pushing in the opposite direction.

### Geopolitical Competition

The paper situates HPC within global technological competition:

- **Europe**: The EuroHPC initiative is building some of the world's fastest
  supercomputers across multiple member nations through coordinated investment
- **Japan**: Developed Fugaku through a carefully planned national program
- **China**: Rapidly advancing domestic HPC capabilities despite export restrictions

In contrast, the US lacks a comprehensive long-term strategy. While DOE and NSF
fund major systems, the authors argue for a more coordinated, multiagency approach
with sustained commitment.

### The Reimagining Call

The paper's central recommendation is comprehensive: "We need to reimagine how the
HPC ecosystem should look from the hardware level, through the software stack, the
connections to distributed computing resources, and all the way up to applications
in science, engineering and manufacturing."

This includes:
- Technical innovations in hardware and software
- Workforce development and education
- International collaboration on shared challenges
- National policies and sustained funding commitment

## Authors and Affiliations

The authorship represents the HPC research leadership:

| Author | Primary Affiliation |
|--------|---------------------|
| Ewa Deelman | USC Information Sciences Institute |
| Jack Dongarra | UT Knoxville, ORNL, U Manchester |
| Bruce Hendrickson | LLNL Computing Directorate |
| Amanda Randles | Duke University BME |
| Daniel Reed | U Utah Scientific Computing |
| Edward Seidel | University of Wyoming |
| Katherine Yelick | UC Berkeley EECS |

Several serve on DOE advisory committees, establishing direct policy relevance.

## Reception and Impact

The paper prompted substantial coverage and response:

- University of Wyoming issued a press release highlighting President Seidel's
  involvement and the call for national strategy
- Secondary analyses discussed the "fourth wave" of scientific inquiry—cognition
  through AI integration
- Research community referenced the paper in subsequent work on AI for HPC software
  development

A notable comment in Science described the synergy among HPC, Big Data, and AI as
potentially "as powerful a metaphor for spawning new waves of discoveries and innovation
as were the telescope and microscope in the 16th century."

## Relevance to Our Paper

This reference is essential for several reasons:

1. **Authoritative HPC voice**: The author list carries enormous credibility within
   the HPC community—if anyone can speak to HPC's state and trajectory, it's this group

2. **Perfect timing**: Published February 2025, this captures the exact moment our
   paper addresses—when the HPC community is grappling with how AI changes everything

3. **Frames the tension**: The paper articulates the precision/architecture tension
   between traditional HPC and AI workloads that our agentic tools operate within

4. **Policy context**: Establishes that HPC+AI integration is not just a technical
   issue but a matter of national strategy and international competition

5. **Ecosystem thinking**: The call to reimagine "from hardware through software
   stack to applications" aligns with our focus on the developer experience layer

For our Background section, this paper provides the authoritative HPC community
perspective that complements the AI industry developments we trace. It answers
the question: How is the HPC community itself responding to the AI transformation?

## Citation

```bibtex
@article{deelman2025hpc,
  author    = {Deelman, Ewa and Dongarra, Jack and Hendrickson, Bruce and 
               Randles, Amanda and Reed, Daniel and Seidel, Edward and 
               Yelick, Katherine},
  title     = {High-performance computing at a crossroads},
  journal   = {Science},
  volume    = {387},
  number    = {6736},
  pages     = {829--831},
  year      = {2025},
  doi       = {10.1126/science.adu0801},
  url       = {https://www.science.org/doi/10.1126/science.adu0801}
}
```

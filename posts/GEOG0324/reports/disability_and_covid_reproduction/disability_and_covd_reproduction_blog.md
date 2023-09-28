---
title: "Disability and COVID-19 Reproduction Blog"
excerpt_separator: "<!--more-->"
author: Madeleine Gallop
date: '2023-09-28'
image: covid_reproduction.png
description: "The purpose of this blog is to reanalyze Chakraborty (2021) and finalize a reproduction report."
categories:
  - blog
  - Open Source GIScience
format: html
---

# Disability and COVID-19 Reproduction Blog

## Step one: identification of errors and plan for modification

The following report will plan and implement revisions to the reproduction of Chakraborty's 2021 study, _Social Inequities in the distribution of COVID-19: An Intra-Catagorial Analysis of People with Disabilities in the U.S._ 
This study was reproduced by Joseph Holler, Junyi Zhou, Peter Kedron, Drew An-Pham, Derrick Burt, and I, Madeleine Gallop, will be implementing revisions to their work. 

In this report, I will be making six primary revisions:

1. The final choropleth map, depicting each county's weight in the GEE model has a mistaken parameter causing it to only use half of the available orange color ramp. I plan to modfiy the code for this map to fix the color ramp. 
2. The "rational for the updated report" section should, and currently does not, occur at the end of the reproduction study. I will move this section to the proper area. 
3. Emily's discussion should be integrated into the existing discussion section. I will combine these two sections as I see fit. 
4. There is not a seperate conclusions section that concludes whether the reproduction attempt was successful, and waht the implications are for how the original study contributes to scientific knowledge. I will add this section, as it will help the audience understand the contributions of the original study to scientific knowledge. 
5. The horizontal orientation of the missing data table with Kable and/or KableExtra functions should be improved. I will fix the orientation of this table. 
6. There are certain ways the efficiency of the study could be improved, such as writing a general purpose function createMap that can be reused throughout the study. Hopefully encapsulating certain code blocks in a function will imrove the efficiency or elegancy of the code. 

In order to visualize and compare results, I plan to include before and after pictures of any visual changes, or orally describe the difference brought about by my revisions. I will include before and after screenshots of code blocks I modify, and write about any changes I make. 


## Step two: write
- modify the analysis plan to address the issue identified above

map: removed the     #midpoint = 0 parameter

## Step three: implement
- implement the change in code

## Step four: interpret
- interpret the results of your change(s) in the rmarkdown report

## Step five: write
- write a blog post highlighting what you have learned from and contributed to with this reproduction and reanalysis study. In particular, please address these questions:
    - Has the reproduction deviated from the original study in any way?
    - If so, are the deviations improvements or errors?
    - Are there opportunities to further improve the study’s research design, reproducibility, or reproducibility for teaching purposes?
    - Are there opportunities to design meaningful replication studies to further test any theories established by this study?
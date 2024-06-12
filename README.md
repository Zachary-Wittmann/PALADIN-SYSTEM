# PALADIN System &nbsp;&nbsp;[![Static Badge](https://img.shields.io/badge/license-Open_Data_Commons-blue)](https://opendatacommons.org/licenses/dbcl/1-0/)

The **P**redictive **A**nalytics-driven **L**aw **A**nd **D**ispatch **I**ntelligence **N**etwork or PALADIN System was created by ***Atlas Development*** during the ***Smart-Borderland AI Hackathon***
at the ***University of Texas at El Paso*** and was awarded 3<sup>rd</sup> place. This program aimed to analyze incident reports and determine where hotspots would appear in order to allow for better optimized
patrol routes.


## Table of Contents.

1. [Team Composition \[Atlas Development\]](#team-composition-atlas-development)
2. [Dataset Information](#dataset-information)
3. [Dataset Overview](#dataset-overview)
4. [Project Contents](#project-contents)
5. [Sample Datasets](#sample-datasets)
6. [Closing Thoughts](#closing-thoughts)

## Team Composition [Atlas Development]
**This Project was completed with the hard work of its members!**

[William Dunlap](https://github.com/unit098 "William's GitHub") - *Code Assistant/Presentation Assistant*: Assisted with any areas in the code or presentation that required an extra set of hands.

[Dante Lopez](https://github.com/dragons6612 "Dante's GitHub") - *Severity Creator/Presentation Assistant*: Created the Severity.csv and assisted in the creation of the presentation

[Jesus Torres](https://github.com/jatorresdom "Jesus's GitHub") - *Main Code Lead*: Handled the majority of the coding process and utilization of Google API.

[Zachary Wittmann](https://github.com/Zachary-Wittmann "Zachary's GitHub") - *Presentation Creator/Code Assistant*: Created the PowerPoint presentation and assisted in approaches for the coding.

<p align="center">
<img src="https://github.com/Zachary-Wittmann/Hackathons/blob/main/PALADIN%20SYSTEM/ReadMeAssets/Atlas_Development_Smart_Borderland_3rd_Place-1.png" height="400px"> 
</p>

## Dataset Information
Diggernaut. (2018, March). El Paso County Sheriff Blotter, Version 1.
Retrieved March, 22<sup>nd</sup> 2024 from https://www.kaggle.com/datasets/diggernaut/el-paso-county-sheriff-blotter/version/1.

## Dataset Overview
+ The dataset is taken from **kaggle** and contains information about **incident reports from the El Paso County Sheriff Office** in Colorado.
+ The *originalData.csv* file provided a lot of information that we had trimmed down to allow for practical use over the hackathon. Although some
  of the information trimmed could likely have improved the overall usefulness of the system for finding hotspots.

## Sample Datasets
__*originalData.csv*__
|incident>>address          |incident>>call_number|incident>>date|incident>>disposition|incident>>grid|incident>>problem    |incident>>time|
|---------------------------|---------------------|--------------|---------------------|--------------|---------------------|--------------|
|9385 Hardin Rd BLACK FOREST|2018-00048237        |3/16/2018     |No Info              |2103          |Alarm Residential    |6:44am        |
|9199 Ute Rd CHIPITA PARK   |2018-00048224        |3/16/2018     |No Info              |8501          |911 Hangup - Phase II|6:24am        |
|990 Glenrock Dr HWY 115    |2018-00048223        |3/16/2018     |No Info              |7304          |Alarm Residential    |6:22am        |
|Address Blocked            |2018-00048222        |3/16/2018     |Case Report          |3010          |Check the Welfare    |6:21am        |
|Address Blocked            |2018-00048219        |3/16/2018     |No Info              |7302          |Follow Up            |6:10am        |
***
__*Severity.csv*__
|incident>>problem          |Severity     |
|---------------------------|-------------|
|Hazard                     |0.2          |
|Reckless Endangerment      |0.6          |
|Drunk Person               |0.6          |
|Traffic Accident With Injury|0.7          |
|Criminal Trespass Auto Cold|0.5          |
***

## Project Contents

| Filename | Type | Description | 
| --------------- | --------------- | --------------- |
| ReadMeAssets | 🗂️ | Contains assets to make this README. |
| data | 🗂️ | Contains all the .csv files utilized within PALADIN. |
| PALADIN | .py | The source code for the project.|
| README | .md | All of the text that you are currently reading. |
| Team 3 | .pptx | The PowerPoint presentation for the project. |

## Closing Thoughts
> "I really enjoyed my first time working with an A.I. model."<br>- William Dunlap


> "N/A"<br>- Dante Lopez


> "This hackathon teached me a lot when approaching a prompt that may be guided for community outreach or community impact. In this case it was in our own community.
  It was eye opening to really consider all the possible options and develp skills to correctly research all available data or resources which can minimize the development
  and get to a better articulated solution."<br>- Jesus Torres


> "I found this experience to be very beneficial as I have an interest in data analytics and the utilization of machine learning and artificial intelligence in the process.
  I especially enjoyed working on a project that I feel would be beneficial to many individuals."<br>- Zachary Wittmann

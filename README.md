# Singing-AI-Bach

This repo contains all aspects of my Honors Senior Thesis project - showing what happens when you attempt to sing AI generated Bach chorales. It is important to me that my research is open and transparent throughout the entire process. You will see live changes/updates to this repository frequently as I continue to make progress on this project.

The repo contains all the resources needed when creating this project, including the following:

* **`project-docs`:** Files related to overall structure and timeline of the project as well as my synopsis of my project.
* **`research-docs`:** All the papers and textbooks that I've been reading for research on this project. Papers are sorted by CS papers and Bach papers. 
* **`papers` (in progress):** any final papers that I write for the project. This includes my final academic paper as well as a script and performance booklet that I would use for my final talk.
* **`datasets`:** Any datasets that were used in the research papers. Will likely do some data analysis on these datasets, including the code for parsing datasets having weird file formats.
* **`ai-music`:** AI generated Bach chorales (including original score) for each Bach chorale that I choose to generate.
* **`scripts`:** any test scripts or Python code that I used to help make my life easier in the project.
* **`models`:** The AI models I am using in my research, linked as *GitHub submodules*. This means that you can relink to the GitHub repository from where I pulled the models.

Additionally, `progress-log.md` lists my updates, challenges, bugs, etc. working on this project throughout the semester.

My faculty advisor for this project is [Dr. Meg Stohlmann](https://www.gonzaga.edu/college-of-arts-sciences/faculty-listing/detail/stohlmann), director of choirs at Gonzaga University.


## HELPFUL LINKS AND COMMANDS

Ability to use Magenta (for now):

```
docker run -it -p 6006:6006 -v /tmp/magenta:/magenta-data tensorflow/magenta
```

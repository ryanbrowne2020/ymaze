# Y-maze Triads

Please cite this script if you use it as: 

`Ryan Browne, Y-Maze Triads, https://github.com/ryanbrowne2020/ymaze, (Access Year)`
Thank you!

Simple analysis for mouse behavioural experiment Y-maze: get the number of triads
(spontaneous alteration test).

This file assumes you watched a recorded video of a Y-maze trial, and entered the mouse arm entries
as a string of numbers in a Word document, with the arms labelled as 1, 2, 3. 
You can add several trials in the same document, just put each trial on a new line. 

Note: you only need the t.pop() command if your lines have a line break / newline character at the end. 

Run as 
`python get_triads.py`

This will count the number of unique triads. 
For example, 12311121 will count as one triad, as the mouse entered three unique arms: 1[231]1121

12132121231 will count as 1[2[1[3]2]1]2[1[23]1] as 5 triads, as the mouse entered three consecutive different arms 5 times
(this approach moves through each entry, and looks at if the previous and next entries are different arms, then adds 1 score).

The definition of uniique triads was taken from:

> The following dependent variables were registered: total number of arm entries, number of triads (sequence of three consecutive visits to different arms), and percentage of alternation. An alternation was defined as an entry into three different arms on consecutive choices. The percentage of alternation was calculated as the ratio of actual to maximum number of alternations. The maximum number of possible alternations was defined as the total number of arm entries minus 2.

(Galeano P, Martino Adami PV, Do Carmo S, Blanco E, Rotondaro C, Capani F, Castaño EM, Cuello AC, Morelli L. Longitudinal analysis of the behavioral phenotype in a novel transgenic rat model of early stages of Alzheimer's disease. Front Behav Neurosci. 2014 Sep 16;8:321. doi: 10.3389/fnbeh.2014.00321. )

Note: this script just prints to the terminal. You could modify it to output to a tsv file for statistical analysis, and so on. 

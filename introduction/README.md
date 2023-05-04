The presentation and explanation in this folder are rendered with [`quarto`](https://quarto.org/).

The source files, `fisher-explanation.qmd` and `fisher-presentation.qmd`, are 
human-readable markdown with embedded scripts to generate the figures.

In order to generate the html explanation, after installing quarto run:

`quarto render fisher-explanation.qmd`

This will run all the embedded scripts.
Or render it to pdf:

`quarto render fisher-explanation.qmd --to pdf`

Similarly, render the presentation with:

`quarto render fisher-presentation.qmd`
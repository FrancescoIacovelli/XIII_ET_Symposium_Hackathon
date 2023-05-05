The presentation and explanation in this folder are rendered with [`quarto`](https://quarto.org/).

The source files, `fisher-explanation.qmd` and `fisher-presentation.qmd`, are 
human-readable markdown with embedded scripts to generate the figures.

The figure scripts within the documents are in `python`, with dependencies
as outlined in `pyproject.toml`.
One can install everything in the current environment with `pip install .`; 
alternatively, an easy way to create a virtual environment and have everything
that's required there is to install [`poetry`](https://python-poetry.org/)
and run `poetry shell` followed by `poetry install`.

In order to generate the html explanation, after [installing quarto](https://quarto.org/docs/get-started/) run:

`quarto render fisher-explanation.qmd`

This will run all the embedded scripts.
Or render it to pdf:

`quarto render fisher-explanation.qmd --to pdf`

Similarly, render the presentation with:

`quarto render fisher-presentation.qmd`
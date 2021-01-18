# Hungarian NER templates

This directory contains the Hungarian NER CHECKLIST templates in CSV format. These templates are created by [Veronika Vincze](mailto:vinczev@inf.u-szeged.hu).

Besides the templates, it contains python scripts for generating sentences from CSVs and postprocessing them for NER model-ready input and for evaluation purposes. The CVSs had multiple versions, so there is no universal solution for this problem. Running a script makes 3 variants(Basic, Negation, Word Order) for input and it also makes their true counterpart for validation.

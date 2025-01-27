
# Some overall ideas on how to tackle this task, as well as a TODO list of items to cover.

- Input json file (as a path to the CLI). Maybe this is a drag & drop to get the full file path
- parse the json input into an iterable object (worth defining a class?)
- the class needs to be able to read the file and test for structure. exit if not compliant with appropriate notification.
- need to create a file spec for the user to know what structure the file should take.

## parser
- [x] obv parse entries and determine something... :)
- for now there seems to be two patterns of:
	- [x] start with *NUM + SPACE + TEXT (all caps)* without brackets.
	- [x] start with *NUM + . + TEXT (Camelcase/no casing) + :*
- [x] maybe have a config/yaml file with regex expressions the user can select and apply?
- [] if user doesn't want to use regex from config file, include an optional param in CLI?

## larger labelled dataset thinking.
- define a suitable metric, in a notebook we'll count the number of headers in our two docs, but the intuition is that there will be less headers than non-headers, leading to class inbalance. F1-score?
- maybe there's really like 20 types of headers for NDAs and some clustering or frequency count would surface them?
- NER? I expect the headers to not have entities, just general title text like AGREEMENT, but not specifics, this would be clarified in the clauses.
- POS? maybe most of the titles (once we remove punctuation and numbers) are really just NOUN,ADJ,DET,ADP?
- [x] If we have a sequence of sentences, maybe we would find that a header is likely to be referenced in the sentence that follows? Here probably even Jaccard might yield a good enough result?
- RNN model if each paragraph is labelled as header/not-header. This would make it into a classification task.

## things to test/validate
- [x] input file type
- [x] input file content to comply with a json schema
- [x] black code
- [x] Dockerfile

## report/document (html/pdf/md?)
- solution
	- [x] overall description
	- [x] how you arrived at it
	- [x] known limitations
- Given a larger dataset...
	- [x] how would you assess the quality of your solution,
	- [] other inference methods might be appropriate

## literature

-	[Header and Footer Extraction by Page-Association](https://www.hpl.hp.com/techreports/2002/HPL-2002-129.pdf)
-	[Developing a Section Labeler for Clinical Documents](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4419880/pdf/1985976.pdf)
-	[PDF text classification to leverage information extraction from publication reports](https://www.sciencedirect.com/science/article/pii/S153204641630017X)
-	[PERFORMANCE MEASURES FOR INFORMATION EXTRACTION](http://ccc.inaoep.mx/~villasen/bib/slot%20error%20rate.pdf)
-	[Metrics for Evaluation of Ontology-based Information Extraction](http://ceur-ws.org/Vol-179/eon2006maynardetal.pdf)
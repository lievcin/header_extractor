# REPORT

## 0. Task statement
The goal of this task is to produce an algorithm that will extract headers from a document. The implementation should take the provided JSON format as input. Please provide your solution with an interface (with suitable methods or functions) that takes the document as input and returns a list of the indices of paragraphs containing headers.

### Literature review
A few resources were found during the research stage of the project.
They could be seen as those (like such as [Header and Footer Extraction by Page-Association](literature/HPL-2002-129.pdf)) that seek to extract headers/titles/footers from the structure (or ontology) of the document itself by relying on:
 - formatting
- position in page
- font sizes/type/weight
- grammatical parsing breaks, due to insertion of foreign text that breaks the narrative flow or grammatical correctness of sentences
- repetition of text across pages

and others, such as [Developing a Section Labeler for Clinical Documents](literature/1985976.pdf) or [Evaluation of a Method to Identify and Categorize Section Headers in Clinical Documents](literature/clinical_documents_headers.pdf), that attempt to extract interesting information from the unstructured documents by using *"a combination of natural language processing techniques, word variant recognition with spelling correction, terminology-based rules, and naive Bayesian scoring methods to identify note section headers"* where *"each document is initially processed by a section labeler that can effectively assign a standardized topic to each section"*.

In the latter case, the medical documents that the authors work with also benefit from having strong structural integrity and therefore entire paragraphs can be grouped together and assigned into predefined and standardized categories, such as:
- history and medical report
- discharge summary
- consultation report

This, intuitively seems similar to legal documents, where within a type of contract, similar headers and sections could be found, perhaps with variations of formatting and numbering.
*DISCLOSURE:* The time spent on this research was very limited, so the information in this section should be taken with a pinch of salt!

#### metrics found in literature
Precision, Recall and F1-score seem to be widely used for information retrieval tasks. However, it might be worth considering other metrics like Slot Error Rate (SER) suggested in [Performance Measures for Information Extraction](literature/slot_error_rate.pdf).

## 1. Overview of solution
At a high level, the project builds parsers that are able to read in the text in the paragraphs and decide whether the given (or previous) paragraph is a header.

### The flow is as follows:
1. User launches the command line interface (CLI) from the terminal and submits the path a file containing a JSON representation of a parsed Word/PDF/HTML document.
	- Additional options are available for the user to select:
		- Parser:
			- Regex (***Default***): Two patters are tried on the text of the documents and flagged as *Header* if a match is found.
			- Jaccard: A (tokenized) paragraph A if checked against the following (tokenized) paragraph B. Given a predefined *threshold*, if the number of tokens in A.intersection(B)/size(A) exceeds the threshold, the paragraph is flagged as *Header*.
		- Output type:
			- Index (***Default***): Returns the headers indices.
			- Text: Returns the headers text.
2. The file is checked for :
	- Existance.
	- Validity of JSON structure (ie, is it JSON?)
	- Validity of schema: The parsers expect certain fields to be present and to be of certain type.
3. With validations and checks completed, the document is parsed (using the default Regex or Jaccard parser), and the outputs are displayed to the user in the console.

## 2. Intuitions and limitations

### Patterns
task stament says: *"Legal agreements are typically quite structured documents. They usually open with a title and a declaration of the parties to the agreement. This is often followed by a declaration section where key terms are defined to disambiguate later clauses."*
Given that both documents headers displayed patterns that could be used, such as:
- **NUM + SPACE + TEXT (all caps)**.
or
- **NUM + . + (NUM) + TEXT (any case) + :**
it made sense to try a simple parser that could use those regular expressions to extract headers. This would be fast to execute in inference mode as well.

### Co-reference
The Jaccard parser was created as a quick and dirty co-reference identified between headers and the next paragraph. The idea here is that, as observed in the two sample NDAs, most of the headers words were repeated in the next (few) paragraphs. This works pretty well, but it does create false positives, classifying consecutive clauses that have high similarity as headers.

### Known limitations
- One file at a time, but it might be useful to be able to run against a folder full of parsed files in batch.
- Due to the limited sample size, so it's would be unreasonable to expect good performance on a larger dataset of NDA's as the strategies implemented will surely not cover the full spectrum of legal documents available.
- The project only identifies top level headers and not other subsections or items of interest. For deeper analysis and usefulness, a hierarchy of headers should be extracted.

## 3. Future work

### Larger dataset availability
As mentioned above, the current project has been built only based on a sample of 2 documents. Therefore, should access to a larger corpus of documents become available, the strategies might need expanding or customising. The project taxonomy has been designed to accomodate for such expansion needs, it does it as follows:
- **Configuration file:** Allows to add/configure new regular expressions in addition to the two existing ones.
- **Parser inheritance:** Entirely new strategies could be created alongside the existing ones by inheriting from the base parser and expanding the necessary custom methods it would require.

### Metrics
Given a larger labelled corpus, one way to measure how well a strategy performs is using the **F1-score**. There's some class imbalance between the header/non-header classes, and therefore a tradeoff between precision and recall that the business would need to decide on.  Specifically, what is the cost of labelling something as a header when it isn't (false-positive) or not labelling a header (false negative).
Another potentially interesting metric could be the **[Matthews Correlation Coefficient (MCC)](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.matthews_corrcoef.html)** which is meant (from literature) to be more robust to class imbalances.


### Potential new strategies
In no particular order.
- **Counting:** maybe there's a limited number of headers for NDAs and some simple frequency count would surface them? Given a large corpus of different NDAs and simplifying the text might yield a comprehensive lookup dictionary.
- **NER:** Headers might not contain any recognisable entities and use very general language. Words such as agreement, disclosure, material. But non-header paragraphs might need to be more specific and name items/places/dates/products.
- **POS:** Similar intuition to the item above, maybe most of the titles (once punctuation and numbers are removed) are really just NOUN,ADJ,DET,ADP.
- **RNN model:** given a larger corpus, and labelled paragraphs as *header/not-header*, then sequence models could be explored, here the paragraph could be passed through an architecture like this:
	- Embedding layer / Pretrained embeddings like Glove
	- LSTM layer
	- CRF or just softmax.
- **Naive Bayes:** given a corpus of labelled examples, prior probabilities could be calculated for the presence of specific headers depending on their location in the document, as well as the probabilistic sequential order for section headers. For example the likelihood of DISCLOSURE header appearing near the beginning of the document, as well as after/before other common headers.
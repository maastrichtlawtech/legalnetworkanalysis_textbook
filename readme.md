
# Legal Network Analysis Textbook

Work in progress...


## Changes summer
* Added text distance information
* spell checking
* etc

## Changes June 18
* Addressed the To Do list items assigned to Gijs

## Changes June 13
* Tidied up imports
* Improved plot for shortest path
* Fixed weighted edges with improved plots and an explanation of closeness vs distance
* Improved the example in in-degree centrality to one that allows more visual exploration
* Fixed eigenvector centrality (mistake was that I used the contigency matrix whereas this one uses the adjacency matrix). The error should no longer pop up.
* Fixed the outputs of the centrality measures to be in descending order and neat (either print or dataframe print to html).

* to consider: do we want to use helper functions to shorten the code for printing results? It is neater, but possible less pedagogical as the learner will have to go find where the function is defined in order to understand what happens.

## To do list as of 27 May 2022:
* Add examples in 1.3. -> GIJS -- done
* The section on closeness centrality is quite complicated. I need to give that another read. -> GIJS -- done
* Same for section on Eigenvector Centrality (the second paragraph is extremely clear). -> GIJS -- done
  * @GUSTAVO: The sentence "Afterwards the vector is "normalized"  by dividing its by its norm: " is not clear to me.
* There is an error in:
  vals, vecs = np.linalg.eig(C)
  vals
  but I couldn't detect what it is (probably replace C?) -> GUSTAVO (could already be fixed in V11)  --- Fixed now
* This I didn't understand: "the ratio of links in the community to the total number of links minus the ratio of links you would expect to find randomly in a community to the total number of links." -> GUSTAVO
* We need to look at the Modularity section. -> GUSTAVO
* Expand on 'edge list' at the end of 6.3. -> GIJS
* Integrate 5.3 into 6.3. -> Roland -> Done
* Add relevant literature to each section. -> ALL

## Attention points as of April 21
* Functions of network analysis: exploratory and confirmatory -> RQ section (GIJS)
* Use images for recurring plots, instead of plotting all the time (mostly done) -> use code where possible (GUSTAVO)
* Do we want an example of a shortest path algorithm in pseudo code? -> let nx compute it
* Figure out what is the difference between EC and pagerank. -> GIJS
* Fix page rank -> GUSTAVO
* Fix Louvain -> necessary? will be part of new revision
* Can we avoid JSON? -> Avoid
* Beautify code or output in sections noted. Decide whether to use images or code print outs for this. -> use code where possible (GUSTAVO)
* Apply python conventions thorough (see next cell)

## Python conventions 
* Please make sure the code cells can be run in order. I.e: first declare variables (e.g. load data into a dataframe), then use them. 
* All variable names should be lowercase. Uppercase names are reserved for class declarations and instantiations.
* When loading the same data into different data type objects, please add a prefix/suffix to the variable names indicating the data type (e.g. the 'kite' data set loaded once into a dataframe, once into a graph, and once into a matrix could be referred to as: df_kite, g_kite, m_kite). This is a good habit even if the data is only stored in one object.
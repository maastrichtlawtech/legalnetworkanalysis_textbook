****

* Consistency that every chapter has intro / conclusion and not just a list of stuff. Narrative structure
* Make all examples legal as if possible. @Gijs: added CJEU example on consumer protection in various sections. Also: went through the text and explained the legal relevance for the examples we show.

**** 
1. It would be nice to have a large_n example of a power law distribution. Any suggestion of ready at hand yet comprehensible networks? @Gijs -> DONE

2. I think we can get rid of the trains examples in directed degree centrality, because the Karate Club is enough and more based on literature @Gustavo

3. The legal history network should go in a section 2.4 to be written which explains how to have networks with meta-data. I don't yet know how to implement that, but then you can make qualitative distinctions between node types (nodes with this or that attribute), color them differently, and query the network depending on certain node attributes. @Gustavo

4. The document similarity network build-up must be explained slower and moved to an appendix or new section of "practical examples". It is too convoluted for what needs to be explained. We can keep the network, but move "how it was made" elsewhere. @Gijs -> I THINK @GUSTAVO MOVED THE TEXT TO AN APPENDIX. I WOULD BE MORE IN FAVOR OF ADDING A SECTION ON 'WEIGHTED NETWORKS' TO CH3, WHERE DOCUMENT SIMILARITY IS DISCUSSED. IT IS AN IMPORTANT TOPIC. THE ONLY THING WE NEED TO DO, HOWEVER, IS TO REPLACE THE EXAMPLE WITH A LEGAL EXAMPLE (EG CJEU CASES). I COULD ASK AN ASSISTANT TO WORK ON THAT.

5. The results of closeness centrality should be presented as a dataframe, with the degree results side by side. @Gustavo

6. There must be a discussion about when/if centrality scores can be presented as a percentage (ie. normalized). I would think this is generally the right way to do things. All scores need to be normalized if possible (maybe normalization is not alawys desirable). @Gijs -> WE DON'T NEED TO DO ONE OR THE OTHER. IT DEPENDS ON WHAT YOU WANT TO KNOW. I EXPLAINED THIS IN THE REVISED SECTION 3.1.

7. Fact check if Eigenvector centrality is a percentage as presented, or if it needs to be normalized first @Gijs -> FROM WHAT I'VE READ, IT'S NOT A NORMALIZED SCORE THAT CAN BE NORMALIZED, BUT THAT NORMALIZATION HAS LITTLE VALUE. PROPOSAL: WE DO NOT DISCUSS THIS IN OUR TEXTBOOK. 

---

9. Furniture websites dataset needs replacement. The legal history dataset might not work, because it relies heavily on node attributes and does not have long chains of links. @Gijs -> DONE (replaced by case law network)

10. Update page rank and eigenvector centrality to explain that they consider the weight of who links to you (and contrast this with results of other scores). So closeness considers "long chains of links" behind you, but PR / EC consider size or popularity of who inks you. Put this at the beginning of section @Gustavo

11. HITS discussion relies on normalization, so this needs to be explained at the outset of centrality scores if not earlier (see point 6). @Gijs -> SAME ANSWER AS UNDER 6.

-----

13. For spectral clustering, some methods needs to be introduced, for finding the optimal number of communities. There must be something for this. Also, it would be nice to have some insight into why this works... @Vageesh

14. Maybe instead of a bibliography, some vignettes of useful studies would be better. @Roland


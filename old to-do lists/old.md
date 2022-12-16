# Changes and notes before moving to repo
# Delete as soon as convenient

## Notes Gustavo 5oct2022

- IPython.display.image is the only way I have found to make the images display at github and offline. But it changes the cell structure, because we need to put the images in a code cell instead of a markdown cell. Do we keep this? See the first two images to see how it would look.

## Notes Gijs 29sep2022 

- REVISED: "It is a bit hard to see, but note that this is a fully connected or complete graph. In this case it is not pointless to assess the centrality or community of its nodes, because the edges have different weights." -> Is this so? Can I not calculate, for instance, in-degree by multiplying the number of incoming edges with the edge weight? 

I think it is so, and I cleared up the text, and pointed to a fuller explanation in the section on closeness.

- In the train station example: Roosendal should be Roosendaal.

Fixed

- Discrepency of centrality measures discussed in Ch1 and Ch3. Decision to be made: How to align?

I think this can stay like this, because we don't promise that we will show all of them. I have minimally changed the text to make it clear that these are only some of the measures.

- I moved some paragraphs around for the centrality measures so that we first get a conceptual explanation and then the mathematical one (i.e. formulas).
- To discuss: do we need small/short visualizations for the steps explained for, for instance, closeness centrality?
- We don't discuss HITS in Ch3. We should move it to there and stick to just the basic measures (degree / indegree / outdegree / betweenness) and discuss these and others in more detail in Ch3.
- In section 3.3, should the adjacency matrix be called A ("A = ...")? This is confusing.

Indeed it is. I have tried to remove confusion. I also removed the subway stations. As a matter of literary style, the stations come up once and never show up again... 

- Section 3.3: "Afterwards the vector is "normalized" by dividing it by its norm". What does "dividing it by its norm" mean?

I added some explanation. I am sort of figuring this out too.

- I don't understand the text of section 3.3 that starts with "Finally let us approach it from the perspective of eigenvalues and eigenvectors. The largest eigenvalue here is 4.3. This is in index position 0." and continues with the eigenvalues and then the eigenvectors again. Perhaps you (Gustavo) can explain this to me and I'll try to update the text.

It should be clearer now!

- I don't follow section 4.1. Would it be an idea to swap 4.1 and 4.2? It would also help me if Gustavo could walk me through the section.
- Some errors in the code (code does not run).
- When calculating the modularity, there is a factor 10 difference between the figure and the calculation that follows.
- The section on Louvain community detection reads well overall. Great effort making this more explainable.
- I swapped Ch5 and Ch6.
- I would delete the spare text in the last paragraph (**### where to enter this type of info?**) in 5.3.

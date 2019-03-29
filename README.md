# A* Search

The A * algorithm is an improved version of the Dijkstra algorithm. While in Dijkstra it searches for the smallest path among all possibilities, the algorithm of A * does a search giving preference to a path that, in relation to the destination, will have the shortest distance. In Dijkstra, he may end up going further if the neighbor has the slightest path to himself. In A *, if the neighbor that has the smallest path in relation to the current point is distancing itself from the destination, the algorithm will prefer another neighbor, even if in relation to the present one this neighbor has a greater distance but has the smallest distance between it and fate among the given possibilities.

In this work, an algorithm was developed using A * to trace the front door paths of an intelligent house to the comfortable one in which an emergency alarm was triggered. In the initial phase, de facto sensors are not used, thus using a menu with the options of each enclosure, so when choosing an enclosure, the code is treated as if a sensor had been fired in that room, thus tracing the best way to it.

#### References 

[A* Searcj Algorithm](https://en.wikipedia.org/wiki/A*_search_algorithm). 

[Geeks For Geeks](https://www.geeksforgeeks.org/a-search-algorithm). 

[Let's Learn Python #20 - A* Algorithm](https://www.youtube.com/watch?v=ob4faIum4kQ).

[A* (A Star) Search Algorithm - Computerphile](https://www.youtube.com/watch?v=ySN5Wnu88nE).

[A* (A Star) Search Algorithm - geekforgeeks](https://www.youtube.com/watch?v=ySN5Wnu88nE).

[A* Pathfinding (E01: algorithm explanation)](https://www.youtube.com/watch?v=-L-WgKMFuhE).

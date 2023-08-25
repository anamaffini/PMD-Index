# Potential Movement Difference Index

The PMD Index plugin performs a set of metrics based on graph theory which depict properties of urban networks. The metrics were conceived in the context of the [**Urban Systems Research Group**](https://www.ufrgs.br/sistemas-urbanos/en/) from the **Federal University of Rio Grande do Sul (UFRGS)**, Brazil, by researchers **Gustavo Maciel Gonçalves** and **Ana Luisa Maffini** and programmed by Ana Luisa Maffini.

The measures are based on the Polarity model, first proposed by Krafta (1996) and the plugin was based on GAUS – Graph Analysis or Urban Systems.

Potential Movement (PM) is defined as the frequency with which streets in the urban street network belong to the shortest paths of a population when heading to urban facilities. In this sense, it can be taken as an indicator of population flows within urban systems.



The PMD Index plugin considers origins and destinations locations to estimate potential movements. It also uses weights according to the size (i.e.: attractiveness, magnitude) of destination locations and the size of origin locations (i.e.: number of people or households). 

The plugin calculates the differences in the Potential Movement values of specific populations’ groups when compared to a general value of Potential Movement (see The PMD Index metrics section). Currently, the PMD Index plugin calculates eight measures: 

- The General Potential Movement (GPM) 
- The Potential Movement for a Group A of the Population (PMa) 
- The Potential Movement for a Group B of the Population (PMb) 
- The normalized value of GPM 
- The normalized value of PMa 
- The normalized value of PMb 
- The Potential Movement Difference for Group A (PMDa) 
- The Potential Movement Difference for Group B (PMDb)

## The PMD Index metrics

### Potential Movement

The Potential Movement (PM) indicator is a network centrality measure. It is restricted to ordered pairs of nodes, which represent the locations of origins and destinations. Only the pairs with these opposite attributes are considered in the calculation. 
For origin nodes, the PM uses the location of the households weighted by the number of residents. 
For destination nodes, different activity spaces can be considered. They are usually weighed by the number of establishments in the node. 

### Normalized Potential Movement

After computing the GPM and the two PM metrics (PMa and PMb), the plugin normalizes the values by the total amount of population that was considered in the metric. For the GPM, that number is the total amount of the city’s population, whereas for the PMa and PMb, it is the total amount of that specific population group. 

### Potential Movement Difference

PMD is the difference between the population group PM and the GPM. It indicates how different the PM values of that population are when compared to what they might be if the entire population of the city belonged to that population’s group. 


# The PMD Index Plugin

## Installation



## Interface



### Input vector layer
the user is required to select a vector layer as input. The vector layer must be of a LineString geometry type and can have any CRS, although the user must be aware that for geometric calculations the CRS must be a projected CRS. Linkar com o wiki do GAUS (connection rules). 

### Analysis Type
indicates how the distance between lines will be computed. There are two types of analysis: topological or geometric. In topological analysis, the distance is considered equivalent to 1 between each pair of neighboring lines. In geometric analysis, the Euclidean distances measured in QGIS between the centroids of adjacent lines are considered. Linkar com o wiki do GAUS (how distance is computed)

### Connecting rule
indicates the type of map that the input vector layer corresponds to (i.e.: axial map, segment map, center lines map, street names map, etc.). There are three options: “overlapping vertices”, “crossing lines”, and “overlapping vertices + crossing lines”. Linkar com o wiki do GAUS (connection rules)

### Radius (optional)
can be used to designate a Global or Local analysis. When the radius is set at 0, a global analysis of the metrics will be run. If the user sets a different value, then a local analysis will be performed. The radius provided by the user must be according to the analysis type (topological or geometric).

### Impedance, destinations and origins
for each of these inputs, the user must prepare separate columns in the table of contents, identifying their values (or weights, in the case of the destinations and the origins) for each node in the network. In the calculation, the impedance values multiply the distance values between pairs of nodes, thus artificially reducing or increasing the real length of the lines. It is an optional field: if the user does not input an impedance column, the algorithm considers the value as 1. The origins and destinations are not optional: if the user does not provide the input field, the plugin will not run. 

### Output vector layer
Finally, the user must inform the output vector layer. 

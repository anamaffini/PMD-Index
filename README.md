# PMD Index

**PMD Index** is a plugin for calculating a set of urban network metrics in QGIS that was developed by [Ana Luisa Maffini](https://github.com/anamaffini) and [Gustavo Maciel Gonçalves](https://github.com/gustavo-m-goncalves) in the [Urban Systems Research Group](https://www.ufrgs.br/sistemas-urbanos/en/) at the Federal University of Rio Grande do Sul (UFRGS) in Brazil.\
The PMD metrics are based on a refined network betweenness centrality model named Polarity, which was conceived by professor [Romulo Krafta](https://www.researchgate.net/profile/Romulo-Krafta).

**Potential Movement** is the frequency with which streets in the urban street network belong to the shortest paths of a population when heading to urban facilities, which can be taken as an indicator of population flows.

The PMD Index plugin considers origins and destinations locations to estimate potential movements. It also uses weights according to the size (i.e.: attractiveness, magnitude) of destination locations and the size of origin locations (i.e.: number of people or households). 

The plugin is written in Python, and it's algorithm was developed by [Ana Luisa Maffini](https://github.com/anamaffini) at Chalmers University during her time as a visitor PhD researcher, and it is based on the script GAUS, developed by [Guilherme Dalcin](https://www.researchgate.net/profile/Guilherme-Dalcin) in the [Urban Systems Research Group](https://www.ufrgs.br/sistemas-urbanos/en/).

Check out PMD Index documentation [here]().

**Contact:**\
Ana Luisa Maffini: analuisamaffini@gmail.com / analuisamaffini@ufrgs.br\
Gustavo Maciel Gonçalves: gustavomacielg@gmail.com  / gustavo.goncalves@gutech.edu.om


License
-------
Copyright 2023 Ana Luisa Maffini

PMD Index Plugin is free software: you can redistribute it and/or modify
it under the terms of the GNU Lesser General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version. The GNU Lesser General Public License
is intended to guarantee your freedom to share and change all versions
of a program--to make sure it remains free software for all its users.

PMD Index Plugin is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
GNU Lesser General Public License for more details.

You should have received a copy of the GNU Lesser General Public License
along with PMD Index Plugin. If not, see <http://www.gnu.org/licenses/>.

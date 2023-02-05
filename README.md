# CSCI 3302: Modified Algorithm — FSVRPLW
<p align="justify"><b>CSCI 3302</b> or <i>Data Structures & Algorithms II</i> is a course instructed by <b>Dr. Nurul Liyana Binti Mohamad Zulkufli</b> and offered by <i>International Islamic University, Malaysia.</i> All codes including documentation in this repository were written and prepared by <b>Muhammad Hadif Bin Mohd Hatta (matric  2114589)</b>.</p>

<p align="justify"><b>FSVRPLW</b> stands for <i>Flight Speed-aware Vehicle Routing Problem with Load and Wind</i> and is one of the <a href="https://en.wikipedia.org/wiki/NP-hardness">NP-hard problems</a>. The dynamic programming approach to this problem is finding the optimal route that minimizes the total flight time. The payloads influences the flight speed, the heavier the weight, the slower it will be. The goal is to calculate the shortest time for the drone to deliver all the packages.</p>
  
  
### Journal Reference
<div class="csl-entry">Ito, S., Akaiwa, K., Funabashi, Y., Nishikawa, H., Kong, X., Taniguchi, I., &#38; Tomiyama, H. (2022). Load and Wind Aware Routing of Delivery Drones. <i>Drones</i>, <i>6</i>(2). https://doi.org/10.3390/drones6020050</div>
  
  
### Pseudocodes for FSVRPLW
```
Input: N: Number of customer, W: Payload of each customer,
 C: Coordinates of each customer, Vw: Wind Vector

Output: Optimal Route: The route that minimizes the total flight time
Wall ← ΣW

for Next ∈ C do
  FT[1 << (Next - 1)][Next] ← FlighTime(depot to Next)
  Payload[1 << (Next - 1)] ← (Wall - Wnext)
end for

for Visited ∈ 0, 1, 2, ..., (2N-1) do
  for Next ∈ C do
    if Next has not already visited then
      for Previous ∈ C do
        if Previous has been already visited then
          FT[Visited|(1 << (Next - 1))][Next] ← min(FT[Visited][Previous] +
          FlightTime(Previous to Next), FT[Visited|(1 << (Next - 1))][Next])
          Payload[Visited|(1 << (Next - 1))] ← Payload[Visited] - Wnext
        end if
      end for
    end if
  end for
end for

MIN_TIME ← INFINITE

for Previous ∈ C do
  MIN_TIME ← min(FT[2N-1][Previous] + FlighTime(Previous to depot), MIN_TIME)
end for
```

### Coding & Known Issue
The python implementation for this dynamic programming approach can be found below:
1. Basic algorithm - [Link](https://github.com/hdfhtt/CSCI3302_FSVRPLW/blob/f698270dd29de2268275552e172d120298427f6f/main.py)
2. Modified algorithm - [Link](https://github.com/hdfhtt/CSCI3302_FSVRPLW/blob/main/main.py)

<p align="justify">However, the <b>modified algorithm</b> is not working as some part requires high levels knowledge of understanding in order to be implemented. This problem has also been issued in <b>StackOverflow</b> which can be found <a href="https://stackoverflow.com/q/75266932/9260075">here</a> and has been labelled as <b>todo</b> in the coding file. The parts related are as follow:</p>  

`FT[Visited|(1 << (Next - 1))][Next] ← min(FT[Visited][Previous] + FlightTime(Previous to Next), FT[Visited|(1 << (Next - 1))][Next])`
  
  
### Performances
| Complexity | T(n) |
| :--- | :---: |
| Time | ? |
| Space | ? |

<sub>* *Time and space complexity are yet to be identify as the code is currently not working.*</sub>
  
  
### License
The project is licensed under **MIT License**, the terms of which are available in [LICENSE.txt](https://github.com/hdfhtt/CSCI3302_FSVRPLW/blob/main/LICENSE).

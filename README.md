# CSCI 3302: Modified Algorithm - FSVRPLW
**FSVRPLW** stands for *Flight Speed-aware Vehicle Routing Problem with Load and Wind* and is one of the [NP-hard problems](https://en.wikipedia.org/wiki/NP-hardness). The dynamic programming approach to this problem is finding the optimal route that minimizes the total flight time. The payloads influences the flight speed, the heavier the weight, the slower it will be. The goal is to calculate the shortest time for the drone to deliver all the packages.

### Journal Reference
<div class="csl-entry">Ito, S., Akaiwa, K., Funabashi, Y., Nishikawa, H., Kong, X., Taniguchi, I., &#38; Tomiyama, H. (2022). Load and Wind Aware Routing of Delivery Drones. <i>Drones</i>, <i>6</i>(2). https://doi.org/10.3390/drones6020050</div>

### Pseudocodes for FSVRPLW
```
Input: N: Number of customer, W: Payload of each customer,
 C: Coordinates of each customer, Vw: Wind Vector

Output: Optimal Route: The route that minimizes the total flight time
WallW

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


### Additional Notes
1. This project is a programming assignment assessed by the *CSCI 3302: Data Structures & Algorithms 2* course instructed by *Dr. Nurul Liyana Binti Mohamad Zulkufli* and offered by *International Islamic University, Malaysia*.
2. The python implementation of the this dynamic programming approach can be referred [here](https://github.com/hdfhtt/CSCI3302_FSVRPLW/blob/main/main.py). However, the code is not working as some part requires high levels of knowledge to implement and has been labelled as *todo*. 
3. The project is licensed under **MIT License**, the terms of which are available in [LICENSE.txt](https://github.com/hdfhtt/CSCI3302_FSVRPLW/blob/main/LICENSE).

Robert Bradshaw
rbradshaw6
3/12/2017
Assignment 2 - Randomized Optimization

Hey so I stole code from this nerd https://github.com/james7132/GTCourseWork/tree/master/CS%204641%20-%20Machine%20Learning/Randomized%20Optimization%20Assignment/jliu348
(except I don't run my stuff in a dumb way and I can make my readme consistent with what you actually have to do. :^) )

First, to compile everything:
>cd ABIGAIL
>ant
-------------------------------
RHC:
java -cp ABAGAIL.jar project2.SpambaseTest ./waveform-5000.arff rhc HIDDENLAYERS ITERATIONS
-------------------------------
Simulated Annealing:
java -cp ABAGAIL.jar project2.SpambaseTest ./waveform-5000.arff sa HIDDENLAYERS ITERATIONS INITIAL_TEMP COOLING_FACTOR
-------------------------------
Genetic Algorithm:
java -cp ABAGAIL.jar project2.SpambaseTest ./waveform-5000.arff ga HIDDENLAYERS ITERATIONS INITIAL_POP_SIZE MATES_PER_ITERATION MUTATIONS_PER_ITERATION
-------------------------------
FourPeaks:
java -cp ABAGAIL.jar project2.FourPeaksTest N T TRIALS > FILE_NAME
python analyze_results.py FILE_NAME
-------------------------------
FlipFlop:
java -cp ABAGAIL.jar project2.FlipFlopTest N TRIALS > FILE_NAME
python analyze_results.py FILE_NAME
-------------------------------
TSP:
java -cp ABAGAIL.jar project2.TravelingSalesmanTest N TRIALS > FILE_NAME
python analyze_results.py FILE_NAME

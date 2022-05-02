#!/bin/sh
python ../cs412_NP_Proj_Approx.py < small_adj_list_0.txt > small_solution_0.txt # 5 nodes 0.0001609325408935547
python ../cs412_NP_Proj_Approx.py < small_adj_list_1.txt > small_solution_1.txt # 10 nodes   0.00029015541076660156
python ../cs412_NP_Proj_Approx.py < medium_adj_list_0.txt > medium_solution_0.txt # 100 nodes 0.8918852806091309
python ../cs412_NP_Proj_Approx.py < medium_adj_list_1.txt > medium_solution_1.txt # 1000 nodes 1.09753464
python ../cs412_NP_Proj_Approx.py < medium_adj_list_2.txt > medium_solution_2.txt # 5000 nodes 1.592543117179
python .../cs412_NP_Proj_Approx.py < medium_adj_list_3.txt > medium_solution_3.txt # 2000 nodes 1.2045823065705
python ../cs412_NP_Proj_Approx.py < medium_adj_list_4.txt > medium_solution_4.txt # 3000 nodes 1.32207081948080
python ../cs412_NP_Proj_Approx.py < large_adj_list_0.txt > large_solution_0.txt # This test will run a long time - 10 000 nodes

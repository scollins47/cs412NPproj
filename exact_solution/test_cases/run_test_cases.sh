#!/bin/sh
python ../cs412_NP_Proj_Exact.py < small_adj_list_0.txt > small_solution_0.txt # 5 nodes      < 1 sec
python ../cs412_NP_Proj_Exact.py < small_adj_list_1.txt > small_solution_1.txt # 10 nodes     < 1 sec
python ../cs412_NP_Proj_Exact.py < medium_adj_list_0.txt > medium_solution_0.txt # 100 nodes  < 1 sec
python ../cs412_NP_Proj_Exact.py < medium_adj_list_1.txt > medium_solution_1.txt # 1000 nodes ~10 seconds
python ../cs412_NP_Proj_Exact.py < medium_adj_list_2.txt > medium_solution_2.txt # 5000 nodes ~13 minutes
python ../cs412_NP_Proj_Exact.py < medium_adj_list_3.txt > medium_solution_3.txt # 2000 nodes ~55 seconds
python ../cs412_NP_Proj_Exact.py < medium_adj_list_4.txt > medium_solution_4.txt # 3000 nodes ~3 minutes
python ../cs412_NP_Proj_Exact.py < large_adj_list_0.txt > large_solution_0.txt # This test will run a long time - 10 000 nodes

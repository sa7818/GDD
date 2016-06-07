#CMSC6950 course project
SRC=./src
All: Download
Download:
	$(shell cd $(SRC); python3.5 csvlink.py)

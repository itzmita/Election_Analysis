# Election_Analysis

## Overview of Project
A Colorado Board of Elections has requested to complete the election audit of a recent local congressional election.

	1. Calculate the total number of votes cast.
	2. Get a complete list of candidates who received votes.
	3. Calculate the total number of votes for each candidate received.
	4. Calculate the percentage of votes each candidate won.
	5. Determine the winner of the election based on popular vote.
	6. Calculate the voter turnout for each county.
	7. Calculate the percentage of votes from each county out of the total.
	8. Determine the county with the highest turnout.


## Resources: 
	• Data Source: election_results.csv
	• Software: Python 3.9.1, Visual Studio Code 1.52.1

		

## Challenge Overview

As per the above analysis we were able to find out who was the winner candidate.
The Final Challenge requirement was to find out few more additional details such as below

	• The voter turnout for each county  
	• The percentage of votes from each county out of the total count  
	• The county with the highest turnout
  
We worked from the same election_results.csv file wrote additional code to find the above 3 results as well.



### Deliverable 1: The Election Results Printed to the Command Line
We analyzed 2 types of outcomes as shown below

#### Candidate Results:
Attached terminal screenshot show all the candidate's results and who the winner was

![image](https://user-images.githubusercontent.com/3753839/164590848-ae1a3103-1fc3-4e03-acf3-fe2f04977a5d.png)


#### County Results:
Attached terminal screenshot show turnout for all the counties and which county had the largest turnout

![image](https://user-images.githubusercontent.com/3753839/164590860-e6355386-6c96-433e-87ae-b375c6ead320.png)



### Deliverable 2: Election Results Saved to a Text File
Attached screenshot show the results for Candidate and County are printed in the output file 'election_results.txt'

![image](https://user-images.githubusercontent.com/3753839/164590888-956065eb-ed1c-446d-b6fb-c27e83323f14.png)




### Deliverable 3: Written Analysis of the Election Audit

#### Overview of Election Audit: 
Analyzed Election data for Colorado board of elections using Python programming.
These votes were captured from 3 different methods such as 
  * Mail-in-Ballots
  * Punch-cards
  * DRE(direct-recording electronic counting)

In the module we learnt how to include dependencies

![image](https://user-images.githubusercontent.com/3753839/164590966-3ad1ee47-acab-427f-bf26-0ed52f2bb87f.png)


The csv import allows us to use certain operations of csv module such as next() which is used to skip a row if needed. In here we skipped the Header row. Another operation used was reader() which helps in reading row by row from the file and create a list for us which can be looped through using a for loop to calculate various items like voter counts.

The os import helps us to join file path and file names to give us the actual path in our systems. We used the path() and join() operations in this assignment

![image](https://user-images.githubusercontent.com/3753839/164590994-0ee03a42-b0e6-4444-a3a8-8d1570736c60.png)


We learnt how to open a file using "with open" which takes care of closing the file as well 

![image](https://user-images.githubusercontent.com/3753839/164591001-f56a5083-2208-43df-be79-7223fcebe3ad.png)



We used for loops to go through the list of data and evaluated the candidates one by one while counting the votes for each of them. 

![image](https://user-images.githubusercontent.com/3753839/164591016-79a776bf-e936-4a3c-8cbc-65fd6deba901.png)


A similar logic was created for county as well. We wanted to get the voters by counties.

![image](https://user-images.githubusercontent.com/3753839/164591686-36a3b71b-4369-4359-8268-10c235f934bf.png)



We created a dictionary of candidates and the number of votes as well so that we can calculate the percentage of votes looping through this dictionary.


We learnt to open a file in write mode to output our results.

![image](https://user-images.githubusercontent.com/3753839/164591040-5d9b2d72-32a3-452f-8c14-8b56b31baa15.png)




Before writing to the file, we calculated the percentage looping through the candidate and county dictionary separately.

Here is looping through the candidate dictionary to calculate individual county's voter turnout percentage as well as largest turnout percentage 

![image](https://user-images.githubusercontent.com/3753839/164591099-bc24de2b-916b-4a0d-9748-714537ad467e.png)


Here is looping through the candidate dictionary to calculate individual candidate's voting percentage as well as winning percentage 

![image](https://user-images.githubusercontent.com/3753839/164591117-87437d7a-d0d0-412b-b22c-d85ac3e93f51.png)


The below lines help write the data to the output file.

![image](https://user-images.githubusercontent.com/3753839/164591811-b4c12893-ce06-4f16-a2e7-b376a2fb9058.png)

![image](https://user-images.githubusercontent.com/3753839/164591824-6d1b7682-a319-46a8-8d1f-fc603b87b0d6.png)



#### Election-Audit Results: 
	• There were a total number of 369,711 votes casted as we see from the dataset "election_results.csv" provided.
      These results were collated in the csv file provided to us. 
      There are 3 columns Ballot ID, County, and Candidate Name based off of which we did our analysis.
	• The voters were from 3 Counties
		○ Jefferson
		○ Denver
		○ Arapahoe
	• There are 3 candidates
		○ Charles Casper Stockham
		○ Diana DeGette
		○ Raymon Anthony Doane
	• The candidate results were
		○ Charles Casper Stockham received 23.0% of the total votes and 85,213 number of votes
		○ Diana DeGette received 73.8% of the total votes and 272,892 number of votes
		○ Raymon Anthony Doane received 3.1% of the total votes and 11,606 number of votes
	• From the above results we can clearly see the winner of the election was 
		○ Diana DeGette who received 73.8% of the total votes and 272,892 number of votes
	• The voter turnout for each county was
		○ Jefferson county had 10.5% voter turnout and 38,855 number of voters
		○ Denver county had 82.8% voter turnout and 306,055 number of voters
		○ Arapahoe county had 6.7% voter turnout and 24,801 number of voters
	• The county with the largest voter turnout was
		○ Denver county which had 82.8% voter turnout and 306,055 number of voters


#### Election-Audit Summary: 

This code was created based off of only 3 data points Ballot ID, county and Candidate Name given in the dataset. The Election commission can modify this script a tiny bit to get more audit related information. Such as if we can tweak the code to make it calculate the performance of a candidate based on county. We can introduce another dictionary which can be a nested dictionary or a dictionary inside a list of candidates. This can have for each candidate as key , the nested dictionary with county as the key and values as and the number of votes for that candidate in that county. Something like this   
Candidate_dict = {
"Charles Casper Stockham" : {"Arapahoe":"8302", "Denver": "57188", "Jefferson": "19723"}, 
"Diana DeGette": {"Arapahoe": "15647", "Denver": "239282", "Jefferson": "17963"}, 
"Raymon Anthony Doane": {"Arapahoe": "852", "Denver": "9585", "Jefferson": "1169"}

This will give an opportunity for the candidate to find why they did or did not do well in a certain county. They may want to approach the voters with different strategy to win the next time. 

Also if election commission wants they can add more elements to this data set such as age of the voter, demographic of the voter etc. Again the code can be modified to have the candidates votes shown in a nested dictionary. In this case the nested dictionary can have keys like age bands for example. 16-24, 25-40 , 41-60, more than 60 etc. The demographics and age will also help a candidate understand if they are doing well among elderly/adults or a specific demographics etc. Basically the same code can be utilized to extend similar analysis to other regions in Colorado by using a similar csv spreadsheet with different data. Or we can make modifications to add more parameters in case more drill down is necessary.


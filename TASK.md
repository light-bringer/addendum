Task 1

Given 3 int values, a b c, return their sum. However, if any of the values is a teen -- in the range 13...19
inclusive -- then that value counts as 0, except 15 and 16 do not count as a teen. The input is passed as
command line arguments and output is to be printed on screen

Examples
Input Output
python app.py 1 2 3 6
python app.py 2 13 1 3
python app.py 2 1 14 3
python app.py 2 1 15 18
python app.py 1 2 Exactly 3 numbers are required
python app.py 1 2 a All inputs must be numeric

Deliverables
Solution must contain the following files and be pushed to a GitHub repository.
• A well-documented python script for the above task
• README.md
• Unit testing script (https://www.geeksforgeeks.org/unit-testing-python-unittest/)
• requirements.txt



Task 2

Convert the script from task 1 to a REST API that accepts json input and returns json output
with appropriate error handling
Examples
Replace {INPUT} in the curl command below with inputs in the table
curl -H 'Content-Type: application/json' -X PUT -d '{INPUT}’ http://localhost:5000/sum
Input Output
[1,2,3] {“status”: 200, “result”: 6}
[2,13,1] {“status”: 200, “result”: 3}
[2,1,14] {“status”: 200, “result”: 3}
[2,1,15] {“status”: 200, “result”: 18}
[1,2] {“status”: 400, “error”: “Exactly 3 numbers are required”}
[1,2,”a”] {“status”: 400, “error”: “All inputs must be numeric”}

Deliverables
Solution must contain the following files and be pushed to a GitHub repository.
• A well-documented python script for the above task
• README.md
• Unit testing script (https://www.geeksforgeeks.org/unit-testing-python-unittest/)
• requirements.txt




Task 2
Dockerize the above application

Deliverables
Solution must contain the following files and be pushed to a GitHub repository.
• A well-documented python script for the above task
• README.md
• Unit testing script (https://www.geeksforgeeks.org/unit-testing-python-unittest/)
• requirements.txt
• Dockerfile




Our Team Culture:
• We provide hands-on statistical solutions for the automotive and manufacturing industry in Germany
to highlight trends and generate insights.
• We have closely worked with Deutsche Bahn, Linde, Liebherr creating AI for machines health and
work closely with their backend databases and data engineering teams.
• We act as the primary point of contact for business forecasting, delivering metrics/analytics that
drives the organization and helps senior management taking data-driven business decisions.
Location: Mumbai
To apply, please send an email, including your resume as an attachment, to careers@tvarit.com
About Tvarit
Industry 4.0 Market is expected to reach 152.31 Billion USD by 2022, at a CAGR of 14.72%. Germany, being the
headquarter to the world’s leading manufacturing and automotive companies, is seen as a major contributor to Industry
4.0 innovations. The increasing adoption of the industrial Internet, increased focus on efficient production, single day
plant shutdown costing millions of euro are the major drivers for the Industry 4.0 market.
We, at Tvarit, envision to create AI for manufacturing and focus on the implementation of Industry 4.0 in the industrial
equipment sector which helps manufacturers in analysing the machine conditions in advance to avoid unplanned
downtime and wastage.
Based on technology, the market has been segmented into industrial robotics in smart factories, cybersecurity,
advanced human-machine interface and artificial intelligence. The increasing use of industrial robotics in the automotive
sector is also a major reason for this technology to have the largest market share in the market. Being an early mover
in these segments, we have an advantage of tapping the huge potential in the manufacturing and automotive industry.
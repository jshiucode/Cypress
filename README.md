# Cypress Algorithm

## Description
Cypress is an algorithm which counts the links and knots within spatial graphs. The motivation for this project came from research done in Loyola Marymount University's mathematics department between Dr. Blake Mellor and Jordan Shiu, where we sought to find the minimal linking number of spatial graphs in the Heawood Family. It is usually near impossible to find all the links and knots within particular embeddings of these graphs by hand, so we engineered Cypress to do this task in seconds.

## Using Cypress Online:
Cypress currently lives in the backend of the graph visualization web-app found at https://graph-vis.vercel.app/. Click 'Run Algorithm' to run Cypress. Alex Abrams designed the front end of this graph visualization app.

## Using Cypress Locally:
After cloning, here's how one can use cypress on their local machine through Flask:
1. Create a virtual environment in python and install all dependencies listed in requirements.txt
2. Go into the virtual environment from CLI:
```
. .venv/bin/activate
```
3. Run flask_local.py as a Flask app (deploys at localhost:5000):
```
flask --app flask_local run
```
4. Use Postman or a similar application and add graph data to the body with the following example format:
```
0,1
0,2
1,2
2,3
2,4
3,4
4,5
5,6
5,7
6,7
7,8
0,8
2,4,7,8,1,2,-1
4,5,0,2,2,1,-1
5,7,1,2,1,2,-1
5,6,1,2,1,1,-1
2,3,7,8,1,1,-1
0,8,4,5,1,1,1
```
Edges are tuples where numbered vertices are seperated by a comma.
Crossings are 7-tuples a,b,c,d,m,n,k where:
- a and b are endpoints of the overcrossing edge
- c and d are endpoints of the undercrossing edge
- m is the order of this crossing along edge (a,b) counting from a to b
- n is the order of this crossing along edge (c,d) counting from c to d
- k is the sign of the crossing, assuming the edges are oriented from a to b and c to d.
    - The sign of the crossing is determined by the standard right-hand rule, as shown below:

    <img src="/Cypress/docs/right_hand_rule.jpeg">

5. Send a POST request with this data. The algorithm will run and output the number of links and knots in the graph.

# Genetic liability score
2016_04_28

##Returns 

- R, family matrix
- V, 0.7 multiplied on off-diagonal element of R
- G, genetic liability score for the family memebers

##Inputs

###number of family members in sequence of

** 0 if non or unknown **

- 1. grand parents on farther's side
- 2. grand parents on mother's side
- 3. father's siblings
- 4. mother's siblings
- 5. cousins (father's side)
- 6. cousins (mother's side)
- 7. siblings


##Example

```
python family_matrix.py 2 2 3 6 0 0 2

#1st number : number of grandparents on father's side
#2nd number : number of grandparents on mother's side
#3rd number : number of father's siblings
#4th number : number of mother's siblings
#5th number : number of cousins on father's side
#6th number : number of cousins on mother's side
#7th number : number of siblings
```


## Things under develop
- locating the cousins to a specific subject

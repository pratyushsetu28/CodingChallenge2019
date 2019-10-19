# modify this function, and create other functions below as you wish
def question01 ( p , r , repay ):
    # modify and then return the variable below
    c = 0 ;
    debt = p / 10 ; 
    rep = ((repay)*p)/100 ;
    if ( rep<50 ):
        rep = 50 ; 
    while ( p>50 ) :
        p = p - rep + (( p*r )/100) ; 
        c+=1 ;
    return int (c*rep + debt + p) ; 

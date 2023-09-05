from hello import add , div , mul , sub

def test_add():
    assert 4 == add(2,2)
    
def test_div():
    assert 2 == div(4,2) 
    
def test_mul():
    assert 4 == mul(2,2)
    
def test_sub():
    assert 2 == sub(4,2)               
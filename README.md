# Image Hash

This is just a quick concept that I messed around with.
Basically, this is a visualization of sha384 hash.

The alorithm is extremely simple.

1. Take the `SHA384` Hash of the given text string. `(line 12)`
    Here, I made the decision to take the hash of the lowercase string so as to
    avoid different hashes for different capitalizations of the same string.
2. Split the hash string into a set of tuples each of length 3 `(line 14)`
    This is not as complicated as it seems.
    Here is an example.  
    `  
    String = "abcdefghi"  

    Map = [  
        ( a, b, c )
        ( d, e, f )
        ( g, h, i )
        ]
    `
3. Loop through each tuple and use each of the three values as colors `(line 21)`
    This section is also really simple as SHA384 outputs 48 bytes. In tuples 
    of 3, this is 16 values.  I just represent this as 16 boxes each the color
    made by the values of the bytes in the tuples.

To run this simply run

    ` python imghash.py <text to hash>`

This will output a file that is `<text to has>.png`

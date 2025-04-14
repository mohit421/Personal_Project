```Strings

- 'some' +'text'>>'sometext'
- 'some' +'more'+'text' >>'somemoretext'

- typeof 2 >> number
- typeof 'hello' >> string

- if we add string to a numner sp JS will convert a number to string and then concatentated
- 'hello' +3 >> 'hello3'
- this feature is known as  type coercion or (automatic type conversion)
- '$' + 20.95 + 7.99 > '$20.957.99' //JS add from left to write
- '$' + (20.95 + 7.99) // there is an inaccuracy in floating point
- '$' + (2095+7.99)/100 >> '$28.94'

-------
- 'Items (' + (1+1) + '): $' + (2095+799)/100
>>'Items (2): $28.94'

- alert('Items (' + (1+1) + '): $' + (2095+799)/100)
```

```More Details about Strings
#### In Javascript basically there are three ways to create a strings
1. '...'
2. "...."
3. using backtick
- String created with backtick actually have a name we call these template strings and they
have some special features :-
1. Interpolation:- lets us insert a value directly into a string 
- for example:- Lets say we want to create the first line of text in our project 
earlier we have created this using concatenation
- we can create this using a template strings bcuz interpolation is only a feature of template strings so we'll type backtick 
- Interpolation is much cleaner way of inserting values into a string , So, it's a recommended solutions

2. Multi-line Strings:- Template string have another special feature called multi-line string
```
- `Items (${1+1}): $${(2095+799)/100}`
- alert(`Items (${1+1}): $${(2095+799)/100}`)
- Mutli line string
`some
text`
```
Character:
1. letter (a,b,c)
2. number(1,2,3)
3. symbol(!,@,#)
4. escape character '\'
```

```examples

- 'I'm learning JS' >> this will give syntax error
- "I'm learning JS" >> Double quotes string will be helpful in this case
- 'I\'m learning JS' >> It works with escape character
- alert('some\ntext')
```


- What should we use to create a string
1. Use '...' by default
2. If we need interpolation, multi-line strings use `...`

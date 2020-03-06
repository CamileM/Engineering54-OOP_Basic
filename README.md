# OOP Basics

This repo will contain our oop basics.

We will look at: 'C.R.U.D'

- Create
- Repeat
- Update
- Delete

– Abstraction
- Encapsulation
- Inheritance
- Polymorphism

## Class
Is like a cookie cutter, that creates instances of cookies. 

They are wrappers to define how an object looks and behaves. 

Classes will wrap characteristics as attributes, behaviours and methods. 

## Methods vs Functions.
Methods are functions that belong to a specific data type

Where Functions are anonymous

Where as **Methods NEED th instance to be called** 

## Characteristic: How an object looks like
These are attributes that are assigned to each instance

## Instance
An occurance of something. 

## Self
Refers to the instance on which a method is being called.

self.name = 'ringo'

This means that specific object attributes name will have the string 'ringo'

## Abstraction
The **ability to hide complexity**. 

We do this using:
- Separation of concerns
- Documentation
    - specify which methods and how to use them.
- Inheritance ---> causes some abstractions

Real Life Examples are everywhere:
- changing gears
- heating up food with one button
- using our cards to pass security


## Encapsulation

## Inheritance
The ability to pass to child class all the methods and characteristics. 

This is one of the big reasons for OOP - it means you can re-use code!

**Promise for reusable code**

you do this by passing the parent class as an argument by using the child's class.

```python
class Animal():
    pass

class Reptile(Animal):
    pass
```

## Polymorph
- Many forms

It is the ability to **COMPLETELY override methods**, and if need be, recall method from parent class using 
.super()

## .super()

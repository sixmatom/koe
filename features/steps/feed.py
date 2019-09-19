from behave import given, when, then  # pylint: disable=no-name-in-module
from koe import Cow, Feed

@given(u'the cow weighs {weight:d} kg')
def test_weight(context, weight):
        context.weight = weight
        

@given(u'the cow is {age:d} years')    
def test_age(context, age):
    context.cow = Cow(context.weight, age)
  

@when(u'we calculate the feeding requirements')
def feed(context):
    context.feed = Feed(context.cow)

@then(u'the energy should be {energy:d} MJ')
def test_energy(context, energy):
    assert context.feed.energy == energy


@then(u'the protein should be {protein:d} kg')
def test_protein(context, protein):
    assert context.feed.protein == protein
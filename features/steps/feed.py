from behave import given, when, then  # pylint: disable=no-name-in-module
from koe import berta, Feed

@given(u'the cow weighs {weight:d} kg')
def test_weight(context, weight):
    assert berta.weight == weight

@when(u'we calculate the feeding requirements')
def feed(context):
    context.feed = Feed()

@then(u'the energy should be {energy:d} MJ')
def test_energy(context, energy):
    assert context.feed.energy == energy


@then(u'the protein should be {protein:d} kg')
def test_protein(context, protein):
    assert context.feed.protein == protein
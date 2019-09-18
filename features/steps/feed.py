from behave import given, when, then  # pylint: disable=no-name-in-module
from koe import berta, Feed

@given(u'the cow weighs 450 kg')
def weight(context):
    assert berta.weight == 450

@when(u'we calculate the feeding requirements')
def feed(context):
    context.feed = Feed()

@then(u'the energy should be 26500 MJ')
def energy(context):
    assert context.feed.energy == 26500


@then(u'the protein should be 215 kg')
def protein(context):
    assert context.feed.protein == 215
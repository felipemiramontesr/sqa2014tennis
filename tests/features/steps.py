# -*- coding: utf-8 -*-
from lettuce import *
import app.match as m


@step(u'Given: "([^"]*)" and "([^"]*)" start a match to "([^"]*)" s')
def given_group1_and_group2_start_a_match_to_group3_sets(step, p1,
                                                         p2, s):
    world.match = m.Match(p1, p2, s)


@step(u'Then: I see score: "([^"]*)"')
def then_i_see_score_group1(step, score):
    assert world.match.score_set() == score, \
        "Got %s" % world.match.score_set()


@step(u'When: "([^"]*)" won the "([^"]*)" set "([^"]*)"-"([^"]*)"')
def when_group1_won_the_group2_set_group3_group4(step, p1,
                                                 numset, pp1,
                                                 pp2):
    world.match.save_set_won(p1)
    world.match.save_score_set(pp1,
                               pp2,
                               numset,
                               p1)


@step(u'And: "([^"]*)" won the "([^"]*)" set "([^"]*)"-"([^"]*)"')
def and_group1_won_the_group2_set_group3_group4(step, p1,
                                                numset, pp1,
                                                pp2):
    world.match.save_set_won(p1)
    world.match.save_score_set(pp1,
                               pp2,
                               numset,
                               p1)


@step(u'Then: The match score is: "([^"]*)"')
def then_the_match_score_is_group1(step, score):
    assert world.match.score_set() == score, \
        "Got %s" % world.match.score_set()

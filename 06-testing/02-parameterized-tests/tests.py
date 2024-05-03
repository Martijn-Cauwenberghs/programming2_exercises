import pytest
from matching_parentheses import matching_parentheses

@pytest.mark.parametrize('string', [
    '',
    '()',
    '()()',
    '(())'
])
def test_matching_parentheses(string):
    actual = matching_parentheses(string)
    assert actual == True, f'{string} has matching parentheses'


@pytest.mark.parametrize('string', [
    '(',
    ')',
    ')(',
    '()(',
    '(()))'
])
def test_nonmatching_parentheses(string):
    actual = matching_parentheses(string)
    assert not actual == True, f'{string} should not have matching parentheses'